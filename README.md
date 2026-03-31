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
| Unity Catalog | Catálogo **`dbacademy`** utilizado neste roteiro (volume **`faq_volume`** para o Lab 4 e o **seu** schema pessoal `<seu_database>` nos notebooks). Ajuste se o instrutor fornecer nomes diferentes. |
| Permissões | `USAGE` no catálogo; `CREATE` e `SELECT` no **seu** schema (`dbacademy.<seu_database>`); permissões para criar **Genie Spaces** e acessar **AgentBricks** conforme política da conta. |
| Runtime | **DBR 16.4 LTS** ou versão indicada pelo instrutor (anotada nos notebooks). |
| Navegador | Navegador atualizado para UI do Databricks, Genie e AgentBricks. |
| Rede | Para o notebook de funções: possível necessidade de **HTTPS de saída** para geocodificação (OpenStreetMap Nominatim). Redes restritas podem exigir exceção. |

**Pré-trabalho (opcional):** familiaridade básica com SQL e notebooks Python no Databricks.

---

## Estrutura do repositório

```
AgentBricks-Lab/
├── README.md                 ← você está aqui
├── assets/
│   ├── banner.png            ← faixa do treinamento (README no GitHub usa PNG)
│   └── banner.svg            ← mesma arte em vetor (edição / outros usos)
├── docs/
│   └── GUIA_NOTEBOOKS.md     ← passo a passo detalhado dos notebooks
├── Lab 1 - Geração de Dados/
│   └── 01_generate_data.ipynb
├── Lab 2 - Criação de Funções/
│   └── 02_create_function.ipynb
├── Lab 3 - Criação de Salas Genie/
│   ├── 03_1_genie_spaces.ipynb
│   └── 03_2_genie_tools.ipynb
├── Lab 4 - Criação do Knowledge Assistant/
│   └── README.md             ← passo a passo Knowledge Assistant + UC volume
├── Lab 5 - Criação do Supervisor/
└── Lab 6 - Criação do App/
```

---

## Roteiro do treinamento

### Parte 1 — Laboratórios (ordem obrigatória)

**Lab 1 - Geração de Dados** — [`01_generate_data.ipynb`](./Lab%201%20-%20Geração%20de%20Dados/01_generate_data.ipynb): gera tabelas de vendas/logística e **Metric Views** (`mvw_inventory`, `mvw_sales`) em `dbacademy.<seu_database>` (substitua pelo seu identificador).

**Lab 2 - Criação de Funções** — [`02_create_function.ipynb`](./Lab%202%20-%20Criação%20de%20Funções/02_create_function.ipynb): cria funções UC (`get_store_by_id`, `geocode_address`).

**Lab 3 - Criação de Salas Genie** — na mesma pasta, execute em sequência:
1. [`03_1_genie_spaces.ipynb`](./Lab%203%20-%20Criação%20de%20Salas%20Genie/03_1_genie_spaces.ipynb) — orientação para criar **dois Genie Spaces** (logística/inventário e vendas) na interface, usando as metric views.
2. [`03_2_genie_tools.ipynb`](./Lab%203%20-%20Criação%20de%20Salas%20Genie/03_2_genie_tools.ipynb) — cria `_genie_query` e o *wrapper* `chat_with_sales`; exige configurar **host**, **token** e **ID do espaço Genie** conforme células SQL.

Para comandos, validações e cuidados (IDs aleatórios, substituição de `store_id`, rede), use o **[Guia dos notebooks](./docs/GUIA_NOTEBOOKS.md)**.

### Parte 2 — AgentBricks e app (interface)

**Lab 4 - Criação do Knowledge Assistant** — siga o [**README do Lab 4**](./Lab%204%20-%20Criação%20do%20Knowledge%20Assistant/README.md): na UI **Agents** → **Knowledge Assistant**, criar o assistente com fonte **UC Files** no volume **`faq_volume`** do catálogo **`dbacademy`** (`dbacademy.<schema_do_volume>.faq_volume`). *No ambiente do instrutor o volume pode estar em outro catálogo; o material padroniza `dbacademy` para os alunos.*

**Lab 5 - Criação do Supervisor** — pasta [`Lab 5 - Criação do Supervisor/`](./Lab%205%20-%20Criação%20do%20Supervisor/): no AgentBricks, configurar um **supervisor** que utilize os **dois Genie Spaces** do Lab 3 (logística e vendas) e o **Knowledge Assistant** do Lab 4. *Material detalhado será adicionado nesta pasta.*

**Lab 6 - Criação do App** — pasta [`Lab 6 - Criação do App/`](./Lab%206%20-%20Criação%20do%20App/): criação/publicação do aplicativo associado ao fluxo do treinamento. *Material detalhado será adicionado nesta pasta.*

Siga na UI as opções que o produto exibir na sua versão; o instrutor demonstrará o fluxo no dia do treinamento.

---

## Catálogo e database (schema) pessoal

| Objeto | Valor |
|--------|--------|
| Catálogo UC (tabelas/funções do lab) | `dbacademy` |
| Database / schema do participante | **`<seu_database>`** — primeira letra do nome + sobrenome em minúsculas (ex.: `cbettanim`) |
| Caminho completo dos objetos do lab | `dbacademy.<seu_database>` (ex.: `dbacademy.cbettanim`) |
| Volume de FAQ (Knowledge Assistant) | **`faq_volume`** no catálogo **`dbacademy`** — caminho `dbacademy.<schema_do_volume>.faq_volume` (veja [Lab 4](./Lab%204%20-%20Criação%20do%20Knowledge%20Assistant/README.md)) |

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

- Nome exato do **schema** que hospeda o volume **`faq_volume`** no catálogo `dbacademy` (pode ser distinto do `<seu_database>` dos Labs 1–3).
- Versão exata do **AgentBricks** e nomes de menus se a UI mudar entre regiões/versões.
- Política de **tokens** e **segredos** no workspace do cliente.
- Se a geocodificação externa for proibida, um exercício alternativo sem `geocode_address`.

---

**Licença:** defina conforme desejar no repositório público (este README não inclui arquivo de licença por padrão).
