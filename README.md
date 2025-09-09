🧙‍♂️ Sistema de Gerenciamento de Campanha de RPG

Programação para Sistemas Web II – Trabalho Final

Professor: Carlos Anderson
Projeto apresentado ao Curso de Informática para Internet do Instituto Federal de Educação, Ciência e Tecnologia Baiano - Campus Guanambi, como requisito parcial para obtenção da nota parcial da disciplina de Programação para Sistemas Web.
O sistema foi desenvolvido com o objetivo de facilitar o gerenciamento de campanhas de RPG de mesa, permitindo a organização de personagens, guildas, itens, monstros, NPCs e dungeons, além de separar permissões de acesso entre Mestre e Jogadores.

🔧 Funcionalidades

Cadastro de personagens, guildas, itens, monstros, NPCs e dungeons;

Associação de personagens a guildas;

Gerenciamento de atributos de personagens (nome, raça, classe, nível, HP, ouro e história);

Organização de monstros e NPCs que interagem com os jogadores;

Estruturação de dungeons com nível recomendado e descrição;

Controle de usuários com diferentes perfis: Mestre e Jogador;

Visualização de todos os registros (index), detalhes de cada entidade, edição e exclusão;

⚙️ Como Executar Localmente

1. Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git


2. Acesse a pasta do projeto:

cd campanha-rpg


3. Crie e ative um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


4. Instale as dependências:

pip install -r requirements.txt


5. Realize as migrações do banco de dados:

python manage.py makemigrations
python manage.py migrate


6. Crie um superusuário (para ser o Mestre ou administrador):

python manage.py createsuperuser


7. Execute o servidor:

python manage.py runserver


8. Acesse localmente no seu navegador:

http://127.0.0.1:8000

💡 Instruções de Acesso

O sistema possui dois perfis de usuário:

Mestre

Acessa todas as funcionalidades do sistema.

Pode cadastrar, editar, visualizar e excluir personagens, guildas, itens, monstros, NPCs e dungeons.

Tem controle total sobre a campanha.


Jogador

Possui acesso restrito.

Pode visualizar seu personagem, guildas e informações gerais da campanha.

Não pode criar, editar ou excluir entidades principais.



Ao realizar o login com uma conta de Mestre (superusuário), todas as funcionalidades estarão disponíveis.
Já as contas de Jogador terão restrições, acessando apenas os recursos autorizados.

👥 Integrantes do Grupo

Ítalo Breno Rocha Ferreira

Ryan Nascimento Ladeia

Leonardo Vinicius Pardinho Bernardo
