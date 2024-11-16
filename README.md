# Sistema de Informações Médicas  

Este projeto é um **Sistema de Informações Médicas** desenvolvido para auxiliar pacientes e cuidadores na organização de informações médicas, como exames, receitas e lembretes de medicamentos. Ele é acessível, intuitivo e foi pensado para facilitar o gerenciamento de dados de saúde.  

---

## 🎯 **Objetivo**  
Oferecer uma plataforma digital para centralizar informações médicas de forma prática, promovendo organização e suporte a usuários com diferentes níveis de experiência tecnológica.  

---

## 🛠️ **Funcionalidades**  

- **Cadastro de informações médicas:**  
  - Inserção de dados de exames, medicamentos e consultas.  

- **Consulta de informações:**  
  - Exibição de dados cadastrados, permitindo acesso rápido e organizado.  

- **Lembretes:** (função ainda em desenvolvimento) 
  - Configuração de alertas para horários de medicamentos e consultas.  

- **Acessibilidade:**  
  - Interface simples e adaptada às necessidades de idosos e cuidadores.  

---

## 📂 **Estrutura do Projeto**  

A estrutura do projeto no servidor segue o padrão:  

/ (raiz do projeto) │ ├── app/ │ ├── init.py │ ├── routes.py │ ├── models.py │ └── templates/ │ ├── index.html │ ├── exames.html │ └── quemsomos.html │ ├── static/ │ ├── css/ │ │ └── index.css │ ├── images/ │ │ ├── icon-logo-19.png │ │ └── outros-logos.png │ └── js/ │ └── main.js │ ├── tests/ │ └── test_app.py │ ├── requirements.txt ├── README.md └── run.py


---

## 🚀 **Tecnologias Utilizadas**  

- **Backend:** Flask (Python).  
- **Frontend:** HTML5, CSS3, JavaScript.  
- **Banco de Dados:** PostgreSQL.  
- **Design Responsivo:** Compatível com dispositivos móveis e desktop.  

---

## 🔧 **Instalação e Configuração**  

1️⃣ Clonar o Repositório  
git clone https://github.com/seu-usuario/sistema-informacoes-medicas.git
cd sistema-informacoes-medicas

2️⃣ Criar o Ambiente Virtual
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Instalar as Dependências
pip install -r requirements.txt

4️⃣ Executar o Projeto
python run.py
O sistema estará disponível em http://127.0.0.1:5000.

🧪 Testes
Para executar os testes:
pytest tests/

🤝 Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:

Faça um fork do projeto.
Crie uma nova branch: git checkout -b minha-nova-funcionalidade.
Realize as alterações desejadas e faça commit: git commit -m 'Adiciona nova funcionalidade'.
Envie para o branch principal: git push origin minha-nova-funcionalidade.
Abra um Pull Request.

📝 Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

👥 Equipe de Desenvolvimento
Sereni, Allan Kanesiro
Costa, Anderson Ferreira da
Salas, Cyntia Kimie Tashira Saldias
Silva, Vinícius Nogueira Alves da

📌 Notas
Este projeto é parte do Projeto Integrador da UNIVESP (Universidade Virtual do Estado de São Paulo).
Feedback dos usuários é uma prioridade para melhorias contínuas!

Se precisar de ajustes no texto ou inclusão de mais informações, é só avisar! 😊





