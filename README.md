# Databricks — Criação de Agentes com AgentBricks

![Faixa do treinamento — Databricks Criação de Agentes com AgentBricks](./assets/banner.png)

## Público-alvo

Usuários Databricks que desejam utilizar a plataforma para **construção de agentes de IA**, integrando dados governados (Unity Catalog), análise conversacional (Genie), Knowledge Assistant e solução multi-agent no Databricks.

---

## Seu database (identificador pessoal)

Cada participante utiliza um **database** próprio. No **Unity Catalog**, isso corresponde ao **nome do schema** dentro do catálogo **`dbacademy`**.

| Regra | Exemplo |
|-------|---------|
| **Primeira letra do nome** + **sobrenome**, em **minúsculas**, sem espaços | Aluno **Carlos Bettanim** → database **`cbettanim`** |

**Anote esse valor** e use-o em todo o treinamento (notebooks, Genie, referências a tabelas e views).

---

## Requisitos para participar

| Requisito | Detalhes |
|-----------|----------|
| Acesso ao workspace | Cada participante recebe o **link do ambiente** (ex.: 1 dia antes do treinamento). Login, uso de notebooks e permissões são concedidos pelo notebook de preparação (grupo `dbacademy_workshop`). |
| Unity Catalog | Catálogo `dbacademy` e volume `dbacademy.default.faq_volume` (já com o PDF FAQ) criados pelo notebook de preparação. |

---

## Preparação do ambiente (instrutor/admin)

Este lab inclui dois notebooks auxiliares: **`workshop_prep_checker`** cuida da preparação
do ambiente e da checagem dos requisitos, e **`workshop_teardown`** remove os recursos
criados para o workshop.

O **`workshop_prep_checker`** é idempotente (seguro re-executar) e requer **admin de conta**.

**Passos:**

1. Abra o notebook e rode as **duas primeiras células** para exibir os widgets.
2. Selecione os **participantes** e ajuste os alternadores.
3. Clique em **Run all** — todas as células devem terminar com sucesso.
4. Confira o veredito na seção **5. Relatório final**. O esperado é
   `✅ CHECKS COMPLETOS`. Se houver ❌ ou ⚠️, corrija e re-execute o notebook inteiro.

Ele cria: grupo `dbacademy_workshop` (participantes + acessos), catálogo `dbacademy`,
volume `dbacademy.default.faq_volume` (com o PDF FAQ), SQL Warehouse, cluster multiuso
e as concessões.

Após o workshop, rode **`workshop_teardown`** para limpar (o `DROP CATALOG` vem desativado).

---

## Roteiro do treinamento

**Ordem recomendada:** comece pelo **Lab 1** (Knowledge Assistant demora a provisionar). O **Lab 2** (Geração de Dados) pode correr em paralelo. Para a trilha **AgentBricks** (Labs 3 → 4 → 5), os Labs anteriores são pre-requisitos.

### Laboratórios

**Lab 1 - Criação do Knowledge Assistant**

**Lab 2 - Geração de Dados**

**Lab 3 - Criação de Salas Genie**

**Lab 4 - Criação do Supervisor**

**Lab 5 - Criação do App**

A UI pode variar por região/versão; siga também as orientações do instrutor.

---

## Segurança

- **Não commite** Personal Access Tokens (PAT), senhas ou secrets.
