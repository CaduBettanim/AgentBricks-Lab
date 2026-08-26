# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %md
# MAGIC # Desmontagem do Workshop: Agent Bricks Lab (`AgentBricks-Lab`)
# MAGIC
# MAGIC Reverte os recursos criados por `agentbricks_prep_checker`. **Idempotente**: qualquer coisa
# MAGIC já ausente é ignorada, portanto é seguro re-executar.
# MAGIC
# MAGIC Cada alternador é `true`/`false`. Os padrões removem os recursos **específicos do workshop**
# MAGIC (grupo, warehouse, cluster, volume faq_volume). Deletar o grupo também revoga todas as concessões feitas a ele.
# MAGIC
# MAGIC ⚠️ **`DROP CATALOG dbacademy` padrão é `false`**: o catálogo pertence ao administrador e contém
# MAGIC o schema `dbacademy.<username>` de cada participante e seus dados. Defina como `true` apenas se o notebook
# MAGIC de preparação criou o catálogo e o workshop foi completamente encerrado.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Parâmetros

# COMMAND ----------

dbutils.widgets.dropdown("delete_group", "true", ["true", "false"], "1. Excluir grupo do workshop")
dbutils.widgets.dropdown("delete_warehouse", "true", ["true", "false"], "2. Excluir SQL Warehouse")
dbutils.widgets.dropdown("delete_cluster", "true", ["true", "false"], "3. Excluir Cluster Multiuso")
dbutils.widgets.dropdown("delete_volume", "true", ["true", "false"], "4. Excluir Volume faq_volume")
dbutils.widgets.dropdown("delete_catalog", "false", ["true", "false"], "5. REMOVER CATÁLOGO (DESTRUTIVO)")

# COMMAND ----------

from databricks.sdk import WorkspaceClient

w = WorkspaceClient()

# Convenções fixas, deve corresponder ao notebook de preparação.
CATALOG = "dbacademy"
GROUP = "dbacademy_workshop"
WAREHOUSE_NAME = "dbacademy_workshop_wh"
CLUSTER_NAME = "dbacademy_workshop_cluster"
VOLUME_SCHEMA = "default"
VOLUME_NAME = "faq_volume"
VOLUME_FULL_NAME = f"{CATALOG}.{VOLUME_SCHEMA}.{VOLUME_NAME}"

DELETE_GROUP = dbutils.widgets.get("delete_group") == "true"
DELETE_WAREHOUSE = dbutils.widgets.get("delete_warehouse") == "true"
DELETE_CLUSTER = dbutils.widgets.get("delete_cluster") == "true"
DELETE_VOLUME = dbutils.widgets.get("delete_volume") == "true"
DELETE_CATALOG = dbutils.widgets.get("delete_catalog") == "true"

OK, NO, ERR, NA = "✅", "❌", "⚠️", "➖"

def _acct_scim(method, path, **kw):
    return w.api_client.do(method, f"/api/2.0/account/scim/v2{path}", **kw)

