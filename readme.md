# AWS Lambda - Insert log in DynamoDB

## 👨‍💻 Projeto desenvolvido por: 
[Rafael Torres Nantes](https://github.com/rafael-torres-nantes)

## Índice

* [📚 Contextualização do projeto](#-contextualização-do-projeto)
* [🛠️ Tecnologias/Ferramentas utilizadas](#%EF%B8%8F-tecnologiasferramentas-utilizadas)
* [🖥️ Funcionamento do sistema](#%EF%B8%8F-funcionamento-do-sistema)
    * [🧩 Parte 1 - Backend](#parte-1---backend)
    * [🎨 Parte 2 - Frontend](#parte-2---frontend)
* [🔀 Arquitetura da aplicação](#arquitetura-da-aplicação)
* [📁 Estrutura do projeto](#estrutura-do-projeto)
* [📌 Como executar o projeto](#como-executar-o-projeto)
* [🕵️ Dificuldades Encontradas](#%EF%B8%8F-dificuldades-encontradas)

## 📚 Contextualização do projeto

O projeto tem como objetivo criar uma solução automatizada para inserir logs em uma tabela DynamoDB utilizando AWS Lambda. A aplicação foi desenvolvida para registrar eventos e atividades de forma eficiente e escalável, aproveitando os serviços gerenciados da AWS.

## 🛠️ Tecnologias/Ferramentas utilizadas

[<img src="https://img.shields.io/badge/AWS_Lambda-FF9900?logo=amazonaws&logoColor=white">](https://aws.amazon.com/lambda/)
[<img src="https://img.shields.io/badge/AWS_DynamoDB-4053D6?logo=amazonaws&logoColor=white">](https://aws.amazon.com/dynamodb/)
[<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white">](https://www.python.org/)
[<img src="https://img.shields.io/badge/Visual_Studio_Code-007ACC?logo=visual-studio-code&logoColor=white">](https://code.visualstudio.com/)
[<img src="https://img.shields.io/badge/Boto3-0073BB?logo=amazonaws&logoColor=white">](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
[<img src="https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=white">](https://github.com/)

## 🖥️ Funcionamento do sistema

### 🧩 Parte 1 - Backend

O backend da aplicação foi desenvolvido utilizando **Python** com AWS Lambda, seguindo o padrão de arquitetura serverless. As principais funcionalidades incluem a inserção de logs em uma tabela DynamoDB e a integração com outros serviços AWS.

* **Handler**: O arquivo `lambda_function.py` contém a lógica responsável por processar os eventos recebidos e inserir os logs na tabela DynamoDB.
* **Serviços AWS**: A integração com DynamoDB e outras funcionalidades estão localizadas em `services/dynamodb_services.py`.
* **Utilitários**: A pasta `utils` contém funções auxiliares para manipulação de dados e configuração de credenciais AWS.

### 🎨 Parte 2 - Frontend

O frontend não é aplicável neste projeto, pois a solução é inteiramente baseada em backend e serviços AWS.

## 🔀 Arquitetura da aplicação

O sistema é baseado em uma arquitetura serverless, onde o AWS Lambda é utilizado para processar eventos e inserir logs em uma tabela DynamoDB. A arquitetura aproveita a escalabilidade e a gestão automática de recursos oferecida pela AWS.

## 📁 Estrutura do projeto

A estrutura do projeto é organizada da seguinte maneira:

```
.
├── lambda/
│   ├── services/
│   ├── utils/
│   ├── lambda_function.py
│   └── requirements.txt
└── README.md
```

## 📌 Como executar o projeto

Para executar o projeto localmente, siga as instruções abaixo:

1. **Clone o repositório:**
    ```bash
    git clone https://github.com/rafael-torres-nantes/aws-lambda-dynamodb-logger.git
    ```

2. **Instale as dependências do projeto:**
    ```bash
    cd lambda
    pip install -r requirements.txt
    ```

3. **Implante a função Lambda na AWS:**
    Utilize o AWS CLI ou o console da AWS para criar e configurar a função Lambda, garantindo que ela tenha permissões para acessar a tabela DynamoDB.

## 🕵️ Dificuldades Encontradas

Durante o desenvolvimento do projeto, algumas dificuldades foram enfrentadas, como:

- **Configuração de permissões AWS:** Garantir que a função Lambda tenha as permissões corretas para acessar e manipular a tabela DynamoDB.
- **Gerenciamento de dependências:** Manter as dependências do projeto atualizadas e compatíveis com o ambiente de execução do AWS Lambda.
- **Escalabilidade:** Ajustar a configuração da tabela DynamoDB para lidar com grandes volumes de logs sem comprometer a performance.
