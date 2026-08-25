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

O administrador executa **`workshop_prep_checker`** (idempotente, requer admin de conta) para
provisionar e validar tudo antes do treinamento: grupo `dbacademy_workshop` com os participantes
e direitos de acesso, catálogo `dbacademy`, SQL Warehouse, cluster multiuso, volume
`dbacademy.default.faq_volume` com o PDF FAQ, e as concessões. Exibe uma matriz por participante e
um Relatório final (✅ / ❌ / ⚠️ / ➖).

**Uso:** rode as **duas primeiras células** para exibir os widgets, selecione os participantes e
os alternadores, e use Run all. Para limpar ao fim, rode **`workshop_teardown`** (o `DROP CATALOG`
vem desativado por padrão).

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
