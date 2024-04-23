# Desafio Back-End Frame

## Descrição

Este é um projeto desenvolvido como parte de um desafio para uma vaga de desenvolvedor back-end na empresa Framework Digital. O objetivo é criar uma API RESTFull de uma carteira virtual contemplando 2 tipos de usuários, clientes e lojistas.

## Tecnologias Utilizadas

- Python
- Flask
- Flask-RESTx
- Flask-JWT-Extended
- SQLAlchemy
- Docker

## Instalação

### Localmente

1. Clone este repositório:

```
git clone <https://github.com/EdwinNRM/Desafio-BackEnd-Frame.git>

```

1. Instale as dependências:

```
pip install -r requirements.txt

```

### Com Docker

1. Certifique-se de ter o Docker instalado em sua máquina.
2. Clone este repositório:

```
git clone <https://github.com/EdwinNRM/Desafio-BackEnd-Frame.git>

```

1. Navegue até o diretório do projeto:

```
cd Desafio-BackEnd-Frame

```

1. Construa a imagem Docker:

```
docker build -t desafio-backend-frame .

```

1. Execute o contêiner Docker:

```
docker run -p 5000:5000 desafio-backend-frame

```

## Uso

### Localmente

1. Execute o aplicativo Flask:

```
python run.py

```

1. Acesse a API em `http://localhost:5000`.

### Com Docker

1. O contêiner Docker estará em execução e a API estará acessível em `http://localhost:5000`.

## Endpoints da API

- `/register`: Endpoint para registrar um novo usuário.
- `/login`: Endpoint para autenticar um usuário e obter um token de acesso.
- `/balance`: Endpoint para verificar o saldo de um usuário.
- `/transaction`: Endpoint para realizar uma transação entre usuários.
- `/user/<user_id>`: Endpoint para atualizar e deletar os dados de um usuário.