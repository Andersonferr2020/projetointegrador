import os
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Exame
from datetime import datetime

app = Flask(__name__)
app.config.from_object(Config)

# Caminho base para armazenar os arquivos
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Inicializando o banco de dados
db.init_app(app)

# Função para criar a pasta do usuário
def criar_pasta_usuario(usuario_id):
    path = os.path.join(app.config['UPLOAD_FOLDER'], str(usuario_id))
    if not os.path.exists(path):
        os.makedirs(path)
    return path

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para a página "Quem Somos"
@app.route('/quemsomos')
def quem_somos():
    return render_template('quemsomos.html')

# Rota para a página de Exames
@app.route('/exames', methods=['GET', 'POST'])
def exames():
    if request.method == 'POST':
        nome = request.form['nome']
        tipo = request.form['tipo']
        data_realizacao = datetime.strptime(request.form['data_realizacao'], '%Y-%m-%d')
        arquivo = None
        
        # Verificar se um arquivo foi enviado
        if 'arquivo' in request.files:
            arquivo = request.files['arquivo']
            if arquivo.filename != '':
                # Obter o ID do usuário (por exemplo, via session ou variável)
                usuario_id = 1  # Aqui você deve obter o ID do usuário atual
                pasta_usuario = criar_pasta_usuario(usuario_id)
                
                # Salvar o arquivo na pasta do usuário
                caminho_arquivo = os.path.join(pasta_usuario, arquivo.filename)
                arquivo.save(caminho_arquivo)
                arquivo = caminho_arquivo  # Salva o caminho do arquivo no banco de dados
        
        # Adicionando o exame ao banco de dados
        novo_exame = Exame(nome=nome, tipo=tipo, data_realizacao=data_realizacao, arquivo=arquivo)
        
        try:
            db.session.add(novo_exame)
            db.session.commit()
            return redirect(url_for('exames'))
        except Exception as e:
            db.session.rollback()
            print(f"Erro ao adicionar exame: {e}")
    
    exames_lista = Exame.query.all()
    return render_template('exames.html', exames=exames_lista)

# Criar o banco de dados se não existir
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    # Configurar para rodar na VM do Azure (geralmente em IP público ou privado)
    app.run(host='0.0.0.0', port=5000, debug=True)

