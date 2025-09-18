# 🧙‍♂️ Sistema de Gerenciamento de Campanha de RPG
**Disciplina:** Programação para Sistemas Web II – Trabalho Final  
**Professor:** Carlos Anderson Oliveira Silva  

Este projeto foi desenvolvido como parte da avaliação do curso de Informática para Internet do Instituto Federal de Educação, Ciência e Tecnologia Baiano - Campus Guanambi.  

A aplicação tem como foco auxiliar Mestres e Jogadores de RPG de mesa no gerenciamento de suas campanhas. O sistema possibilita organizar **personagens, guildas, itens, missões e usuários**, além de oferecer controle de acesso diferenciado para Mestres e Jogadores, garantindo uma experiência mais estruturada durante a narrativa.

---

## 🎲 Recursos do Sistema

- Cadastro e gerenciamento de **personagens, guildas, itens, missões e usuários**;  
- Exibição de listas completas (index) com todos os registros;  
- Visualização detalhada de cada entidade (ex.: ficha de personagem, informações de guilda ou itens de inventário);  
- Edição de informações já cadastradas;  
- Remoção de registros indesejados;  
- **Controle de permissões**: Mestres possuem acesso total, enquanto Jogadores têm acesso limitado.  

---

## ⚙️ Passo a Passo para Rodar o Projeto

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/italobrenorf/sistema_rpg.git

2. **Acesse a pasta do projeto**:
   ```bash
   cd sistema_rpg

3. **Crie e ative um ambiente virtual (Opcional)**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt

5. **Realize as migrações do banco de dados**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate

6. **Crie um superusuário**:
   ```bash
   python manage.py createsuperuser

7. **Execute o servidor**:
   ```bash
   python manage.py runserver

8. **Acesse localmente no navegador**:
   ```bash
   http://127.0.0.1:8000

## 💡 Perfis de Usuário

O sistema possui dois níveis de acesso:

- Mestre 🎭: tem controle total sobre a aplicação, podendo criar, editar, visualizar e remover personagens, guildas, itens e missões.
- Jogador 🧑‍🤝‍🧑: possui acesso restrito, limitado à visualização de informações ligadas ao seu personagem, à sua guilda e aos dados gerais da campanha.

Exemplo prático:
Ao acessar a área de personagens como Mestre, é possível:

- Ver todos os personagens cadastrados;
- Criar novos personagens;
- Atualizar fichas já existentes;
- Excluir registros, se necessário.

## 👥 Integrantes do Grupo

- Ítalo Breno Rocha Ferreira

- Ryan Nascimento Ladeia

- Leonardo Vinicius Pardinho Bernardo

## Link do Vídeo

 https://youtu.be/itkKo0o8cyo?si=rLW9bPh0jwOLKS-8
