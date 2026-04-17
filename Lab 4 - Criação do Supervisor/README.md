# Lab 4 — Criação do Supervisor (Agent Bricks)

Este laboratório guia a criação de um **Agent Bricks: Supervisor Agent** que orquestra **vários subagentes**: os **dois Genie Spaces** e o **Knowledge Assistant**.

Documentação oficial: [Supervisor Agent — multi-agent system](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/multi-agent-supervisor).

---

## Objetivo

- Criar um **supervisor** na UI **Agents** que delega perguntas aos especialistas certos:
  - **Genie (Logística)**.
  - **Genie (Vendas)**.
  - **Knowledge Assistant**.

---

## Passo a passo na interface

1. No workspace Databricks, abra **Agents** (menu lateral).
2. Selecione **Create Agent**
3. Selecione o tile **Supervisor Agent**.

### 2. Preencher nome e descrição do supervisor

| Campo | Informação |
|-------|--------------------------------------|
| **Name** | `Supervisor_Lojas_<seu_database>` |
| **Description** | `Orquestra dois assistentes Genie (Logistica e Vendas) e um Knowledge Assistant sobre documentos FAQ. Encaminha cada pergunta ao subagente adequado e consolida respostas quando necessário.` |

### 3. Configurar os subagentes (**Configure Agents**)

Em **Configure Agents**, você deve incluir **três** entradas (use **+ Add** entre elas):

#### 3.1 Primeiro Genie Space - Vendas

1. Em **Type**, selecione **Genie Space**.
2. No menu do espaço Genie, escolha a sua Genie de Vendas.
3. Mantenha o **Agent name** como está.
4. Em **Describe the content** Ajuste para o supervisor delegar bem as perguntas pertinentes a este agente:

```text
Especialista em vendas. Use para perguntas sobre quantidade vendida, faturamento, ticket médio e rankings de produtos ou lojas.
```
#### 3.2 Segundo Genie Space — Logistica

1. Clique em **+ Add**.
2. Em **Type**, selecione **Genie Space**.
3. No menu do espaço Genie, escolha a sua Genie de Logística.
4. Mantenha o **Agent name** como está.
5. Em **Describe the content** Ajuste para o supervisor delegar bem as perguntas pertinentes a este agente:

```text
Especialista em estoque e inventário de lojas. Use para perguntas sobre níveis de estoque, produtos, lojas e métricas de inventário.
```

#### 3.3 Knowledge Assistant

**Colete seu Endpoint**

1. No workspace Databricks, clique com o botão direito em **Agents** (menu lateral).
2. Selecione para abrir em uma nova aba.
3. Encontre e selecione seu Knowledge Assistant que foi criado no laboratório 1 (na busca digite `FAQ_Lojas_<seu_database>`)
4. Clique no botão superior direito chamado **Endpoint**.
5. Copie o nome do seu endpoint.
   
**De volta na aba de criação do Supervisor**
1. Clique em **+ Add**.
2. **Type:** **Agent endpoint**.
3. Em **Agent Endpoint** cole o nome do endpoint do seu Knowledge Assistant.
4. Mantenha o **Agent name** como está.
5. Em **Describe the content** Ajuste para o supervisor delegar bem as perguntas pertinentes a este agente:

```text
Especialista em documentos e políticas em linguagem natural (FAQ, manuais). Use para perguntas que dependem de texto nos arquivos do volume faq_volume.
```

### 4. Optional

No campo **Instructions**, defina como o supervisor deve escolher o subagente. Exemplo:

```text
Analise a pergunta do usuário. Se envolver números de estoque, inventário, disponibilidade por loja ou produto, delegue ao Genie de inventário. Se envolver vendas, faturamento, quantidades vendidas ou rankings de venda, delegue ao Genie de vendas. Se envolver políticas, procedimentos ou conteúdo de documentos/FAQ, delegue ao Knowledge Assistant. Se a pergunta cruzar domínios, pode consultar mais de um subagente e sintetize uma resposta coerente em português do Brasil. Se nenhum subagente for adequado, diga claramente que não foi possível rotear a pergunta.
```

### 5. Criar e aguardar

1. Clique em **Create Agent**.

### 6. Testar

1. Clique em **Open in Playground**.
2. Caso peça permissões de acesso aos agentes, conceda as permissões.
3. Faça perguntas que claramente pertencem a **cada** subagente (inventário, vendas, FAQ).

```text
Qual o estoque atual de cada produto?
```

```text
Qual o total de vendas de Carregador Rápido com Microfone?
```

```text
As entregas são feitas para todo o Brasil?
```

```text
Quais são os horários das lojas físicas?
```

---

## Referências

- [Supervisor Agent — Databricks Docs](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/multi-agent-supervisor)
- [Knowledge Assistant](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant)
- [Genie — configurar e compartilhar espaço](https://docs.databricks.com/aws/en/genie/set-up)
- [Agent Bricks — visão geral](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)
