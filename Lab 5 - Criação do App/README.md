# Lab 5 — Criação do App Multi-Agente

Este laboratório guia a criação de um novo App na Databricks.

---

## Objetivo

- Criar um novo App para atuar como uma nova interface limpa e intuitiva, podendo compartilhar com toda a organização.

---

## 1. Passo a passo na interface

1. No workspace Databricks, abra a aba **Compute** (Laterial esquerda).
2. Digite a seguinte instrução (Não se esqueça de alterar o nome que será dado ao seu App).
3. Selecione o botão **Create App**.
4. Na interface de criação, selecione o tipo de template chamado **Agents**.
5. Selecione o template chamado **Chat IU**.
6. Em **Serving Endpoint** selecione o endpoint do seu Supervisor. Se não souber, faça como no exercício anterior (Agents > Selecione seu Supervisor > Endpoint) e copie o id do seu endpoint.
7. Clique em **Next**.

8. Em **Review Authorizations** selecione **Next**
9. Em **App Name** coloque o nome do seu App como no exemplo a seguir: `App_<seu_database>`
10. Clique **Install**

`Agora devemos esperar o deploy da aplicação...`

### 2. Liberar acesso adicional para aplicação

1. Dentro do seu app, selecione o botão **Edit** (Canto superior direito)
2. Clique em **Next: Configure Git**
3. Clique em **Next: Configure**
4. Em **User authorization** clique no botão **+ Add scope**
5. Selecione a opção **Manage your nodel serving endpoints**
6. Selecione o botão **Save**
7. Clique no botão **Deploy**

`Agora devemos esperar o deploy desta nova alteração...`

8. Com a aplicação no ar, selecione o endereço da aplicação (do lado do status da aplicação - No caso deve estar em **Running**)
9. Dentro da interface do app, se for questionado autorização de acesso, clique em **Authorize**
10. Agora pode lançar novas perguntas. Abaixo seguem alguns exemplos:

```text
O que fazer se o pedido online atrasar?
```

```text
Quais produtos estão com estoques acima de 500 unidades?
```

```text
Quais os meses que mais venderam?
```

### PARABÉNS
Você concluiu o workshop Hands-on de criação de novos agentes de IA na Databricks!