print(f"Grupo:     {GROUP}            (excluir={DELETE_GROUP})")
print(f"Warehouse: {WAREHOUSE_NAME}   (excluir={DELETE_WAREHOUSE})")
print(f"Cluster:   {CLUSTER_NAME}     (excluir={DELETE_CLUSTER})")
print(f"Volume:    {VOLUME_FULL_NAME} (excluir={DELETE_VOLUME})")
print(f"Catálogo:  {CATALOG}          (REMOVER={DELETE_CATALOG})  {'⚠️ DESTRUTIVO' if DELETE_CATALOG else ''}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Desmontagem (idempotente)

# COMMAND ----------

print("=" * 70)
print("DESMONTAGEM")
print("=" * 70)

# --- Cluster ---------------------------------------------------------------
if DELETE_CLUSTER:
    _cl = next((c for c in w.clusters.list() if c.cluster_name == CLUSTER_NAME), None)
    if _cl:
        try:
            w.clusters.permanent_delete(cluster_id=_cl.cluster_id)
            print(f"{OK} Cluster '{CLUSTER_NAME}' excluído.")
        except Exception as e:
            print(f"{NO} Não foi possível excluir o cluster '{CLUSTER_NAME}': {e}")
    else:
        print(f"{OK} Cluster '{CLUSTER_NAME}' já ausente.")
else:
    print(f"{NA} Cluster '{CLUSTER_NAME}' mantido (excluir=false).")

# --- Warehouse -----------------------------------------------------------
if DELETE_WAREHOUSE:
    _wh = next((x for x in w.warehouses.list() if x.name == WAREHOUSE_NAME), None)
    if _wh:
        try:
            w.warehouses.delete(id=_wh.id)
            print(f"{OK} Warehouse '{WAREHOUSE_NAME}' excluído.")
        except Exception as e:
            print(f"{NO} Não foi possível excluir o warehouse '{WAREHOUSE_NAME}': {e}")
    else:
        print(f"{OK} Warehouse '{WAREHOUSE_NAME}' já ausente.")
else:
    print(f"{NA} Warehouse '{WAREHOUSE_NAME}' mantido (excluir=false).")

# --- Volume (faq_volume + PDF FAQ) -----
if DELETE_VOLUME:
    try:
        spark.sql(f"DROP VOLUME IF EXISTS {VOLUME_FULL_NAME}")
        print(f"{OK} Volume '{VOLUME_FULL_NAME}' removido (seus arquivos, incl. o PDF FAQ, foram removidos).")
    except Exception as e:
        print(f"{NO} Não foi possível remover o volume '{VOLUME_FULL_NAME}': {e}")
else:
    print(f"{NA} Volume '{VOLUME_FULL_NAME}' mantido (excluir=false).")

# --- Grupo do workshop (revogar concessões, desassociar, excluir) ----
if DELETE_GROUP:
    # Melhor esforço para revogar enquanto o grupo ainda existe (omitido se o recurso foi removido).
    for _sql, _label in [
        (f"REVOKE USE CATALOG, CREATE SCHEMA ON CATALOG {CATALOG} FROM `{GROUP}`", "catálogo"),
        (f"REVOKE USE SCHEMA ON SCHEMA {CATALOG}.{VOLUME_SCHEMA} FROM `{GROUP}`", "schema"),
        (f"REVOKE READ VOLUME ON VOLUME {VOLUME_FULL_NAME} FROM `{GROUP}`", "volume"),
    ]:
        try:
            spark.sql(_sql)
            print(f"{OK} Concessões de {_label} revogadas de {GROUP}.")
        except Exception:
            print(f"{NA} Revogação de {_label} omitida (recurso ou concessão já removido).")

    _found = _acct_scim("GET", "/Groups", query={"filter": f'displayName eq "{GROUP}"'}).get("Resources") or []
    if _found:
        _gid = _found[0]["id"]
        try:
            w.api_client.do("DELETE", f"/api/2.0/preview/permissionassignments/principals/{_gid}")
        except Exception:
            pass  # a atribuição pode já ter sido removida
        try:
            _acct_scim("DELETE", f"/Groups/{_gid}")
            print(f"{OK} Grupo de conta '{GROUP}' (id {_gid}) excluído. Suas concessões/associações também foram removidas.")
        except Exception as e:
            print(f"{NO} Não foi possível excluir o grupo de conta '{GROUP}': {e}")
    else:
        print(f"{OK} Grupo de conta '{GROUP}' já ausente.")

    for _g in w.groups.list(filter=f'displayName eq "{GROUP}"'):
        _meta = w.groups.get(_g.id).meta
        if _meta and _meta.resource_type == "WorkspaceGroup":
            w.groups.delete(_g.id)
            print(f"  removido grupo obsoleto local de workspace '{GROUP}' (id {_g.id}).")
else:
    print(f"{NA} Grupo '{GROUP}' mantido (excluir=false). Suas concessões permanecerão.")

# --- Catálogo (DESTRUTIVO, ativação manual) --------------------------------
if DELETE_CATALOG:
    try:
        spark.sql(f"DROP CATALOG IF EXISTS {CATALOG} CASCADE")
        print(f"{OK} Catálogo '{CATALOG}' removido (CASCADE: todos os schemas/dados/volumes removidos).")
    except Exception as e:
        print(f"{NO} Não foi possível remover o catálogo '{CATALOG}': {e}")
else:
    print(f"{NA} Catálogo '{CATALOG}' mantido (REMOVER=false). Schemas/dados dos participantes preservados.")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Relatório final
# MAGIC ✅ = revertido (recurso agora ausente) · ➖ = mantido por escolha · ❌ = ainda presente · ⚠️ = desconhecido.

# COMMAND ----------

import pandas as pd

def _account_group_exists(group):
    try:
        return len(_acct_scim("GET", "/Groups", query={"filter": f'displayName eq "{group}"'}).get("Resources") or []) > 0
    except Exception:
        return None

def _volume_exists(full_name):
    try:
        w.volumes.read(full_name); return True
    except Exception:
        return False

def _row(label, requested, still_present):
    if not requested:
        return {"Item": label, "Status": NA, "Note": "mantido (excluir=false)"}
    if still_present is None:
        return {"Item": label, "Status": ERR, "Note": "não foi possível verificar"}
    return {"Item": label, "Status": OK if not still_present else NO,
            "Note": "removido" if not still_present else "AINDA PRESENTE"}

try:
    w.catalogs.get(CATALOG); _catalog_present = True
except Exception:
    _catalog_present = False

report = [
    _row(f"Cluster '{CLUSTER_NAME}'",     DELETE_CLUSTER,   any(c.cluster_name == CLUSTER_NAME for c in w.clusters.list())),
    _row(f"Warehouse '{WAREHOUSE_NAME}'", DELETE_WAREHOUSE, any(x.name == WAREHOUSE_NAME for x in w.warehouses.list())),
    _row(f"Volume '{VOLUME_FULL_NAME}'",  DELETE_VOLUME,    _volume_exists(VOLUME_FULL_NAME) if _catalog_present else False),
    _row(f"Grupo '{GROUP}'",              DELETE_GROUP,     _account_group_exists(GROUP)),
    _row(f"Catálogo '{CATALOG}'",         DELETE_CATALOG,   _catalog_present),
]

_done = all(r["Status"] in (OK, NA) for r in report)
print("GERAL:", "✅ Desmontagem concluída: tudo o que foi solicitado foi revertido."
      if _done else "❌ Alguns itens ainda estão presentes: veja abaixo.")
display(pd.DataFrame(report, columns=["Item", "Status", "Note"]))
