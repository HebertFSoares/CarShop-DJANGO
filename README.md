# CarShop
Este é um projeto de um sistema de gerenciamento de veículos para uma loja de veículos. Ele foi desenvolvido como parte do meu aprendizado e prática em desenvolvimento web, utilizando as tecnologias Django e Python.

## Funcionalidades
- Cadastro de Usuário: Os usuários podem se cadastrar no sistema fornecendo suas informações básicas, como nome, e-mail e senha.
- Login de Usuário: Os usuários podem fazer login no sistema utilizando seu e-mail e senha.
- Cadastro de Veículos: Os usuários autenticados podem cadastrar novos veículos fornecendo informações como marca, modelo, ano, preço.
- Visualização de Detalhes do Veículo: Os usuários podem visualizar detalhes específicos de um veículo, incluindo todas as suas informações.
- Edição de Veículo: Os usuários autenticados têm a capacidade de editar as informações de um veículo existente.
- Exclusão de Veículo: Os usuários autenticados podem excluir um veículo do sistema.
- Pesquisa de Veículos: Os usuários podem pesquisar veículos com base em critérios específicos, como marca, modelo, ano, etc.

## Tecnologias Utilizadas
- Python
- Django
- Sqlite
- HTML/CSS
- Bootstrap

## Requisitos
### Para executar o projeto em sua máquina local, você precisará ter o Python 3 instalado. Além disso, recomendamos utilizar um ambiente virtual para instalar as dependências necessárias.

## Instalação

### Clone este repositório em sua máquina local.

- Crie um ambiente virtual:
```
python3 -m venv myenv
```
- Ative o ambiente virtual:
```
source myenv/bin/activate
```
- Instale as dependências:
```
pip install -r requirements.txt
```
- Execute as migrações do banco de dados:
```
python manage.py migrate
```
- Crie um superusuário:
```
python manage.py createsuperuser
```
- Execute o servidor:
```
python manage.py runserver
```

## Contribuição
Este projeto é de código aberto e contribuições são bem-vindas. Se você quiser contribuir com o projeto, por favor, abra uma issue ou um pull request.

## Licença
Este projeto está licenciado sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
