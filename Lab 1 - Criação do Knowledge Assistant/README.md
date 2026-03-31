# Lab 1 — Criação do Knowledge Assistant (Agent Bricks)

Este laboratório guia a criação de um **Agent Bricks: Knowledge Assistant** na interface do Databricks, usando documentos em um **Unity Catalog volume** como fonte de conhecimento.

> **Comece por aqui.** A criação e a sincronização do Knowledge Assistant podem levar **muito tempo**. Dispare este laboratório **primeiro** e, enquanto o agente processa, siga os [Labs 2](../Lab%202%20-%20Geração%20de%20Dados/) (dados), [Lab 3](../Lab%203%20-%20Criação%20de%20Funções/) (funções) e [Lab 4](../Lab%204%20-%20Criação%20de%20Salas%20Genie/) (Genie). No [Lab 5](../Lab%205%20-%20Criação%20do%20Supervisor/README.md), você precisará do endpoint deste assistente **já criado** e dos dois Genie Spaces do Lab 4.

**Referência nos materiais (alunos):** catálogo **`dbacademy`**, volume **`faq_volume`**, caminho lógico:

`dbacademy.<schema_do_volume>.faq_volume`

Substitua **`<schema_do_volume>`** pelo schema que o instrutor indicar no ambiente de treinamento (o volume `faq_volume` deve existir e conter arquivos suportados).

> **Nota para o instrutor:** no ambiente de demonstração, o volume pode estar em outro catálogo (ex.: `serverless_stable_bettanim_catalog.<schema>.faq_volume`). **Na documentação deste repositório mantemos sempre `dbacademy` e `faq_volume`** para padronizar o material dos participantes.

Documentação oficial do produto: [Use Agent Bricks: Knowledge Assistant](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant).

---

## Objetivo

- Criar um assistente de conhecimento que responde perguntas sobre os documentos do volume, com **citações** às fontes.
- Deixar o agente pronto para ser referenciado no **Lab 5 (Supervisor)**.

---

## Passo a passo na interface

### 1. Abrir **Agents**

1. No workspace Databricks, abra o menu lateral (**☰** ou navegação principal).
2. Acesse **Agents** (ou **Mosaic AI** → **Agents**, conforme o layout da sua região/versão).
3. Localize o bloco **Knowledge Assistant** (Agent Bricks: Knowledge Assistant).

### 2. Iniciar a construção

1. No tile **Knowledge Assistant**, clique em **Build** (ou equivalente, ex.: **Criar** / **Get started**).
2. Você será levado ao fluxo de configuração na aba **Build**.

### 3. Configurar o agente (aba Build)

#### 3.1 Nome e descrição do agente

Preencha campos que identificam o assistente para você e para quem for usar depois.

| Campo | Sugestão (PT-BR) — ajuste ao seu caso |
|-------|--------------------------------------|
| **Name** | `FAQ Lojas — Knowledge Assistant` |
| **Description** | `Assistente que responde perguntas com base em documentos de FAQ e políticas armazenados no volume Unity Catalog dbacademy, com respostas citando as fontes.` |

#### 3.2 Fonte de conhecimento — arquivos no UC (volume)

1. No painel **Knowledge source**, adicione uma fonte.
2. Em **Type**, selecione **UC Files** (arquivos no Unity Catalog).
3. Em **Source**, selecione o **volume** (ou **pasta dentro do volume**) onde estão os documentos:
   - **Referência pedagógica:** `dbacademy.<schema_do_volume>.faq_volume`
   - No seletor da UI, navegue: catálogo **`dbacademy`** → schema indicado → volume **`faq_volume`**.
4. Em **Name** (nome da fonte), use algo identificável, por exemplo: `FAQ volume — documentos loja`.
5. Em **Describe the content**, descreva o conteúdo para o modelo saber **quando** usar esta fonte. Exemplo:

   > *Documentos de perguntas frequentes e orientações operacionais para equipes de loja: políticas, procedimentos e respostas padronizadas. Use esta fonte para dúvidas sobre regras, processos e conteúdo explícito nos arquivos do volume faq_volume.*

6. *(Opcional)* **Add knowledge source** — até **10** fontes no total (outro volume, outro diretório, etc.).

#### 3.3 Instruções do agente (opcional e recomendado)

No campo **Instructions**, defina o comportamento. Exemplo:

> *Responda em português do Brasil. Seja claro e objetivo. Sempre que possível, indique de qual documento ou seção a informação foi retirada. Se a pergunta não puder ser respondida com base nos documentos fornecidos, diga que a base de conhecimento não contém essa informação e não invente fatos.*

> **Atenção:** a documentação do produto menciona limitações de idioma em partes da experiência; se o workspace exibir avisos ou comportamento distinto para PT-BR, siga as orientações na UI ou do instrutor.

### 4. Criar o agente

1. Clique em **Create Agent** (ou **Create**).
2. A criação e a **sincronização** dos arquivos do volume podem levar **vários minutos** (em bases grandes, até horas). Acompanhe o painel até as fontes aparecerem como sincronizadas.
3. Se você **adicionar ou alterar arquivos** no volume depois, use **Sync** no assistente para atualizar a base (apenas o criador do Knowledge Assistant costuma poder sincronizar, conforme a doc).

Neste treinamento, **não é necessário testar o assistente no chat neste laboratório** — a validação conversacional fica para **depois** (outro momento do curso ou integração no fluxo do Supervisor).

### 5. Permissões e uso downstream

- Por padrão, acesso restrito a autores/admins; conceda **Can Query** ou **Can Manage** conforme necessário para o Lab 5 e para colegas testarem.
- Anote o **nome/identificador** do agente e, se precisar para integrações, consulte **See Agent status** (endpoint, detalhes).

---

## Checklist rápido

- [ ] Volume `dbacademy.<schema_do_volume>.faq_volume` existe e contém arquivos nos formatos aceitos.
- [ ] Agents → Knowledge Assistant → **Build**.
- [ ] Nome e descrição do agente preenchidos.
- [ ] Fonte **UC Files** apontando para o volume correto.
- [ ] Nome e **Describe the content** da fonte preenchidos com contexto de negócio.
- [ ] **Instructions** (recomendado) com tom, idioma e regras anti-alucinação.
- [ ] **Create Agent** e aguardar sincronização.
- [ ] Permissões ajustadas para quem for usar no Lab 5.
- [ ] Identificador do agente anotado para o Supervisor.

---

## Referências

- [Knowledge Assistant — Databricks Docs](https://docs.databricks.com/aws/en/generative-ai/ai-builder/knowledge-assistant)
- [Agent Bricks](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)
- [Volumes no Unity Catalog](https://docs.databricks.com/aws/en/volumes/)

---

*Última revisão do roteiro conforme documentação Databricks (março/2026). Nomes de menus podem variar levemente por cloud e versão do workspace.*
