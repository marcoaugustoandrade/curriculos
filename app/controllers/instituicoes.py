from app import app, db
from flask import render_template, request
from app.models.tables import Instituicao

@app.route('/instituicoes')
def listar_instituicoes():
    i = Instituicao.query.all()
    return render_template('listar_instituicoes.html', instituicao=i)

@app.route('/instituicoes/<instituicao_id>')
def detalhar_instituicoes(instituicao_id):
    i = Instituicao.query.filter_by(id=instituicao_id).first()
    return render_template('detalhar_instituicoes.html', i=i)

@app.route('/instituicoes/nova')
def carregar_formulario():
    return render_template('formulario_instituicoes.html')

@app.route('/instituicoes/inserir', methods=['POST'])
def inserir_instituicao():
    # Recebendo os dados do formulário
    nome = request.form['nome']
    sigla = request.form['sigla']
    
    # Cadastrando no banco de dados
    i = Instituicao(nome=nome, sigla=sigla)
    db.session.add(i)
    db.session.commit()

    instituicoes = Instituicao.query.all()
    return render_template('listar_instituicoes.html', instituicao=instituicoes)