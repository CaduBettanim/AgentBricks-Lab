# Databricks — Criação de Agentes com AgentBricks

![Faixa do treinamento](./assets/banner.svg)

Repositório do laboratório **AgentBricks Lab**: preparação de dados e ativos no Unity Catalog com notebooks Databricks, uso de **Genie Spaces** e montagem de agentes no **AgentBricks** (Knowledge Assistant e supervisor).

**Idioma:** Português (Brasil).

---

## Público-alvo

Usuários Databricks que desejam utilizar a plataforma para **construção de agentes de IA**, integrando dados governados (Unity Catalog), análise conversacional (Genie) e orquestração no AgentBricks.

---

## Requisitos para participar

| Requisito | Detalhes |
|-----------|----------|
| Acesso ao workspace | Cada participante recebe o **link do ambiente** (ex.: 1 dia antes do treinamento). Conta com permissão de login e uso de notebooks. |
| Unity Catalog | Catálogo **`dbacademy`** utilizado neste roteiro (volume `faq_lojas` e schema de workshop). Ajuste se o instrutor fornecer nomes diferentes. |
| Permissões | `USAGE` no catálogo; `CREATE` e `SELECT` no schema de workshop (`workshop_agentbricks`); permissões para criar **Genie Spaces** e acessar **AgentBricks** conforme política da conta. |
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
│   └── banner.svg            ← identidade visual do treinamento
├── docs/
│   └── GUIA_NOTEBOOKS.md     ← passo a passo detalhado dos notebooks
└── notebooks/
    ├── 01_generate_data.ipynb
    ├── 02_create_functions.ipynb
    ├── 03_1_genie_spaces.ipynb
    └── 03_2_genie_tools.ipynb
```

---

## Roteiro do treinamento

### Parte 1 — Notebooks (ordem obrigatória)

1. **`01_generate_data.ipynb`** — Gera tabelas de vendas/logística e **Metric Views** (`mvw_inventory`, `mvw_sales`) em `dbacademy.workshop_agentbricks`.
2. **`02_create_functions.ipynb`** — Cria funções UC (`get_store_by_id`, `geocode_address`).
3. **`03_1_genie_spaces.ipynb`** — Orientação para criar **dois Genie Spaces** (logística/inventário e vendas) na interface, usando as metric views.
4. **`03_2_genie_tools.ipynb`** — Cria `_genie_query` e o *wrapper* `chat_with_sales`; exige configurar **host**, **token** e **ID do espaço Genie** conforme células SQL.

Para comandos, validações e cuidados (IDs aleatórios, substituição de `store_id`, rede), use o **[Guia dos notebooks](./docs/GUIA_NOTEBOOKS.md)**.

### Parte 2 — AgentBricks (interface)

5. **Knowledge Assistant** — No AgentBricks, crie um assistente de conhecimento apontando para o **volume** **`faq_lojas`** no catálogo **`dbacademy`** (caminho completo conforme definido no workspace, por exemplo `dbacademy.<schema_do_volume>.faq_lojas` ou estrutura equivalente do seu ambiente).
6. **Supervisor** — No AgentBricks, configure um **supervisor** que utilize:
   - os **dois Genie Spaces** criados no passo 3 (logística e vendas);
   - o **Knowledge Assistant** do passo 5.

Siga na UI as opções de seleção de ferramentas/espacos que o produto exibir na sua versão; o instrutor demonstrará o fluxo no dia do treinamento.

---

## Catálogo e schema padrão

| Objeto | Valor padrão neste repositório |
|--------|--------------------------------|
| Catálogo UC (tabelas/funções do lab) | `dbacademy` |
| Schema do lab | `workshop_agentbricks` |
| Volume de FAQ (Knowledge Assistant) | `faq_lojas` (catálogo `dbacademy`) |

Se o ambiente do cliente usar outros nomes, altere os notebooks (busca por `dbacademy.workshop_agentbricks`) ou peça um notebook “parametrizado” ao mantenedor.

---

## Segurança

- **Não commite** Personal Access Tokens (PAT), senhas ou segredos.
- Para testes de `chat_with_sales`, prefira **Databricks Secrets** ou variáveis de ambiente configuradas apenas no workspace.

---

## Créditos e material visual

Os notebooks incluem imagens do repositório [Databricks-BR/workshop_agents](https://github.com/Databricks-BR/workshop_agents) (cabeçalhos e diagramas). O banner SVG deste treinamento é específico do **AgentBricks Lab**.

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

- Nome exato do **schema** que hospeda o volume `faq_lojas` no catálogo `dbacademy`.
- Versão exata do **AgentBricks** e nomes de menus se a UI mudar entre regiões/versões.
- Política de **tokens** e **segredos** no workspace do cliente.
- Se a geocodificação externa for proibida, um exercício alternativo sem `geocode_address`.

---

**Licença:** defina conforme desejar no repositório público (este README não inclui arquivo de licença por padrão).
