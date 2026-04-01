# Lab 5 — Criação do Supervisor (Agent Bricks)

Este laboratório guia a criação de um **Agent Bricks: Supervisor Agent** que orquestra **vários subagentes**: os **dois Genie Spaces** e o **Knowledge Assistant**.

Documentação oficial: [Supervisor Agent — multi-agent system](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/multi-agent-supervisor).

---

## Objetivo

- Criar um **supervisor** na UI **Agents** que delega perguntas aos especialistas certos:
  - **Genie (logística / inventário)**.
  - **Genie (vendas)**.
  - **Knowledge Assistant**.

---

## Passo a passo na interface

1. No workspace Databricks, abra **Agents** (menu lateral).
2. Localize o tile **Supervisor Agent**.
3. Clique em **Build**.

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
