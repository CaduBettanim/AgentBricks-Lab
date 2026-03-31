# Lab 5 — Criação do Supervisor (Agent Bricks)

Este laboratório guia a criação de um **Agent Bricks: Supervisor Agent** que orquestra **vários subagentes**: os **dois Genie Spaces** do [Lab 4](../Lab%204%20-%20Criação%20de%20Salas%20Genie/) e o **Knowledge Assistant** do [Lab 1](../Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md).

Documentação oficial: [Supervisor Agent — multi-agent system](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/multi-agent-supervisor).

---

## Objetivo

- Criar um **supervisor** na UI **Agents** que delega perguntas aos especialistas certos:
  - **Genie (logística / inventário)** — dados estruturados ligados à **Metric View** `dbacademy.<seu_database>.mvw_inventory` (conforme [Lab 4](../Lab%204%20-%20Criação%20de%20Salas%20Genie/03_1_genie_spaces.ipynb)).
  - **Genie (vendas)** — dados estruturados ligados à **Metric View** `dbacademy.<seu_database>.mvw_sales`.
  - **Knowledge Assistant** — documentos do volume **`faq_volume`** (`dbacademy.<schema_do_volume>.faq_volume`), criado no [Lab 1](../Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md).
- Deixar o supervisor pronto para uso no [Lab 6](../Lab%206%20-%20Criação%20do%20App/) (app) ou em testes no Playground.

