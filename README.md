# Desafio Back-End Frame

## Descrição
Este é um projeto desenvolvido como parte de um desafio para uma vaga de desenvolvedor back-end na empresa Framework Digital. O objetivo é criar uma API RESTFull de uma carteira virtual contemplando 2 tipos de usuários, clientes e lojistas.

## Tecnologias Utilizadas
- Python
- Flask
- Flask-RESTx
- Flask-JWT-Extended
- SQLAlchemy

## Instalação
1. Clone o repositório:

## Instalação

1. Clone este repositório:
```
git clone https://github.com/EdwinNRM/Desafio-BackEnd-Frame.git
```
2. Instale as dependências:
```
pip install -r requirements.txt
```

## Uso

1. Execute o aplicativo Flask:
```
python run.py
```
2. Acesse a API em `http://localhost:5000`.

## Endpoints da API

- `/register`: Endpoint para registrar um novo usuário.
- `/login`: Endpoint para autenticar um usuário e obter um token de acesso.
- `/balance`: Endpoint para verificar o saldo de um usuário.
- `/transaction`: Endpoint para realizar uma transação entre usuários.
- `/user/<user_id>`: Endpoint para atualizar e deletar os dados de um usuário.