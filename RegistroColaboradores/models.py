from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Colaborador(db.Model):
    __tablename__ = 'colaboradores'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    carteira_trabalho = db.Column(db.String(20), unique=True, nullable=False)
    nis = db.Column(db.String(20), nullable=False)
    cargo = db.Column(db.String(50), nullable=False)
    departamento = db.Column(db.String(50), nullable=False)
    cnpj_empresa = db.Column(db.String(20), nullable=False)
    endereco_empresa = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    registros = db.relationship('Registro', backref='colaborador', lazy=True)

class Registro(db.Model):
    __tablename__ = 'registros'
    id = db.Column(db.Integer, primary_key=True)
    colaborador_id = db.Column(db.Integer, db.ForeignKey('colaboradores.id'), nullable=False)
    tipo = db.Column(db.String(10), nullable=False)  # "entrada" ou "saida"
    data_hora = db.Column(db.DateTime, default=datetime.utcnow)
    caminho_imagem = db.Column(db.String(100), nullable=False)  # Caminho para a imagem capturada
