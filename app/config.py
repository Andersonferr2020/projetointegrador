import os

class Config:
    # Configuração do banco de dados PostgreSQL
    # Aqui você vai precisar colocar as credenciais de acesso ao seu banco de dados
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:AFC1234@localhost:5432/sistema_medico'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Desativa o rastreamento de modificações para melhorar performance

    # Diretório onde os arquivos serão armazenados
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'data')
    
    # Defina uma chave secreta para a sessão e segurança da aplicação
    SECRET_KEY = AFC1234  # chave aleatória e segura
