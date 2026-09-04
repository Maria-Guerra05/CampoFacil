CAMPOFÁCIL - MVP COM BANCO DE DADOS
=====================================

O que esta versão já possui:
- Login real do Django.
- Cadastro de usuário.
- Cadastro de produtor.
- Salvamento permanente de receitas.
- Salvamento permanente de despesas.
- Upload e armazenamento de documentos.
- Dashboard com totais.
- Listagem e exclusão de receitas, despesas e documentos.
- Banco SQLite, que funciona localmente sem instalar PostgreSQL.
- Interface simples e responsiva.

COMO EXECUTAR NO WINDOWS
------------------------
1. Instale o Python 3.11 ou superior.
2. Abra o Prompt de Comando nesta pasta.
3. Crie um ambiente virtual:

   python -m venv venv

4. Ative:

   venv\Scripts\activate

5. Instale as dependências:

   pip install -r requirements.txt

6. Crie o banco:

   python manage.py migrate

7. Crie um usuário administrador:

   python manage.py createsuperuser

8. Inicie:

   python manage.py runserver

9. Abra no navegador:

   http://127.0.0.1:8000/

LOGIN
-----
Você pode entrar com o usuário criado no createsuperuser.

ADMINISTRAÇÃO
-------------
http://127.0.0.1:8000/admin/

DOCUMENTOS
----------
Os arquivos enviados ficam na pasta media/documentos.

OBSERVAÇÃO
----------
Esta é uma versão MVP para o TCC. Ainda não é uma solução pronta para produção.
Para publicar futuramente, recomenda-se PostgreSQL, HTTPS, backups, validação
mais rígida de arquivos, recuperação de senha por e-mail e configuração de segurança.

ATUALIZAÇÃO - MEU CADASTRO
A tela Meu cadastro agora permite editar nome completo, CPF/CNPJ, propriedade, telefone, município e e-mail. O e-mail é armazenado no usuário do Django e os dados do produtor permanecem salvos no SQLite.
