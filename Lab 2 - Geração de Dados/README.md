# Lab 2 — Geração de Dados (carga CSV via Notebook)

## Objetivos

- Importar um notebook em **Python** no Databricks.
- Criar um novo dataset dentro do seu database `dbacademy.<seu_database>`.
- Crar funções.

## Exercício

1. No menu, abra **Workspace** e vá para **Home**.
2. Nos **três pontos** (⋯) no canto superior direito, escolha **Import**.
3. Na janela de importação, selecione **URL** e cole o endereço abaixo.

**Opção A — repositório AgentBricks-Lab (cópia já alinhada ao placeholder `<seu_database>`):**

```text
https://github.com/CaduBettanim/AgentBricks-Lab/blob/main/Lab%202%20-%20Geração%20de%20Dados/lab02_01_carga_csv.ipynb
```


> Se usar a **opção B**, ajuste manualmente a variável `schema_name` na célula **ALTERE ESSE PARAMETRO**, descomentando a linha e informando seu schema — ou prefira a **opção A**, onde o placeholder segue o padrão do treinamento (`<seu_database>`).

4. Abra o notebook importado. Na célula **ALTERE ESSE PARAMETRO**, garanta que `schema_name` aponta para o seu schema em `dbacademy` (use *Edit → Find and Replace* para trocar `<seu_database>` pelo seu identificador, ex.: `cbettanim`).
5. Confirme que um **cluster** ou **Serverless** está anexado (barra superior, ao lado de **Run all**).
6. Execute o notebook (**Run all**).
7. No **Catalog Explorer**, em `dbacademy.<seu_database>`, confira as tabelas criadas (ex.: `stock_bigtech`, `dim_loja`, `dim_medicamento`, `estoque`, `vendas`).

## Tabelas geradas (resumo)

Os CSV vêm de `https://github.com/CaduBettanim/lab_sql/tree/main/dados/`. Cada bloco do notebook grava uma tabela Delta com o mesmo nome base do arquivo.

## Relação com o restante do treinamento AgentBricks

Este laboratório ensina **ingestão CSV → Delta** no seu schema. As **Metric Views** `mvw_inventory` e `mvw_sales`, além das tabelas usadas nos **Labs 3 a 6** (Genie, funções, supervisor), vêm do fluxo do notebook **`Lab 2 Backup - Geração de Dados/01_generate_data.ipynb`**.

| Caminho | Quando usar |
|--------|-------------|
| **Este Lab 2** | Prática de notebook, CSV e Catalog (conteúdo tipo [README lab_sql](https://github.com/CaduBettanim/lab_sql/blob/main/02_LAB_Notebook/README.md)). |
| [**Lab 2 Backup**](../Lab%202%20Backup%20-%20Geração%20de%20Dados/) | **Obrigatório** antes dos Labs 3, 4, 5 e 6 no roteiro AgentBricks. |

---

**Referências (notebook original):** [Leitura de CSV](https://learn.microsoft.com/pt-br/azure/databricks/external-data/csv), [Notebook exemplo CSV](https://docs.databricks.com/_extras/notebooks/source/read-csv-files.html), [Delta — criar tabela](https://docs.databricks.com/delta/tutorial.html#create-a-table).
