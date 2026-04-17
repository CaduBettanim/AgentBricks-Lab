# Lab 1 — Criação do Knowledge Assistant (Agent Bricks)

Este laboratório guia a criação de um **Agent Bricks: Knowledge Assistant** na interface do Databricks, usando documentos em um **Unity Catalog volume** como fonte de conhecimento.


Documentação oficial do produto: [Use Agent Bricks: Knowledge Assistant](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant).

---

## Objetivo

- Criar um assistente de conhecimento que responde perguntas sobre os documentos do volume.

---

## Passo a passo na interface

### 1. Abrir **Agents**

1. No workspace Databricks, abra o menu lateral.
2. Do lado esquerdo encontre e acesse **Agents**.
3. Clique em **Create Agent**.
4. Localize e clique no bloco **Knowledge Assistant**.

Você será levado ao fluxo de configuração do Knowledge Assistant

### 2. Configurar o agente

#### 2.1 Nome e descrição do agente

| Campo | Sugestão (PT-BR) — ajuste ao seu caso |
|-------|--------------------------------------|
| **Name** | `FAQ_Lojas_<seu_nome>` |
| **Description** | `Assistente que responde perguntas com base em documentos de FAQ.` |

#### 2.2 Fonte de conhecimento — arquivos no UC (volume)

1. No painel **Configure Knowledge source**, adicione uma fonte.
2. Em **Type**, selecione **Files in Volume** (Arquivos em Volume).
3. Em **Source**, clique na caixa de seleção e no campo de busca digite dbacademy e selecione o faq_volume.
4. Em **Name** inclua o nome FAQ <seu_nome>
5. Clique em **Confirm**
6. Em **Describe the content**, descreva o conteúdo para o modelo saber quando usar esta fonte. Exemplo:

   > *Documentos de perguntas frequentes e orientações operacionais para equipes de loja: políticas, procedimentos e respostas padronizadas.*

7. Clique em **Create Agent**.

#### 2.3 Instruções do agente

1. Dentro do agente, clique em **Settings**
2. No campo **Instructions**, defina o comportamento:

> *Responda em português do Brasil. Seja claro e objetivo. Sempre que possível, indique de qual documento ou seção a informação foi retirada. Se a pergunta não puder ser respondida com base nos documentos fornecidos, diga que a base de conhecimento não contém essa informação e não invente fatos.*

2. Clique em **Save and Update**

---

## Referências

- [Knowledge Assistant — Databricks Docs](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant)
- [Agent Bricks](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)
- [Volumes no Unity Catalog](https://docs.databricks.com/aws/en/volumes/)
