#!/bin/bash

# Atualizando pacotes
echo "Atualizando pacotes do sistema..."
sudo apt-get update -y
sudo apt-get upgrade -y

# Instalando dependências do sistema
echo "Instalando dependências do sistema..."
sudo apt-get install -y python3-pip python3-dev libpq-dev postgresql postgresql-contrib

# Instalando dependências do Flask
echo "Instalando dependências do Flask..."
pip3 install -r requirements.txt

# Criando o banco de dados PostgreSQL
echo "Criando o banco de dados..."
sudo -u postgres psql -c "CREATE DATABASE sistema_medico;"

# Criando o usuário do banco de dados e configurando permissões
echo "Criando o usuário PostgreSQL e configurando permissões..."
sudo -u postgres psql -c "CREATE USER postgres WITH PASSWORD 'AFC1234';"
sudo -u postgres psql -c "ALTER ROLE postgres SET client_encoding TO 'utf8';"
sudo -u postgres psql -c "ALTER ROLE postgres SET default_transaction_isolation TO 'read committed';"
sudo -u postgres psql -c "ALTER ROLE postgres SET timezone TO 'UTC';"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE sistema_medico TO postgres;"

# Conectando ao banco de dados e criando as tabelas
echo "Criando as tabelas no banco de dados..."
sudo -u postgres psql -d sistema_medico << EOF
-- Criar banco de dados (caso não tenha sido feito antes)
-- CREATE DATABASE sistema_medico;

-- Criar tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100),
    data_nascimento DATE,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(100) NOT NULL,
    pasta_link VARCHAR(255)
);

-- Criar tabela de exames
CREATE TABLE IF NOT EXISTS exames (
    id SERIAL PRIMARY KEY,
    tipo VARCHAR(50),
    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
    caminho_pasta VARCHAR(255),
    data_envio TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela de consultas
CREATE TABLE IF NOT EXISTS consultas (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
    data_consulta DATE,
    observacao TEXT
);

-- Criar tabela de anotações
CREATE TABLE IF NOT EXISTS anotacoes (
    id SERIAL PRIMARY KEY,
    usuario_id INT REFERENCES usuarios(id) ON DELETE CASCADE,
    data_anotacao DATE DEFAULT CURRENT_DATE,
    anotacao TEXT
);
EOF

# Configurando permissões para arquivos
echo "Configurando permissões..."
chmod +x start.sh
chmod +x deploy.sh

# Finalizando deploy
echo "Deploy concluído. A aplicação está pronta para ser iniciada."
