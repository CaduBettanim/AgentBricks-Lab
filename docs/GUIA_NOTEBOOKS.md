# Guia de execução dos laboratórios

Este guia acompanha os notebooks e o material em **ordem recomendada**.

**Database pessoal:** `dbacademy.<seu_database>` — primeira letra do nome + sobrenome em minúsculas (ex.: `cbettanim`). **Substitua `<seu_database>`** nos notebooks antes de executar. Detalhes no [README](../README.md#seu-database-identificador-pessoal).

## Ordem recomendada

1. **[Lab 1 — Knowledge Assistant](../Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md)** (só interface) — **inicie primeiro**; o provisionamento é lento.  
2. **Lab 2 — dados** — notebook `Lab 2 - Geração de Dados/01_generate_data.ipynb` (paralelo ou após disparar o Lab 1).  
3. **Lab 3 — funções** — `Lab 3 - Criação de Funções/02_create_function.ipynb`.  
4. **Lab 4 — Genie** — `Lab 4 - Criação de Salas Genie/` (`03_1` e `03_2`).  
5. **[Lab 5 — Supervisor](../Lab%205%20-%20Criação%20do%20Supervisor/README.md)** — exige **Lab 1** (endpoint pronto) + dois Genies do **Lab 4**.  
6. **Lab 6 — App** — pasta `Lab 6 - Criação do App/`.

---

## Lab 1 — Knowledge Assistant (somente README)

Não há notebook nesta pasta. Siga o [**README do Lab 1**](../Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md). **Dispare este passo antes** ou em paralelo ao início do Lab 2.

---

## Pré-requisitos antes dos notebooks (Labs 2–4)

1. Acesso ao workspace Databricks (link do instrutor).
2. Permissões no catálogo `dbacademy` e no seu schema `<seu_database>`.
3. Cluster ou **Serverless** com **DBR 16.4 LTS** (ou versão indicada nos notebooks).
4. Criar o schema, se necessário:

```sql
CREATE SCHEMA IF NOT EXISTS dbacademy.<seu_database>;
```

---

## Lab 2 — `Lab 2 - Geração de Dados/01_generate_data.ipynb` — Gerar dados

**Objetivo:** popular tabelas Delta e **Metric Views** (`mvw_inventory`, `mvw_sales`).

**Como executar**

1. Substitua **`<seu_database>`** no notebook.
2. Execute as células na ordem (Python de geração → validações `%sql` → `CREATE` das metric views).
3. Valide com `MEASURE(...)`.

**Observações:** IDs são aleatórios a cada execução; ajuste exemplos de `store_id` nos labs seguintes.

---

## Lab 3 — `Lab 3 - Criação de Funções/02_create_function.ipynb` — Funções no Unity Catalog

**Objetivo:** funções `get_store_by_id` e `geocode_address`.

**Como executar**

1. Substitua **`<seu_database>`**.
2. Dependência: tabelas do **Lab 2**.
3. Teste `get_store_by_id` com `store_id` real: `SELECT store_id FROM dbacademy.<seu_database>.dim_store LIMIT 5;`

---

## Lab 4 (1/2) — `Lab 4 - Criação de Salas Genie/03_1_genie_spaces.ipynb` — Genie Spaces

**Objetivo:** instruções para criar **dois** Genie Spaces (inventário / vendas) na UI.

**Como executar**

1. Use `dbacademy.<seu_database>.mvw_inventory` e `mvw_sales`.
2. Anote IDs dos espaços para o **Lab 5** e para `03_2_genie_tools.ipynb`.

---

## Lab 4 (2/2) — `Lab 4 - Criação de Salas Genie/03_2_genie_tools.ipynb` — Genie como ferramenta

**Objetivo:** `_genie_query` e `chat_with_sales`.

**Como executar**

1. Substitua **`<seu_database>`**, `host`, `token` e `genie_id` conforme o notebook.

---

## Labs 5 e 6 (interface)

- **Lab 5 — Supervisor:** [README](../Lab%205%20-%20Criação%20do%20Supervisor/README.md) — dois Genies (**Lab 4**) + Knowledge Assistant (**Lab 1**).
- **Lab 6 — App:** pasta `Lab 6 - Criação do App/` (conteúdo a definir).

Roteiro resumido no [README principal](../README.md#roteiro-do-treinamento).
