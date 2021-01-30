<h1 align="center">
  Trophy
</h1>

# Sobre

Sistema de premiação de troféus para um jogo.


# Estrutura

## API

API é responsável por registrar as ações do jogo e premiar o usuário, além de autenticar

**Tecnologias**

- [Python](https://www.python.org/)
- [Django Framework](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)

## Web

Aplicação React simples para consumir a API

**Tecnologias**

- [Javascritp](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [React](https://reactjs.org/)
- [Bootstrap](https://react-bootstrap.github.io/)  

## Instalação

### Pré Requisitos

- [Python](https://www.python.org/)
- [PIP](https://pip.pypa.io/en/stable/installing/)
- [Node](https://nodejs.org/en/download/)


### Donwload e Execução

1. Clone o repositório:
```bash
git clone https://github.com/glairtonsantos/trophy.git
```
2. Crie um ambiente virtual para as depedências do Python:

Algumas opções para fazer isso são:
- [venv](https://docs.python.org/3/library/venv.html)
- [conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/)

Exemplo com `virtualenv`
```bash
python -m pip install --user virtualenv
```
**obs: em algumas instalações é necessário utilizar `python3` ou `pip3` no comando*

depois crie um ambiente virtual
```bash
virtualenv nome_da_virtualenv
```

após criar uma `virtualenv` basta ativar
```bash
source nome_da_virtualenv/bin/activate
```

3. Instale as depedências da API

acesse a pasta da `api` e execute o comando (com a `virtualenv` ativada)
```bash
cd api/
pip install -r requirements.txt
```

para verificar as depedências instaladas basta executar
```bash
pip freeze
```

4. Criar Tabelas da aplicação

Agora execute o comando `migrate` para criar um banco `sqlite`
```bash
python manage.py migrate
```
após executar esse comando um `db.sqlite3` será criado

5. Criando usuário admin:

Agora para acessar a sessão `Admin` do Django é preciso criar um usuário
```bash
python manage.py createsuperuser --username admin --email admin@email.com
```
após executar esse comando será necessário adicionar um senha

6. Popular tabelas

Foi criado um comando para criar 3 categorias e os níveis de cada, de acordo com o descrito no [desafio](https://public.3.basecamp.com/p/evofybzgHo1ffgqq6CZXGDMk)
```bash
python manage.py create_categories_and_levels
```

7. Executar API:

Agora para executar basta
```bash
python manage.py runserver
```
Abra no seu navegador `http://localhost:8000/`


## Usando

### Endpoints

#### Auth Token

| Method | Endpoint           | Descrição            |
| :----: | ------------------ | -------------------- |
| `POST` | `/api-token-auth/` | Autenticar usuário   |


#### Coletando Moedas

| Method | Endpoint              | Descrição                                |
| :----: | --------------------- | ---------------------------------------- |
| `POST`  | `/coins/collect/`    | Coleta uma moeda para o usuário logado   |


#### Monstros

| Method | Endpoint            | Descrição                             |
| :----: | --------------      | ------------------------------------- |
| `GET`  | `/monsters/`        | Lista todos os monstros cadastrados   |
| `POST` | `/monsters/kill/`   | Matar um monstro para usuário logado  |


#### Mortes

|  Method  | Endpoint         | Descrição                              |
| :------: | ---------------- | -------------------------------------- |
|  `POST`  | `/users/die/`    | Registra uma morte do usuário          |


#### Detalhes

|  Method  | Endpoint         | Descrição                                  |
| :------: | ---------------- | ------------------------------------------ |
|  `GET`   | `/user/detail/`  | Lista as quantidade de moedas coletadas,   |
|          |                  | monstros mortos e mortes do usuário logado |


#### Troféus

|  Method  | Endpoint         | Descrição                                    |
| :------: | ---------------- | -------------------------------------------- |
|  `GET`   | `/trophies/`     | Lista os troféus que o usuário logado possui |


### Admin

Para acessar o admin e realizar os cadastros basta acessar:

`http://localhost:8000/admin/` e inserir o `username` e senha do admin criado

Após acessar deve haver uma tela como abaixo:

![admin01](/assets/admin01.png)

Você pode cadastrar `monstros`, `categorias`, `níveis` e `troféus`

![monsters](/assets/monsters.png)

Para cadastrar um troféu é necessário cadastrar pelo menos uma categoria e um nível,
nos níveis é possível criar a regra do nível, por exemplo,

`Nível: 100 monstros mortos`

![level](/assets/level.png)

Ainda é possível selecionar um atributo da classe para agrupamento, por exemplo, 

`100 monstros mortos de cada`, ou seja, basta informar qual atributo identifica cada monstro:

no caso da tabela `killed_monster` é o `monster.name` (pois para acessar o atributo é necessário acessar o modelo `Monster`)

Despois de categoria e nível cadastrados basta criar os troféus

![trophies](/assets/trophies.png)

Após criar pelo menos um troféu a API está pronta para ser utilizada

### Acesso Interface web

Em outro terminal acesse a pasta `web` e instale os pacotes
```bash
cd /web
npm install
```

Após executar basta executar o comando
```bash
 npm start
```
e deve abrir localmente `http://localhost:3000/`

*obs: basta utilizar o usuário e senha criados para o admin, ou criar um usuário novo no admin da API*
