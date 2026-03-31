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

Nos notebooks, o placeholder **`<seu_database>`** deve ser substituído pelo seu identificador **antes de executar** qualquer célula: com os sinais `<` e `>`, o texto não é um nome válido no Unity Catalog. Depois da troca, use referências como **`dbacademy.cbettanim`** (exemplo). No Databricks, use *Edit → Find and Replace* no notebook para substituir `<seu_database>` de uma vez.

---

## Requisitos para participar

| Requisito | Detalhes |
|-----------|----------|
| Acesso ao workspace | Cada participante recebe o **link do ambiente** (ex.: 1 dia antes do treinamento). Conta com permissão de login e uso de notebooks. |
| Unity Catalog | Catálogo **`dbacademy`** — volume **`faq_volume`** ([Lab 1](./Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md)) e schema pessoal **`<seu_database>`** ([Labs 2–4](./docs/GUIA_NOTEBOOKS.md); para metric views dos Labs 3–6 use o [**Lab 2 Backup**](./Lab%202%20Backup%20-%20Geração%20de%20Dados/README.md)). Ajuste se o instrutor fornecer nomes diferentes. |
| Permissões | `USAGE` no catálogo; `CREATE` e `SELECT` no **seu** schema (`dbacademy.<seu_database>`); permissões para criar **Genie Spaces** e acessar **AgentBricks** conforme política da conta. |
| Runtime | **DBR 16.4 LTS** ou versão indicada pelo instrutor (anotada nos notebooks). |
| Navegador | Navegador atualizado para UI do Databricks, Genie e AgentBricks. |
| Rede | Para o notebook de funções: possível necessidade de **HTTPS de saída** para geocodificação (OpenStreetMap Nominatim). Redes restritas podem exigir exceção. |

**Pré-trabalho (opcional):** familiaridade básica com SQL e notebooks Python no Databricks.

---

## Estrutura do repositório

```
AgentBricks-Lab/
├── README.md
├── assets/
│   ├── banner.png
│   └── banner.svg
├── docs/
│   └── GUIA_NOTEBOOKS.md     ← ordem dos labs + notebooks
├── Lab 1 - Criação do Knowledge Assistant/
│   └── README.md             ← inicie por aqui (provisionamento lento)
├── Lab 2 - Geração de Dados/
│   ├── README.md
│   └── lab02_01_carga_csv.ipynb   ← carga CSV (estilo lab_sql)
├── Lab 2 Backup - Geração de Dados/
│   ├── README.md
│   └── 01_generate_data.ipynb     ← metric views p/ Labs 3–6
├── Lab 3 - Criação de Funções/
│   └── 02_create_function.ipynb
├── Lab 4 - Criação de Salas Genie/
│   ├── README.md             ← página de treinamento (conteúdo dos 2 notebooks)
│   ├── 03_1_genie_spaces.ipynb
│   └── 03_2_genie_tools.ipynb
├── Lab 5 - Criação do Supervisor/
│   └── README.md
└── Lab 6 - Criação do App/
```

---

## Roteiro do treinamento

**Ordem recomendada:** comece pelo **Lab 1** (Knowledge Assistant demora a provisionar). O **Lab 2** (CSV) pode correr em paralelo. Para a trilha **AgentBricks** (Labs 3 → 4 → 5), execute também o [**Lab 2 Backup**](./Lab%202%20Backup%20-%20Geração%20de%20Dados/README.md) (`01_generate_data.ipynb`). O **Lab 5** exige **Lab 1** concluído (endpoint) e **Lab 4** concluído (dois Genies). Detalhes no **[Guia dos laboratórios](./docs/GUIA_NOTEBOOKS.md)**.

### Laboratórios

**Lab 1 - Criação do Knowledge Assistant** — [**README**](./Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md): **Agents** → **Knowledge Assistant** → volume **`faq_volume`** em **`dbacademy.<schema_do_volume>.faq_volume`**. *Primeiro da fila por causa do tempo de criação/sincronização.*

