# Guia de execução dos notebooks

Este guia resume o que cada notebook faz e **como executar**, na ordem do treinamento.

**Database pessoal:** cada participante usa o schema `dbacademy.<seu_database>`, onde **`<seu_database>`** é a primeira letra do nome + sobrenome em minúsculas (ex.: Carlos Bettanim → `cbettanim`). **Substitua `<seu_database>`** em todo o notebook antes de executar (veja também o [README](../README.md#seu-database-identificador-pessoal)).

---

## Pré-requisitos antes do Lab 1

1. Acesso ao workspace Databricks (link enviado pelo instrutor).
2. Permissões no Unity Catalog: uso do catálogo `dbacademy`, criação de tabelas/views/funções no **seu** schema (`<seu_database>`).
3. Cluster ou **Serverless** com **DBR 16.4 LTS** (ou superior compatível), conforme indicado nos notebooks.
4. Criar o schema, se ainda não existir (troque `<seu_database>` pelo seu identificador):

```sql
CREATE SCHEMA IF NOT EXISTS dbacademy.<seu_database>;
```

---

## Lab 1 — `Lab 1 - Geração de Dados/01_generate_data.ipynb` — Gerar dados

**Objetivo:** popular tabelas Delta de varejo (produtos, lojas, inventário, vendas) e criar **Metric Views** para inventário e vendas.

**Como executar**

1. Substitua **`<seu_database>`** pelo seu database em todo o notebook.
2. Anexe o notebook a um cluster (ou use serverless, se aplicável).
3. Execute as células **de cima para baixo** na seção de geração Python: imports → constantes → definições das funções de geração → bloco `if __name__ == "__main__"` (no Databricks o notebook executa esse bloco ao rodar a célula).
4. Aguarde a gravação das quatro tabelas: `dim_product`, `dim_store`, `ft_inventory`, `ft_sales`.
5. Execute as células `%sql` que fazem `SELECT ... LIMIT 10` para validar.
6. Execute as duas células `CREATE OR REPLACE VIEW ... mvw_inventory` e `mvw_sales` (Metric Views em YAML).
7. Execute as consultas de validação com `MEASURE(...)`.

**Observações**

- Os IDs (`product_id`, `store_id`, etc.) são strings geradas aleatoriamente; **cada execução produz dados diferentes**.
- Se algo falhar por permissão, confirme com o instrutor o catálogo e o seu schema.

---

## Lab 2 — `Lab 2 - Criação de Funções/02_create_function.ipynb` — Funções no Unity Catalog

**Objetivo:** criar funções SQL reutilizáveis: busca de loja por ID e geocodificação via Python (Nominatim).

**Como executar**

1. Substitua **`<seu_database>`** pelo seu database em todo o notebook.
2. **Dependência:** tabelas do Lab 1 já criadas (`dim_store` etc.).
3. Execute `CREATE OR REPLACE FUNCTION ... get_store_by_id` e teste com um `store_id` **válido** da sua base:

```sql
SELECT store_id FROM dbacademy.<seu_database>.dim_store LIMIT 5;
```

Substitua o ID no exemplo `get_store_by_id("...")` por um dos retornados.

4. Execute `CREATE OR REPLACE FUNCTION ... geocode_address` (Python no UC).  
5. Teste a geocodificação com o `SELECT` de exemplo.

**Observações**

- A função Python chama **nominatim.openstreetmap.org**. Redes corporativas podem bloquear HTTPS de saída; nesse caso, peça apoio ao instrutor.
- O *User-Agent* na função deve respeitar a política de uso do Nominatim.

---

## Lab 3 (1/2) — `Lab 3 - Criação de Salas Genie/03_1_genie_spaces.ipynb` — Genie Spaces (conceito)

**Objetivo:** documentação e **instruções em texto** para criar dois espaços Genie na UI.

**Como “executar”**

1. Confirme o seu **`<seu_database>`** (mesmo usado nos notebooks anteriores).
2. Leia as instruções para **Espaço de Logística** (inventário / `mvw_inventory`) e **Espaço de Vendas** (`mvw_sales`).
3. No Databricks, abra **Genie** e crie **dois** espaços, configurando:
   - **Dados:** aponte para as **Metric Views** `dbacademy.<seu_database>.mvw_inventory` e `dbacademy.<seu_database>.mvw_sales` (com o seu database já aplicado, ex.: `dbacademy.cbettanim.mvw_inventory`).
   - **Instruções do sistema:** copie/adapte o texto das células markdown (tom em português, foco em negócio).
4. Use as **perguntas sugeridas** no notebook para testar cada espaço.
5. **Anote os IDs dos espaços** (ou URLs); você precisará deles no passo de AgentBricks e no notebook `Lab 3 - Criação de Salas Genie/03_2_genie_tools.ipynb`.

---

## Lab 3 (2/2) — `Lab 3 - Criação de Salas Genie/03_2_genie_tools.ipynb` — Função `_genie_query` e *wrapper*

**Objetivo:** instalar no UC uma função Python que conversa com a API do Genie e um *wrapper* SQL (`chat_with_sales`) para uso como ferramenta.

**Como executar**

1. Substitua **`<seu_database>`** pelo seu database nas células `USE SCHEMA` e em qualquer referência a `dbacademy.<seu_database>`.
2. Execute a primeira célula SQL grande: `CREATE OR REPLACE FUNCTION ... _genie_query` (no catálogo/schema corretos após a substituição).
3. Na célula `CREATE OR REPLACE FUNCTION chat_with_sales`, **substitua os placeholders** antes de executar:
   - `'host'` → URL do workspace, ex.: `'https://sua-instancia.cloud.databricks.com'`
   - `'token'` → **não commite tokens.** Use variável de ambiente no runtime ou um segredo; em laboratório guiado o instrutor pode pedir PAT temporário.
   - `'genie_id'` → ID do **espaço Genie de Vendas** criado no passo anterior.
4. Execute o `CREATE` do `chat_with_sales`.
5. Teste chamadas conforme orientação do instrutor (pode exigir políticas de rede e permissões de API).

**Observações**

- Guardar PAT em código versionado é **inseguro**. Para produção, use segredos (Secrets) e leitura via função, conforme padrão da sua organização.
- A função `_genie_query` espera `DATABRICKS_HOST` / `DATABRICKS_TOKEN` no ambiente **ou** os parâmetros passados pelo `chat_with_sales`; alinhe com o instrutor qual modelo usar no treinamento.

---

## Próximos passos (UI — AgentBricks e app)

Após o Lab 3, siga as pastas na raiz do repositório (conteúdo em evolução):

1. **Lab 4 - Criação do Knowledge Assistant** — volume **`faq_volume`** no catálogo **`dbacademy`** (`dbacademy.<schema_do_volume>.faq_volume`). Passo a passo: [README do Lab 4](../Lab%204%20-%20Criação%20do%20Knowledge%20Assistant/README.md).
2. **Lab 5 - Criação do Supervisor** — Supervisor Agent com dois Genie Spaces (Lab 3) + endpoint do Knowledge Assistant (Lab 4). Passo a passo: [README do Lab 5](../Lab%205%20-%20Criação%20do%20Supervisor/README.md).
3. **Lab 6 - Criação do App** — aplicativo do treinamento.

O roteiro completo está no [README](../README.md) (seção *Roteiro do treinamento*).
