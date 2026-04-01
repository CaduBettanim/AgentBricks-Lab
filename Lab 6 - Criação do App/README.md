# Lab 6 — Criação do Supervisor via Genie Code

Este laboratório guia a criação de um novo App utilizando estratégia de Vibe Coding via Genie Code.

Documentação oficial: [Genie Code](https://www.databricks.com/blog/introducing-genie-code).

---

## Objetivo

- Criar um novo App para atuar como uma nova interface limpa e intuitiva, podendo compartilhar com toda a organização:

---

## Passo a passo na interface

1. No workspace Databricks, abra **o Genie Code** (Laterial direita superior - ícone semelhante a uma estrela roxa).
2. Digite a seguinte instrução (Não se esqueça de alterar o nome que será dado ao seu App)
```text
Crie um App chamado Agente_<seu_database> no Databricks Apps.
Este app deve considerar aspectos visuais e paleta de cores do site da empresa X (COLOQUE O SITE AQUI).
O app será para servir como interface do agente supervisor <ID DO SUPERVISOR>.
```
4. Clique em **Build**.

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
3. Encontre e selecione seu Knowledge Assistant que foi criado no laboratório 1.
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
