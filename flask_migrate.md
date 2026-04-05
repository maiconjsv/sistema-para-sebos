# README — Migrações de Banco de Dados com Flask-Migrate

Este documento explica como utilizar **Flask-Migrate** no projeto para adicionar tabelas e colunas ao banco de dados **sem precisar apagar e recriar o banco**.

Esse processo é chamado de **migração de banco de dados** e é o padrão profissional usado em sistemas reais.

---

# Objetivo

Permitir que o banco evolua com segurança quando você:

* Criar uma nova tabela
* Adicionar uma nova coluna
* Alterar campos existentes
* Manter os dados já cadastrados

---

# 1. Instalar dependência

No terminal:

```bash
pip install Flask-Migrate
```

---

# 2. Configurar no app.py

Importe o Migrate:

```python
from flask_migrate import Migrate
```

Depois inicialize:

```python
migrate = Migrate(app, db)
```

Exemplo completo:

```python
from flask import Flask
from database import db
from flask_migrate import Migrate

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///sebo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa banco

db.init_app(app)

# Inicializa migração

migrate = Migrate(app, db)
```

---

# IMPORTANTE

Depois de configurar o Flask-Migrate, **remova** isso do projeto:

```python
with app.app_context():
    db.create_all()
```

Porque agora quem controla o banco é o sistema de migrações.

---

# 3. Inicializar o sistema de migração (apenas uma vez)

No terminal:

```bash
flask db init
```

Isso criará a pasta:

```text
migrations/
```

Essa pasta guarda o histórico das mudanças do banco.

---

# 4. Criar uma migração

Sempre que você alterar um model:

```bash
flask db migrate -m "descrição da mudança"
```

Exemplo:

```bash
flask db migrate -m "cria tabela usuario"
```

O sistema detecta automaticamente:

* tabelas novas
* colunas novas
* alterações

---

# 5. Aplicar a migração no banco

Depois de criar a migração:

```bash
flask db upgrade
```

Isso executa as mudanças no banco de dados.

---

# Fluxo padrão de trabalho

Sempre que mudar um model:

```bash
flask db migrate -m "descrição"
flask db upgrade
```

---

# Exemplo prático

Você cria um novo model:

```python
class Usuario(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    nome = db.Column(db.String(100), nullable=False)

    login = db.Column(db.String(150), unique=True)
```

Depois execute:

```bash
flask db migrate -m "cria tabela usuario"
flask db upgrade
```

Resultado:

A tabela será criada sem apagar o banco.

---

# Exemplo: adicionar nova coluna

Você adiciona:

```python
funcao = db.Column(
    db.String(50),
    nullable=False
)
```

Depois:

```bash
flask db migrate -m "adiciona campo funcao"
flask db upgrade
```

A coluna será adicionada automaticamente.

---

# Comandos úteis

Criar migração:

```bash
flask db migrate -m "mensagem"
```

Aplicar migração:

```bash
flask db upgrade
```

Voltar uma versão:

```bash
flask db downgrade
```

Ver histórico:

```bash
flask db history
```

---

# Estrutura criada no projeto

```text
project/

app.py

database.py

models/

routes/

migrations/
```

---

# Erros comuns

## Erro: flask command not found

Solução:

```bash
export FLASK_APP=app.py
```

Ou no Windows:

```bash
set FLASK_APP=app.py
```

---

## Erro: No changes detected

Significa que:

* Você não alterou o model
* Ou esqueceu de salvar o arquivo

---

## Erro: Target database is not up to date

Execute:

```bash
flask db upgrade
```

---

# Quando usar migration

Sempre que:

* Criar tabela
* Alterar tabela
* Adicionar coluna
* Modificar campo

---

# Quando NÃO usar

Você pode usar create_all apenas:

* No início do projeto
* Em testes
* Em protótipos rápidos

---

# Recomendação para este projeto

Use sempre:

```bash
flask db migrate
flask db upgrade
```

Isso evita:

* Perda de dados
* Recriação do banco
* Bugs em produção

---

# Resumo rápido

Sempre que mudar models:

```bash
flask db migrate -m "mudança"
flask db upgrade
```

Pronto. O banco será atualizado com segurança.
