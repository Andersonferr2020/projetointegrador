from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Exame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    data_realizacao = db.Column(db.Date, nullable=False)
    arquivo = db.Column(db.String(200), nullable=True)  # Caminho para o arquivo

    def __repr__(self):
        return f"<Exame {self.nome}>"

