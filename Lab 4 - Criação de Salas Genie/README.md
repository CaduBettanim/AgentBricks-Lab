# Lab 4 - Criação de Salas Genie 

### O que é a Genie

**Genie** é uma ferramenta de análise de dados conversacional: o usuário faz perguntas em linguagem natural e o sistema traduz em consultas sobre os dados configurados, devolvendo respostas e visualizações. Isso reduz a barreira técnica e acelera perguntas de negócio sobre dados governados.

---

## Parte A — Criação de duas salas Genie

**Objetivo:** Criar **dois** Genie Spaces (logística e vendas)


### Material visual

![Cabeçalho workshop](https://raw.githubusercontent.com/Databricks-BR/workshop_agents/refs/heads/main/demo-main/img/header_workshop.png)

![Diagrama](https://raw.githubusercontent.com/Databricks-BR/workshop_agents/refs/heads/main/demo-main/img/img/03_diagram.png)

![Genie](https://raw.githubusercontent.com/Databricks-BR/workshop_agents/refs/heads/main/demo-main/img/img/03_genie.png)


1. Abra **Genie** no workspace (menu lateral à esquerda).
2. Crie em **+New** para criarmos a sala de Vendas; associe como fonte as seguintes tabelas: `dim_store`, `dim_product`, `ft_sales`, `mvw_sales`.
3. Clique em **Create**
4. Altere o nome da sala no canto superior para Genie Vendas `seu_database`. Exemplo: **Genie Vendas cbettanim**
5. Nas **instruções do espaço** (system / instructions), cole o texto da seção **Espaço de Logística** abaixo.
6. Repita para o segundo espaço, usando `mvw_sales` e o texto **Espaço de Vendas**.
7. **Anote o nome e o ID** de cada espaço — serão usados no [Lab 5](../Lab%205%20-%20Criação%20do%20Supervisor/README.md) e na Parte B (`genie_id`).

---

### Espaço de Logística (inventário)

#### Instruções (cole no Genie)

- Você é um assistente de dados especializado em análise de inventário.
- Seu objetivo principal é ajudar os usuários de negócios a obter respostas rápidas e precisas sobre os níveis de estoque de produtos.
- Você deve ser prestativo, conciso e preciso em suas respostas.
- Você DEVE fornecer TODAS as respostas em Português.
- Não importa em qual idioma o usuário faça a pergunta. Toda a sua resposta, incluindo texto, explicações e cabeçalhos de colunas em tabelas, DEVE ser em Português.

#### Perguntas de teste (exemplos)

- Qual era o estoque da capa de celular resistente em dezembro de 2023?
- Você pode me dar informações sobre a loja com id `4823349147981451781`?

  > *Os IDs de loja são gerados aleatoriamente no [Lab 2 Backup](../Lab%202%20Backup%20-%20Geração%20de%20Dados/). Use um `store_id` real da sua tabela, por exemplo:* `SELECT store_id FROM dbacademy.<seu_database>.dim_store LIMIT 5;`

- Quais produtos têm um estoque inferior a 500 unidades?

**Fonte de dados sugerida:** `dbacademy.<seu_database>.mvw_inventory`.

---

### Espaço de Vendas

#### Instruções (cole no Genie)

- Você é um assistente de dados especializado em análise de vendas.
- Seu objetivo principal é ajudar os usuários de negócios a obter respostas rápidas e precisas sobre as vendas de produtos.
- Você deve ser prestativo, conciso e preciso em suas respostas.
- Você DEVE fornecer TODAS as respostas em Português.
- Não importa em qual idioma o usuário faça a pergunta. Toda a sua resposta, incluindo texto, explicações e cabeçalhos de colunas em tabelas, DEVE ser em Português.

#### Perguntas de teste (exemplos)

- Qual é o valor médio de vendas por produto?
- Mostre em ordem decrescente.

**Fonte de dados sugerida:** `dbacademy.<seu_database>.mvw_sales`.

---

## Parte B — Funções UC: `_genie_query` e `chat_with_sales`

Objetivo: registrar no Unity Catalog uma função Python que chama a **API do Genie** e um *wrapper* SQL (`chat_with_sales`) que pode ser usado como ferramenta por outros fluxos.

**Atenção:** não armazene PAT em repositório Git. Use segredos do Databricks ou variáveis de ambiente em produção.

### 1. Criar `_genie_query`

Execute o bloco abaixo em uma **célula SQL** do workspace (ou editor SQL), **após** substituir `<seu_database>` no `USE SCHEMA`.

```sql
    
USE CATALOG dbacademy;
USE SCHEMA <seu_database>;
CREATE OR REPLACE FUNCTION _genie_query(databricks_host STRING, 
                  databricks_token STRING,
                  space_id STRING,
                  question STRING,
                  contextual_history STRING)
RETURNS STRING
LANGUAGE PYTHON
COMMENT 'Este é um agente com o qual você pode conversar para obter respostas a perguntas. Tente fazer perguntas simples e forneça histórico se houve conversas anteriores.'
AS
$$
    import json
    import os
    import time
    from dataclasses import dataclass
    from datetime import datetime
    from typing import Optional
    
    import pandas as pd
    import requests
    
    
    @dataclass
    class GenieResult:
        space_id: str
        conversation_id: str
        question: str
        content: Optional[str]
        sql_query: Optional[str] = None
        sql_query_description: Optional[str] = None
        sql_query_result: Optional[pd.DataFrame] = None
        error: Optional[str] = None
    
        def to_json_results(self):
            result = {
                "space_id": self.space_id,
                "conversation_id": self.conversation_id,
                "question": self.question,
                "content": self.content,
                "sql_query": self.sql_query,
                "sql_query_description": self.sql_query_description,
                "sql_query_result": self.sql_query_result.to_dict(
                    orient="records") if self.sql_query_result is not None else None,
                "error": self.error,
            }
            jsonified_results = json.dumps(result)
            return f"Resultados do Genie: {jsonified_results}"
    
        def to_string_results(self):
            results_string = self.sql_query_result.to_dict(orient="records") if self.sql_query_result is not None else None
            return ("Resultados do Genie: \n"
                    f"ID do Espaço: {self.space_id}\n"
                    f"ID da Conversa: {self.conversation_id}\n"
                    f"Pergunta Realizada: {self.question}\n"
                    f"Conteúdo: {self.content}\n"
                    f"Consulta SQL: {self.sql_query}\n"
                    f"Descrição da Consulta SQL: {self.sql_query_description}\n"
                    f"Resultado da Consulta SQL: {results_string}\n"
                    f"Erro: {self.error}")
    
    class GenieClient:
    
        def __init__(self, *,
                     host: Optional[str] = None,
                     token: Optional[str] = None,
                     api_prefix: str = "/api/2.0/genie/spaces"):
            self.host = host or os.environ.get("DATABRICKS_HOST")
            self.token = token or os.environ.get("DATABRICKS_TOKEN")
            assert self.host is not None, "DATABRICKS_HOST não está definido"
            assert self.token is not None, "DATABRICKS_TOKEN não está definido"
            self._workspace_client = requests.Session()
            self._workspace_client.headers.update({"Authorization": f"Bearer {self.token}"})
            self._workspace_client.headers.update({"Content-Type": "application/json"})
            self.api_prefix = api_prefix
            self.max_retries = 300
            self.retry_delay = 1
            self.new_line = "\r\n"
    
        def _make_url(self, path):
            return f"{self.host.rstrip('/')}/{path.lstrip('/')}"
    
        def start(self, space_id: str, start_suffix: str = "") -> str:
            path = self._make_url(f"{self.api_prefix}/{space_id}/start-conversation")
            resp = self._workspace_client.post(
                url=path,
                headers={"Content-Type": "application/json"},
                json={"content": "iniciando conversa" if not start_suffix else f"iniciando conversa {start_suffix}"},
            )
            resp = resp.json()
            print(resp)
            try:
              return resp["conversation_id"]
            except Exception:
              return resp
    
        def ask(self, space_id: str, conversation_id: str, message: str) -> GenieResult:
            path = self._make_url(f"{self.api_prefix}/{space_id}/conversations/{conversation_id}/messages")
            resp_raw = self._workspace_client.post(
                url=path,
                headers={"Content-Type": "application/json"},
                json={"content": message},
            )
            resp = resp_raw.json()
            message_id = resp.get("message_id", resp.get("id"))
            if message_id is None:
                print(resp, resp_raw.url, resp_raw.status_code, resp_raw.headers)
                return GenieResult(content=None, error="Falha ao obter message_id")
    
            attempt = 0
            query = None
            query_description = None
            content = None
    
            while attempt < self.max_retries:
                resp_raw = self._workspace_client.get(
                    self._make_url(f"{self.api_prefix}/{space_id}/conversations/{conversation_id}/messages/{message_id}"),
                    headers={"Content-Type": "application/json"},
                )
                resp = resp_raw.json()
                status = resp["status"]
                if status == "COMPLETED":
                    try:
    
                        query = resp["attachments"][0]["query"]["query"]
                        query_description = resp["attachments"][0]["query"].get("description", None)
                        content = resp["attachments"][0].get("text", {}).get("content", None)
                    except Exception as e:
                        return GenieResult(
                            space_id=space_id,
                            conversation_id=conversation_id,
                            question=message,
                            content=resp["attachments"][0].get("text", {}).get("content", None)
                        )
                    break
    
                elif status == "EXECUTING_QUERY":
                    self._workspace_client.get(
                        self._make_url(
                            f"{self.api_prefix}/{space_id}/conversations/{conversation_id}/messages/{message_id}/query-result"),
                        headers={"Content-Type": "application/json"},
                    )
                elif status in ["FAILED", "CANCELED"]:
                    return GenieResult(
                        space_id=space_id,
                        conversation_id=conversation_id,
                        question=message,
                        content=None,
                        error=f"Consulta falhou com status {status}"
                    )
                elif status != "COMPLETED" and attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                else:
                    return GenieResult(
                        space_id=space_id,
                        conversation_id=conversation_id,
                        question=message,
                        content=None,
                        error=f"Consulta falhou ou ainda em execução após {self.max_retries * self.retry_delay} segundos"
                    )
                attempt += 1
            resp = self._workspace_client.get(
                self._make_url(
                    f"{self.api_prefix}/{space_id}/conversations/{conversation_id}/messages/{message_id}/query-result"),
                headers={"Content-Type": "application/json"},
            )
            resp = resp.json()
            columns = resp["statement_response"]["manifest"]["schema"]["columns"]
            header = [str(col["name"]) for col in columns]
            rows = []
            output = resp["statement_response"]["result"]
            if not output:
                return GenieResult(
                    space_id=space_id,
                    conversation_id=conversation_id,
                    question=message,
                    content=content,
                    sql_query=query,
                    sql_query_description=query_description,
                    sql_query_result=pd.DataFrame([], columns=header),
                )
            for item in resp["statement_response"]["result"]["data_typed_array"]:
                row = []
                for column, value in zip(columns, item["values"]):
                    type_name = column["type_name"]
                    str_value = value.get("str", None)
                    if str_value is None:
                        row.append(None)
                        continue
                    match type_name:
                        case "INT" | "LONG" | "SHORT" | "BYTE":
                            row.append(int(str_value))
                        case "FLOAT" | "DOUBLE" | "DECIMAL":
                            row.append(float(str_value))
                        case "BOOLEAN":
                            row.append(str_value.lower() == "true")
                        case "DATE":
                            row.append(datetime.strptime(str_value, "%Y-%m-%d").date())
                        case "TIMESTAMP":
                            row.append(datetime.strptime(str_value, "%Y-%m-%d %H:%M:%S"))
                        case "BINARY":
                            row.append(bytes(str_value, "utf-8"))
                        case _:
                            row.append(str_value)
                rows.append(row)
    
            query_result = pd.DataFrame(rows, columns=header)
            return GenieResult(
                space_id=space_id,
                conversation_id=conversation_id,
                question=message,
                content=content,
                sql_query=query,
                sql_query_description=query_description,
                sql_query_result=query_result,
            )
    
    
    assert databricks_host is not None, "host não está definido"
    assert databricks_token is not None, "token não está definido"
    assert space_id is not None, "space_id não está definido"
    assert question is not None, "question não está definida"
    assert contextual_history is not None, "contextual_history não está definido"
    client = GenieClient(host=databricks_host, token=databricks_token)
    conversation_id = client.start(space_id)
    if isinstance(conversation_id, str) is False:
        return conversation_id
    formatted_message = f"""Use o histórico contextual para responder à pergunta. O histórico pode ou não ser útil. Use-o se considerar relevante.
    
    Histórico Contextual: {contextual_history}
    
    Pergunta a responder: {question}
    """
    
    try:
        result = client.ask(space_id, conversation_id, formatted_message)
    except Exception as e:
        return f"Erro: {str(e)}"
    return result.to_string_results()

$$;
```

### 2. Antes de criar `chat_with_sales`

Na próxima célula SQL, substitua:

1. **`'host'`** — URL do workspace (ex.: `https://xxx.cloud.databricks.com`), sem barra no final.
2. **`'token'`** — PAT com permissão para a API Genie (não versionize).
3. **`'genie_id'`** — identificador do **espaço Genie de vendas** criado na Parte A.

Após o treinamento, prefira [Databricks Secrets](https://docs.databricks.com/security/secrets/index.html).

### 3. Criar `chat_with_sales`

```sql
    
USE CATALOG dbacademy;
USE SCHEMA <seu_database>;
CREATE OR REPLACE FUNCTION chat_with_sales(question STRING COMMENT "a pergunta a ser feita sobre dados de e-commerce",
                  contextual_history STRING COMMENT "forneça histórico relevante para poder responder esta pergunta, assuma que o genie não mantém histórico. Use 'sem histórico relevante' se não houver nada relevante para responder a pergunta.")
RETURNS STRING
LANGUAGE SQL
COMMENT 'Este é um agente com o qual você pode conversar para obter respostas a perguntas sobre dados de e-commerce. Tente fazer perguntas simples e forneça histórico se houve conversas anteriores.' 
RETURN SELECT _genie_query(
  'host',
  'token',
  'genie_id',
  question, -- recuperado da função
  contextual_history -- recuperado da função
);
```

---

## Referências

- [Genie — Databricks](https://docs.databricks.com/aws/en/genie/)
- [Configurar Genie space](https://docs.databricks.com/aws/en/genie/set-up)
- Material visual: [Databricks-BR/workshop_agents](https://github.com/Databricks-BR/workshop_agents)

---

*Conteúdo alinhado aos notebooks `03_1_genie_spaces.ipynb` e `03_2_genie_tools.ipynb` do repositório.*
