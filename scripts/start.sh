#!/bin/bash

# Ativando o ambiente virtual
echo "Ativando o ambiente virtual..."
source venv/bin/activate

# Iniciando o servidor Flask
echo "Iniciando a aplicação Flask..."
export FLASK_APP=app.py
export FLASK_ENV=production
flask run --host=0.0.0.0 --port=5000
