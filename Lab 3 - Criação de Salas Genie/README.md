# Lab 3 - Criação de Salas Genie 

### O que é a Genie

**Genie** é uma ferramenta de análise de dados conversacional: o usuário faz perguntas em linguagem natural e o sistema traduz em consultas sobre os dados configurados, devolvendo respostas e visualizações. Isso reduz a barreira técnica e acelera perguntas de negócio sobre dados governados.

---

## Parte A — Criação de duas salas Genie

**Objetivo:** Criar **dois** Genie Spaces (Vendas e Logística)


![Cabeçalho workshop](https://raw.githubusercontent.com/Databricks-BR/workshop_agents/refs/heads/main/demo-main/img/header_workshop.png)

![Diagrama](https://raw.githubusercontent.com/Databricks-BR/workshop_agents/refs/heads/main/demo-main/img/img/03_diagram.png)

![Genie](https://raw.githubusercontent.com/Databricks-BR/workshop_agents/refs/heads/main/demo-main/img/img/03_genie.png)

### Espaço de Vendas

1. Abra **Genie** no workspace (menu lateral à esquerda).
2. Crie em **+New** para criarmos a sala de Vendas; associe como fonte as seguintes tabelas: `dim_store`, `dim_product`, `ft_sales`, `mvw_sales`.
3. Clique em **Create**
4. Altere o nome da sala no canto superior para Genie Vendas `seu_database`. Exemplo: **Genie Vendas cbettanim**
5. Vá até **Configure** > **Instructions**. Em **General Instructions** cole o texto abaixo:

```text
- Você é um assistente de dados especializado em análise de vendas.
- Seu objetivo principal é ajudar os usuários de negócios a obter respostas rápidas e precisas sobre as vendas de produtos.
- Você deve ser prestativo, conciso e preciso em suas respostas.
- Você DEVE fornecer TODAS as respostas em Português.
- Não importa em qual idioma o usuário faça a pergunta. Toda a sua resposta, incluindo texto, explicações e cabeçalhos de colunas em tabelas, DEVE ser em Português.
```

6. Clique em **Save**
7. No campo de perguntas faça os seguintes testes:
```text
Qual é o valor médio de vendas por produto?
```

```text
Mostre em ordem alfabética
```


---

### Espaço de Logística


1. Abra **Genie** no workspace (menu lateral à esquerda).
2. Crie em **+New** para criarmos a sala de Vendas; associe como fonte as seguintes tabelas: `dim_store`, `dim_product`, `ft_inventory`, `mvw_inventory` (para facilitar, no campo de busca digite `dbacademy.<seu_database>`)
3. Clique em **Create**
4. Altere o nome da sala no canto superior para Genie Logistica `seu_database`. Exemplo: **Genie Logistica cbettanim**
5. Vá até **Configure** > **Instructions**. Em **General Instructions** cole o texto abaixo:

```text
- Você é um assistente de dados especializado em análise de inventário.
- Seu objetivo principal é ajudar os usuários de negócios a obter respostas rápidas e precisas sobre os níveis de estoque de produtos.
- Você deve ser prestativo, conciso e preciso em suas respostas.
- Você DEVE fornecer TODAS as respostas em Português.
- Não importa em qual idioma o usuário faça a pergunta. Toda a sua resposta, incluindo texto, explicações e cabeçalhos de colunas em tabelas, DEVE ser em Português.
```

6. Clique em **Save**

7. No campo de perguntas faça os seguintes testes:
```text
Qual era o estoque da capa de celular resistente em dezembro de 2023?
```

```text
Quais produtos têm um estoque inferior a 500 unidades?
```

## Referências

- [Genie — Databricks](https://docs.databricks.com/aws/en/genie/)
- [Configurar Genie space](https://docs.databricks.com/aws/en/genie/set-up)
