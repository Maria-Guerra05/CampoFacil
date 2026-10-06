CampoFácil
Sobre o projeto

O CampoFácil é um sistema web voltado à organização de  informações financeiras e documentais de pequenos produtores rurais.

A proposta é disponibilizar uma interface simples para o registro de receitas e despesas, acompanhamento do saldo, armazenamento de documentos e consulta das informações pela contabilidade.

O sistema foi desenvolvido com foco na simplicidade de uso e na centralização das informações essenciais do produtor.

## Funcionalidades

O protótipo atualmente possui:

- autenticação de usuários;
- perfil de Produtor;
- perfil de Contabilidade;
- cadastro de informações do produtor;
- cadastro e consulta de receitas;
- cadastro e consulta de despesas;
- cálculo do saldo;
- envio e armazenamento de documentos;
- painel do produtor;
- painel da contabilidade;
- vinculação de produtores à contabilidade;
- consulta das informações dos produtores vinculados;
- geração de relatório por produtor;
- controle de acesso conforme o perfil do usuário.

## Tecnologias utilizadas

- Python
- Django
- SQLite
- HTML
- CSS
- Git
- GitHub

## Estrutura do projeto

O projeto está organizado principalmente da seguinte forma:

- `campofacil/` – configurações principais do projeto Django;
- `core/` – modelos, formulários, views e regras principais da aplicação;
- `templates/` – páginas HTML do sistema;
- `static/css/` – arquivos de estilo;
- `manage.py` – utilitário de gerenciamento do Django;
- `requirements.txt` – dependências necessárias para execução do projeto.

## Como executar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/Maria-Guerra05/CampoFacil.git