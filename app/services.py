from app import db
from app.models import User
from flask_jwt_extended import create_access_token
import bcrypt
import requests
import logging

logging.basicConfig(filename='transaction.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def register_user(data):
    try:
        existing_user = User.query.filter_by(cpf=data['cpf']).first()
        existing_email = User.query.filter_by(email=data['email']).first()
        if existing_user or existing_email:
            return False
        
        hashed_password = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        
        new_user = User(
            name=data['name'],
            cpf=data['cpf'],
            email=data['email'],
            password=hashed_password.decode('utf-8'),
            balance=data['balance'],
            is_merchant=data.get('is_merchant', False)
        )
        
        db.session.add(new_user)
        db.session.commit()
        
        return True
    except Exception as e:
        logging.error(f'Erro ao registrar usuário: {str(e)}')
        db.session.rollback()
        return False

def login_user(data):
    try:
        email = data.get('email')
        password = data.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            return None
        
        if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
            return create_access_token(identity=user.id)
    except Exception as e:
        logging.error(f'Erro ao fazer login do usuário: {str(e)}')
    return None


def get_balance(user_id):
    try:
        user = User.query.get(user_id)
        if user:
            return user.balance
        else:
            return None
    except Exception as e:
        logging.error(f'Erro ao obter saldo do usuário: {str(e)}')
        return None

def make_transaction(data, current_user_id):
    try:
        value = data['value']
        payee_id = data['payee']
        
        payer = User.query.get(current_user_id)
        payee = User.query.get(payee_id)

        if not payee or payer.balance < value:
            logging.error(f'Transação falhou: Saldo insuficiente ou destinatário inválido. Pagador ID: {current_user_id}, Destinatário ID: {payee_id}')
            return False
        
        if payee.is_merchant:
            logging.error(f'Transação falhou: Destinatário é um lojista. Pagador ID: {current_user_id}, Destinatário ID: {payee_id}')
            return False

        response = requests.get('https://run.mocky.io/v3/5794d450-d2e2-4412-8131-73d0293ac1cc')
        if response.status_code != 200 or response.json().get('message') != 'Autorizado':
            logging.error(f'Transação falhou: Serviço de autorização retornou erro. Pagador ID: {current_user_id}, Destinatário ID: {payee_id}')
            return False

        payer.balance -= value
        payee.balance += value

        db.session.commit()
        logging.info(f'Transação bem-sucedida: Pagador ID: {current_user_id}, Destinatário ID: {payee_id}, Valor: {value}')
        return True
    except Exception as e:
        logging.error(f'Erro ao fazer transação: {str(e)}')
        db.session.rollback()
        return False