> **`<seu_database>`** e **`<schema_do_volume>`** seguem as convenções do [README principal](../README.md#catálogo-e-database-schema-pessoal): substitua pelos valores do seu ambiente de treinamento. Na documentação pedagógica usamos sempre o catálogo **`dbacademy`**.

---

## Antes de começar (dependências dos Labs 1 e 4)

| Pré-requisito | Onde foi feito |
|---------------|----------------|
| **Dois Genie Spaces** (logística/inventário e vendas) em **`dbacademy.<seu_database>`** | [Lab 4 — `03_1_genie_spaces.ipynb`](../Lab%204%20-%20Criação%20de%20Salas%20Genie/03_1_genie_spaces.ipynb). Opcionalmente [`03_2_genie_tools.ipynb`](../Lab%204%20-%20Criação%20de%20Salas%20Genie/03_2_genie_tools.ipynb). |
| **Knowledge Assistant** (endpoint) | [Lab 1 — README](../Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md) (**inicie o Lab 1 no começo do treinamento** — a criação demora). |
| Permissões | Quem for **usar** o supervisor precisa de acesso aos **dois espaços Genie** (e aos dados UC por trás deles) e permissão **Can Query** no endpoint do Knowledge Assistant. Quem criou cada recurso deve compartilhar conforme a [documentação de compartilhamento de Genie](https://docs.databricks.com/aws/en/genie/set-up#share-a-genie-space) e as permissões do Agent Bricks. |

Anote os **nomes** dos dois Genie Spaces e o **nome do Knowledge Assistant** (ou endpoint) para selecioná-los nos passos abaixo.

---

## Passo a passo na interface

### 1. Abrir **Agents** e iniciar o Supervisor

1. No workspace Databricks, abra **Agents** (menu lateral; em alguns layouts: **Mosaic AI** → **Agents**).
2. Localize o tile **Supervisor Agent** (Agent Bricks: Supervisor Agent).
3. Clique em **Build** (ou equivalente).

### 2. Preencher nome e descrição do supervisor

| Campo | Sugestão (PT-BR) — ajuste ao seu caso |
|-------|--------------------------------------|
| **Name** | `Supervisor — Lojas (Genie + FAQ)` |
| **Description** | `Orquestra dois assistentes Genie (inventário/logística e vendas) sobre dados em dbacademy.<seu_database> e um Knowledge Assistant sobre documentos do volume faq_volume em dbacademy. Encaminha cada pergunta ao subagente adequado e consolida respostas quando necessário.` |

*(Substitua `<seu_database>` na descrição pelo valor real se quiser texto fixo na UI.)*

### 3. Configurar os subagentes (**Configure Agents**)

Em **Configure Agents**, você deve incluir **três** entradas (use **+ Add** entre elas, até o limite de 20 do produto):

#### 3.1 Primeiro Genie Space — logística / inventário

1. Em **Type**, selecione **Genie Space**.
2. No menu do espaço Genie, escolha o espaço criado no **Lab 4** para **inventário / logística** (metric view **`mvw_inventory`** em `dbacademy.<seu_database>`).
3. Revise **Agent name** e **Describe the content** (a UI pode preencher automaticamente). Ajuste para o supervisor delegar bem, por exemplo em **Describe the content**:

   > *Especialista em estoque e inventário de lojas. Use para perguntas sobre níveis de estoque, produtos, lojas e métricas de inventário a partir da base configurada no Genie (dados em dbacademy.<seu_database>, visão mvw_inventory).*

#### 3.2 Segundo Genie Space — vendas

1. Clique em **+ Add**.
2. **Type:** **Genie Space**.
3. Selecione o espaço Genie de **vendas** do **Lab 4** (metric view **`mvw_sales`** em `dbacademy.<seu_database>`).
4. Refine **Describe the content**, por exemplo:

   > *Especialista em vendas e desempenho comercial. Use para perguntas sobre quantidade vendida, faturamento, ticket médio e rankings de produtos ou lojas (dados em dbacademy.<seu_database>, visão mvw_sales).*

#### 3.3 Knowledge Assistant (Lab 1)

1. Clique em **+ Add**.
2. **Type:** **Agent endpoint** (no fluxo do Supervisor, o Knowledge Assistant criado no Agent Bricks aparece como endpoint de agente).
3. Selecione o **endpoint do Knowledge Assistant** criado no [Lab 1](../Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md) (volume **`faq_volume`** / `dbacademy.<schema_do_volume>.faq_volume`).
4. Ajuste **Agent name** e **Describe the content** se necessário, por exemplo:

   > *Especialista em documentos e políticas em linguagem natural (FAQ, manuais). Use para perguntas que dependem de texto nos arquivos do volume faq_volume, não para consultas SQL agregadas nas metric views dos Genies.*

> **Referência de produto:** apenas endpoints de Knowledge Assistant criados via [Agent Bricks: Knowledge Assistant](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant) são suportados como subagente nesse fluxo, conforme a documentação do Supervisor.

### 4. Instruções do supervisor (recomendado)

No campo **Instructions**, defina como o supervisor deve escolher o subagente. Exemplo:

> *Analise a pergunta do usuário. Se envolver números de estoque, inventário, disponibilidade por loja ou produto, delegue ao Genie de inventário. Se envolver vendas, faturamento, quantidades vendidas ou rankings de venda, delegue ao Genie de vendas. Se envolver políticas, procedimentos ou conteúdo de documentos/FAQ, delegue ao Knowledge Assistant. Se a pergunta cruzar domínios, pode consultar mais de um subagente e sintetize uma resposta coerente em português do Brasil. Se nenhum subagente for adequado, diga claramente que não foi possível rotear a pergunta.*

### 5. Criar e aguardar

1. Clique em **Create Agent**.
2. A criação do sistema multiagente pode levar **vários minutos** (ou mais, conforme o workspace). Acompanhe o status na interface até ficar pronto.

### 6. Testar

1. Use **Test your Agent** no painel lateral ou **Open in Playground**.
2. Faça perguntas que claramente pertencem a **cada** subagente (inventário, vendas, FAQ) e uma **misturada** para validar o roteamento.
3. Ajuste **Description** e **Instructions** e use **Update Agent** se o supervisor delegar mal.

### 7. Permissões e próximos passos

- Conceda **Can Query** (ou **Can Manage**) a quem for testar o supervisor, além de garantir acesso aos **dois Genies** e ao **endpoint** do Knowledge Assistant.
- Anote o identificador / **See Agent status** para o [Lab 6](../Lab%206%20-%20Criação%20do%20App/).

---

## Checklist rápido

- [ ] Lab 4 concluído: dois Genie Spaces (inventário → `mvw_inventory`, vendas → `mvw_sales`) em `dbacademy.<seu_database>`.
- [ ] Lab 1 concluído: Knowledge Assistant com fonte no volume **`faq_volume`** (`dbacademy.<schema_do_volume>.faq_volume`).
- [ ] Agents → **Supervisor Agent** → **Build**.
- [ ] Nome e descrição do supervisor preenchidos.
- [ ] Subagente 1: **Genie Space** (logística/inventário).
- [ ] Subagente 2: **Genie Space** (vendas).
- [ ] Subagente 3: **Agent endpoint** → Knowledge Assistant do Lab 1.
- [ ] Descrições de cada subagente ajudam o roteamento; **Instructions** do supervisor definidas.
- [ ] **Create Agent** → testes → permissões para Lab 6 / equipe.

---

## Referências

- [Supervisor Agent — Databricks Docs](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/multi-agent-supervisor)
- [Knowledge Assistant](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant)
- [Genie — configurar e compartilhar espaço](https://docs.databricks.com/aws/en/genie/set-up)
- [Agent Bricks — visão geral](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)

---

*Roteiro alinhado à documentação Databricks (março/2026). Menus podem variar por cloud e versão do workspace.*
