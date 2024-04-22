from flask import request
from flask_restx import Resource, Api, fields
from flask_jwt_extended import jwt_required, create_access_token, get_jwt_identity
from app import app, db
from app.models import User
from app.services import register_user, login_user, get_balance, make_transaction

api = Api(app, version='1.0', title='API de Pagamentos', description='API para realizar transações de pagamento')

login_model = api.model('Login', {
    'email': fields.String(description='E-mail do usuário'),
    'password': fields.String(description='Senha do usuário')
})

user_model = api.model('User', {
    'name': fields.String(description='Nome completo do usuário'),
    'cpf': fields.String(description='CPF do usuário'),
    'email': fields.String(description='E-mail do usuário'),
    'password': fields.String(description='Senha do usuário'),
    'balance': fields.Float(description='Saldo do usuário'),
    'is_merchant': fields.Boolean(description='Indica se o usuário é um lojista')
})

transaction_model = api.model('Transaction', {
    'value': fields.Float(description='Valor da transação'),
    'payee': fields.Integer(description='ID do destinatário da transação')
})

@api.route('/register')
class Register(Resource):
    @api.expect(user_model)
    def post(self):
        """Endpoint para registrar um novo usuário"""
        data = request.json
        result = register_user(data)
        if result:
            return {'message': 'User registered successfully'}, 201
        else:
            return {'message': 'User registration failed'}, 400

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        """Endpoint para realizar o login do usuário"""
        data = request.json
        access_token = login_user(data)
        if access_token:
            return {'message': 'Login successful', 'access_token': access_token}, 200
        else:
            return {'message': 'Invalid credentials'}, 401

@api.route('/balance')
class Balance(Resource):
    @jwt_required()
    def get(self):
        """Endpoint para obter o saldo do usuário autenticado"""
        current_user_id = get_jwt_identity()
        balance = get_balance(current_user_id)
        return {'balance': balance}, 200

@api.route('/transaction')
class Transaction(Resource):
    @api.expect(transaction_model)
    @jwt_required()
    def post(self):
        """Endpoint para realizar uma transação de pagamento"""
        data = request.json
        current_user_id = get_jwt_identity()
        result = make_transaction(data, current_user_id)
        if result:
            return {'message': 'Transaction successful'}, 200
        else:
            return {'message': 'Transaction failed'}, 400
