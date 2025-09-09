🧙‍♂️ Sistema de Gerenciamento de Campanha de RPG

Programação para Sistemas Web II – Trabalho Final

Professor: Carlos Anderson Oliveira Silva

Projeto apresentado ao Curso de Informática para Internet do Instituto Federal de Educação, Ciência e Tecnologia Baiano - Campus Guanambi, como requisito parcial para obtenção da nota parcial da disciplina de Programação para Sistemas Web (PsW), desenvolvido com o objetivo de facilitar o gerenciamento de campanhas de RPG de mesa, permitindo organizar personagens, guildas, itens, monstros, NPCs e dungeons, além de separar permissões de acesso entre Mestre e Jogadores.

🔧 Funcionalidades

Cadastro de personagens, guildas, itens, monstros, NPCs e dungeons;

Visualização de todos os registros (lista/index);

Detalhamento individual de cada entidade (ex.: ficha de personagem, detalhes da guilda);

Atualização de dados já cadastrados;

Exclusão de registros;

Controle de usuários com dois perfis diferentes: Mestre e Jogador.

⚙️ Como Executar Localmente

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


Acesse a pasta do projeto:

cd campanha-rpg


Crie e ative um ambiente virtual (Opcional):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


Instale as dependências:

pip install -r requirements.txt


Realize as migrações do banco de dados:

python manage.py makemigrations
python manage.py migrate


Crie um superusuário:

python manage.py createsuperuser


Execute o servidor:

python manage.py runserver


Acesse no navegador localmente:

http://127.0.0.1:8000

💡 Instruções de Acesso

O sistema possui dois perfis de usuário:

Mestre: acessa todas as funcionalidades, podendo cadastrar, editar, visualizar e excluir personagens, guildas, itens, monstros, NPCs e dungeons.

Jogador: possui acesso restrito, podendo apenas visualizar informações relacionadas ao seu personagem, guilda e dados gerais da campanha.

Ao realizar o login com uma conta de Mestre (superusuário), todas as funcionalidades da aplicação estarão disponíveis no menu.
Por exemplo, ao acessar a página de personagens, o Mestre poderá:

Visualizar a lista completa de personagens cadastrados;

Adicionar novos personagens;

Atualizar informações de personagens existentes;

Excluir registros, se necessário.

👥 Integrantes do Grupo

Ítalo Breno Rocha Ferreira

Ryan Nascimento Ladeia

Leonardo Vinicius Pardinho Bernardo
