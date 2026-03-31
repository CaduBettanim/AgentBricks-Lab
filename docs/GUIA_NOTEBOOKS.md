# Guia de execução dos notebooks

Este guia resume o que cada notebook faz e **como executar**, na ordem do treinamento. Catálogo e schema padrão neste repositório: **`dbacademy.workshop_agentbricks`**. Se o instrutor indicar outros nomes, faça *find/replace* nos notebooks ou ajuste as células SQL/Python.

---

## Pré-requisitos antes do notebook 01

1. Acesso ao workspace Databricks (link enviado pelo instrutor).
2. Permissões no Unity Catalog: uso do catálogo `dbacademy`, criação de tabelas/views/funções no schema `workshop_agentbricks` (ou equivalente).
3. Cluster ou **Serverless** com **DBR 16.4 LTS** (ou superior compatível), conforme indicado nos notebooks.
4. Criar o schema, se ainda não existir:

```sql
CREATE SCHEMA IF NOT EXISTS dbacademy.workshop_agentbricks;
```

---

## 01 — `01_generate_data.ipynb` — Gerar dados

**Objetivo:** popular tabelas Delta de varejo (produtos, lojas, inventário, vendas) e criar **Metric Views** para inventário e vendas.

**Como executar**

1. Anexe o notebook a um cluster (ou use serverless, se aplicável).
2. Execute as células **de cima para baixo** na seção de geração Python: imports → constantes → definições das funções de geração → bloco `if __name__ == "__main__"` (no Databricks o notebook executa esse bloco ao rodar a célula).
3. Aguarde a gravação das quatro tabelas: `dim_product`, `dim_store`, `ft_inventory`, `ft_sales`.
4. Execute as células `%sql` que fazem `SELECT ... LIMIT 10` para validar.
5. Execute as duas células `CREATE OR REPLACE VIEW ... mvw_inventory` e `mvw_sales` (Metric Views em YAML).
6. Execute as consultas de validação com `MEASURE(...)`.

**Observações**

- Os IDs (`product_id`, `store_id`, etc.) são strings geradas aleatoriamente; **cada execução produz dados diferentes**.
- Se algo falhar por permissão, confirme com o instrutor o catálogo/schema corretos.

---

## 02 — `02_create_functions.ipynb` — Funções no Unity Catalog

**Objetivo:** criar funções SQL reutilizáveis: busca de loja por ID e geocodificação via Python (Nominatim).

**Como executar**

1. **Dependência:** tabelas do notebook 01 já criadas (`dim_store` etc.).
2. Execute `CREATE OR REPLACE FUNCTION ... get_store_by_id` e teste com um `store_id` **válido** da sua base:

```sql
SELECT store_id FROM dbacademy.workshop_agentbricks.dim_store LIMIT 5;
```

Substitua o ID no exemplo `get_store_by_id("...")` por um dos retornados.

3. Execute `CREATE OR REPLACE FUNCTION ... geocode_address` (Python no UC).  
4. Teste a geocodificação com o `SELECT` de exemplo.

**Observações**

- A função Python chama **nominatim.openstreetmap.org**. Redes corporativas podem bloquear HTTPS de saída; nesse caso, peça apoio ao instrutor.
- O *User-Agent* na função deve respeitar a política de uso do Nominatim.

---

## 03_1 — `03_1_genie_spaces.ipynb` — Genie Spaces (conceito)

**Objetivo:** documentação e **instruções em texto** para criar dois espaços Genie na UI.

**Como “executar”**

1. Leia as instruções para **Espaço de Logística** (inventário / `mvw_inventory`) e **Espaço de Vendas** (`mvw_sales`).
2. No Databricks, abra **Genie** e crie **dois** espaços, configurando:
   - **Dados:** aponte para as **Metric Views** `dbacademy.workshop_agentbricks.mvw_inventory` e `dbacademy.workshop_agentbricks.mvw_sales` (ou os assets que o instrutor indicar).
   - **Instruções do sistema:** copie/adapte o texto das células markdown (tom em português, foco em negócio).
3. Use as **perguntas sugeridas** no notebook para testar cada espaço.
4. **Anote os IDs dos espaços** (ou URLs); você precisará deles no passo de AgentBricks e possivelmente no notebook `03_2`.

---

## 03_2 — `03_2_genie_tools.ipynb` — Função `_genie_query` e *wrapper*

**Objetivo:** instalar no UC uma função Python que conversa com a API do Genie e um *wrapper* SQL (`chat_with_sales`) para uso como ferramenta.

**Como executar**

1. Execute a primeira célula SQL grande: `CREATE OR REPLACE FUNCTION ... _genie_query` (permanece em `dbacademy.workshop_agentbricks`).
2. Na célula `CREATE OR REPLACE FUNCTION chat_with_sales`, **substitua os placeholders** antes de executar:
   - `'host'` → URL do workspace, ex.: `'https://sua-instancia.cloud.databricks.com'`
   - `'token'` → **não commite tokens.** Use variável de ambiente no runtime ou um segredo; em laboratório guiado o instrutor pode pedir PAT temporário.
   - `'genie_id'` → ID do **espaço Genie de Vendas** criado no passo anterior.
3. Execute o `CREATE` do `chat_with_sales`.
4. Teste chamadas conforme orientação do instrutor (pode exigir políticas de rede e permissões de API).

**Observações**

- Guardar PAT em código versionado é **inseguro**. Para produção, use segredos (Secrets) e leitura via função, conforme padrão da sua organização.
- A função `_genie_query` espera `DATABRICKS_HOST` / `DATABRICKS_TOKEN` no ambiente **ou** os parâmetros passados pelo `chat_with_sales`; alinhe com o instrutor qual modelo usar no treinamento.

---

## Próximos passos (UI — AgentBricks)

Após os notebooks:

1. **Knowledge Assistant** apontando para o volume **`dbacademy` … `faq_lojas`** (caminho exato do volume conforme workspace).
2. **Supervisor no AgentBricks** combinando os **dois Genie Spaces** (logística e vendas) e o **Knowledge Assistant**.

O roteiro detalhado da interface está no [README](../README.md#parte-2--agentbricks-interface).
