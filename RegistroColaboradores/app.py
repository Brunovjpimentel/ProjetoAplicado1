from flask import Flask, request, jsonify
from models import db, Colaborador, Registro
from captura import capturar_imagem
import cv2
import os
from datetime import datetime
import envia_email2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///registro_colaboradores.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def obter_nome_colaborador(colaborador_id): 
    colaborador = Colaborador.query.get(colaborador_id)
    if colaborador:
         return colaborador.nome
    else: return None
         
# Rota para cadastro de colaboradores
@app.route('/cadastrar_colaborador', methods=['POST'])
def cadastrar_colaborador():
    try:
        dados = request.json
        print("Dados recebidos:", dados)  # Log para ver os dados recebidos
        
        colaborador = Colaborador(
            nome=dados['nome'], 
            sobrenome=dados['sobrenome'],
            cpf=dados['cpf'],
            carteira_trabalho=dados['carteira_trabalho'],
            nis=dados['nis'],
            cargo=dados['cargo'],
            departamento=dados['departamento'],
            cnpj_empresa=dados['cnpj_empresa'],
            endereco_empresa=dados['endereco_empresa'],
            email=dados['email'],
        )
        
        db.session.add(colaborador)
        db.session.commit()
        
        return jsonify({"mensagem": "Colaborador cadastrado com sucesso!"}), 201
    except Exception as e:
        print("Erro ao processar dados:", e)  # Log do erro para depuração
        return jsonify({"erro": "Erro ao processar os dados recebidos"}), 400

# Rota para registrar entrada/saída com captura de imagem
@app.route('/registrar/<int:colaborador_id>/<tipo>', methods=['POST'])
def registrar(colaborador_id, tipo):
    colaborador = Colaborador.query.get(colaborador_id)
    if not colaborador:
        return jsonify({"erro": "Colaborador não encontrado"}), 404

    caminho_imagem = capturar_imagem(colaborador_id)
    registro = Registro(
        colaborador_id=colaborador_id,
        tipo=tipo,
        caminho_imagem=caminho_imagem
    )
    db.session.add(registro)
    db.session.commit()
    return jsonify({"mensagem": f"Registro de {tipo} efetuado com sucesso!"})

# Inicialização do banco de dados e execução do servidor
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
