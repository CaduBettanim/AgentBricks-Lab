# Lab 1 — Criação do Knowledge Assistant (Agent Bricks)

Este laboratório guia a criação de um **Agent Bricks: Knowledge Assistant** na interface do Databricks, usando documentos em um **Unity Catalog volume** como fonte de conhecimento.


Documentação oficial do produto: [Use Agent Bricks: Knowledge Assistant](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant).

---

## Objetivo

- Criar um assistente de conhecimento que responde perguntas sobre os documentos do volume, com **citações** às fontes.

---

## Passo a passo na interface

### 1. Abrir **Agents**

1. No workspace Databricks, abra o menu lateral (**☰** ou navegação principal).
2. Do lado esquerdo encontre e acesse **Agents**.
3. Localize o bloco **Knowledge Assistant** (Agent Bricks: Knowledge Assistant).

### 2. Iniciar a construção

1. No tile **Knowledge Assistant**, clique em **Build**.
2. Você será levado ao fluxo de configuração na aba **Build**.

### 3. Configurar o agente (aba Build)

#### 3.1 Nome e descrição do agente

Preencha campos que identificam o assistente para você e para quem for usar depois.

| Campo | Sugestão (PT-BR) — ajuste ao seu caso |
|-------|--------------------------------------|
| **Name** | `FAQ_Lojas_<seu_nome>` |
| **Description** | `Assistente que responde perguntas com base em documentos de FAQ.` |

#### 3.2 Fonte de conhecimento — arquivos no UC (volume)

1. No painel **Configure Knowledge source**, adicione uma fonte.
2. Em **Type**, selecione **UC Files** (arquivos no Unity Catalog).
3. Em **Source**, clique na caixa de seleção e no campo de busca digite dbacademy e selecione o faq_volume. Clique em Confirm:
4. Em **Name** (nome da fonte), use algo identificável, por exemplo: `FAQ volume — documentos loja`.
5. Em **Describe the content**, descreva o conteúdo para o modelo saber **quando** usar esta fonte. Exemplo:

   > *Documentos de perguntas frequentes e orientações operacionais para equipes de loja: políticas, procedimentos e respostas padronizadas. Use esta fonte para dúvidas sobre regras, processos e conteúdo explícito nos arquivos do volume faq_volume.*

6. Clique em **Create Agent**.

#### 3.3 Instruções do agente (opcional e recomendado)

1. Dentro do agente, clique em **Settings**
2. No campo **Instructions**, defina o comportamento. Exemplo:

> *Responda em português do Brasil. Seja claro e objetivo. Sempre que possível, indique de qual documento ou seção a informação foi retirada. Se a pergunta não puder ser respondida com base nos documentos fornecidos, diga que a base de conhecimento não contém essa informação e não invente fatos.*

### 4. Criar o agente

1. Clique em **Create Agent** (ou **Create**).
2. A criação e a **sincronização** dos arquivos do volume podem levar **vários minutos** (em bases grandes, até horas). Acompanhe o painel até as fontes aparecerem como sincronizadas.
3. Se você **adicionar ou alterar arquivos** no volume depois, use **Sync** no assistente para atualizar a base (apenas o criador do Knowledge Assistant costuma poder sincronizar, conforme a doc).

Neste treinamento, **não é necessário testar o assistente no chat neste laboratório** — a validação conversacional fica para **depois** (outro momento do curso ou integração no fluxo do Supervisor).

---

## Checklist rápido

- [ ] Volume `dbacademy.<schema_do_volume>.faq_volume` existe e contém arquivos nos formatos aceitos.
- [ ] Agents → Knowledge Assistant → **Build**.
- [ ] Nome e descrição do agente preenchidos.
- [ ] Fonte **UC Files** apontando para o volume correto.
- [ ] Nome e **Describe the content** da fonte preenchidos com contexto de negócio.
- [ ] **Instructions** (recomendado) com tom, idioma e regras anti-alucinação.
- [ ] **Create Agent** e aguardar sincronização.
- [ ] Identificador do agente anotado para o Supervisor (quando disponível na UI).

---

## Referências

- [Knowledge Assistant — Databricks Docs](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant)
- [Agent Bricks](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)
- [Volumes no Unity Catalog](https://docs.databricks.com/aws/en/volumes/)

---

*Última revisão do roteiro conforme documentação Databricks (março/2026). Nomes de menus podem variar levemente por cloud e versão do workspace.*