**Lab 2 - Geração de Dados** — [**README**](./Lab%202%20-%20Geração%20de%20Dados/README.md) + [`lab02_01_carga_csv.ipynb`](./Lab%202%20-%20Geração%20de%20Dados/lab02_01_carga_csv.ipynb): importação de notebook, carga de **CSV** em tabelas Delta (conteúdo alinhado ao [LAB 02 — lab_sql](https://github.com/CaduBettanim/lab_sql/blob/main/02_LAB_Notebook/README.md)).

**Lab 2 Backup - Geração de Dados** — [**README**](./Lab%202%20Backup%20-%20Geração%20de%20Dados/README.md) + [`01_generate_data.ipynb`](./Lab%202%20Backup%20-%20Geração%20de%20Dados/01_generate_data.ipynb): dados sintéticos e **Metric Views** `mvw_inventory` / `mvw_sales` — **necessário** para Labs 3, 4, 5 e 6.

**Lab 3 - Criação de Funções** — [`02_create_function.ipynb`](./Lab%203%20-%20Criação%20de%20Funções/02_create_function.ipynb): funções UC (`get_store_by_id`, `geocode_address`).

**Lab 4 - Criação de Salas Genie** — guia principal: [**README do Lab 4**](./Lab%204%20-%20Criação%20de%20Salas%20Genie/README.md) (instruções Genie na UI, textos para colar, SQL `_genie_query` / `chat_with_sales`). Notebooks opcionais: [`03_1_genie_spaces.ipynb`](./Lab%204%20-%20Criação%20de%20Salas%20Genie/03_1_genie_spaces.ipynb), [`03_2_genie_tools.ipynb`](./Lab%204%20-%20Criação%20de%20Salas%20Genie/03_2_genie_tools.ipynb).

**Lab 5 - Criação do Supervisor** — [**README**](./Lab%205%20-%20Criação%20do%20Supervisor/README.md): **Supervisor Agent** com **dois Genies (Lab 4)** + **Knowledge Assistant (Lab 1)**.

**Lab 6 - Criação do App** — [`Lab 6 - Criação do App/`](./Lab%206%20-%20Criação%20do%20App/) — material em evolução.

A UI pode variar por região/versão; siga também as orientações do instrutor.

---

## Catálogo e database (schema) pessoal

| Objeto | Valor |
|--------|--------|
| Catálogo UC (tabelas/funções do lab) | `dbacademy` |
| Database / schema do participante | **`<seu_database>`** — primeira letra do nome + sobrenome em minúsculas (ex.: `cbettanim`) |
| Caminho completo dos objetos do lab | `dbacademy.<seu_database>` (ex.: `dbacademy.cbettanim`) |
| Volume de FAQ (Knowledge Assistant) | **`faq_volume`** — `dbacademy.<schema_do_volume>.faq_volume` ([Lab 1](./Lab%201%20-%20Criação%20do%20Knowledge%20Assistant/README.md)) |

Se o instrutor definir outra convenção de nome, ajuste os notebooks com *Find and Replace* em `<seu_database>`.

---

## Segurança

- **Não commite** Personal Access Tokens (PAT), senhas ou segredos.
- Para testes de `chat_with_sales`, prefira **Databricks Secrets** ou variáveis de ambiente configuradas apenas no workspace.

---

## Créditos e material visual

Os notebooks incluem imagens do repositório [Databricks-BR/workshop_agents](https://github.com/Databricks-BR/workshop_agents) (cabeçalhos e diagramas). O banner deste treinamento é específico do **AgentBricks Lab** (`banner.png` / `banner.svg`). O README referencia **PNG** porque o GitHub em geral **não renderiza SVG** em `![alt](url)` no README do repositório (política de segurança contra scripts embutidos).

---

## Publicar no GitHub

Este conteúdo foi gerado para o repositório [github.com/CaduBettanim/AgentBricks-Lab](https://github.com/CaduBettanim/AgentBricks-Lab).  
Não é possível autenticar na sua conta GitHub a partir deste ambiente; para enviar as alterações:

```bash
cd "/caminho/para/AgentBricks-Lab"
git init
git branch -M main
git remote add origin https://github.com/CaduBettanim/AgentBricks-Lab.git
git add .
git commit -m "Treinamento AgentBricks Lab: notebooks, guia e README"
git push -u origin main
```

Se o repositório remoto já tiver commits, use `git pull` com estratégia de mesclagem ou `git clone` o remoto e copie estes arquivos por cima antes do `push`.

---

## O que ainda pode ser alinhado com o instrutor (opcional)

- Nome exato do **schema** do volume **`faq_volume`** no catálogo `dbacademy` (pode ser distinto do `<seu_database>` dos Labs 2–4).
- Versão exata do **AgentBricks** e nomes de menus se a UI mudar entre regiões/versões.
- Política de **tokens** e **segredos** no workspace do cliente.
- Se a geocodificação externa for proibida, um exercício alternativo sem `geocode_address`.

---

**Licença:** defina conforme desejar no repositório público (este README não inclui arquivo de licença por padrão).
