# sistema-para-sebos

### para ativar o ambiente virtual
> source venv/bin/activate


# Documentação do Banco de Dados

## Sistema de Gerenciamento de Sebos

Autor: Maicon Junior Silva Vieira
Data: 2026

---

# 1. Visão Geral

O sistema utiliza o banco de dados **SQLite**, executado localmente no computador que hospeda o sistema. O objetivo é armazenar e controlar informações relacionadas ao estoque de livros e sua organização em prateleiras.

O banco é criado automaticamente pelo Flask/SQLAlchemy quando a aplicação é executada.

Arquivo do banco:

```
sebo.db
```

---

# 2. Tecnologias Utilizadas

* Python
* Flask
* SQLAlchemy (ORM)
* SQLite

O SQLAlchemy permite manipular o banco usando classes Python em vez de escrever SQL diretamente, embora SQL ainda possa ser usado quando necessário.

---

# 3. Tabelas Existentes

Atualmente o sistema possui as seguintes tabelas:

1. **prateleira**
2. **livro**

Essas tabelas representam a base inicial do controle de estoque.

---

# 4. Tabela: prateleira

Responsável por armazenar as prateleiras físicas onde os livros são organizados.

## Estrutura

| Campo | Tipo       | Obrigatório | Descrição                                 |
| ----- | ---------- | ----------- | ----------------------------------------- |
| id    | Integer    | Sim         | Identificador único da prateleira         |
| nome  | String(50) | Sim         | Nome da prateleira (ex: A1, B2, Infantil) |

## Exemplo de registro

| id | nome     |
| -- | -------- |
| 1  | A1       |
| 2  | B1       |
| 3  | INFANTIL |

## Modelo SQLAlchemy

```python
class Prateleira(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(50),
        nullable=False,
        unique=True
    )
```

---

# 5. Tabela: livro

Responsável por armazenar os livros existentes no estoque.

## Estrutura

| Campo         | Tipo        | Obrigatório | Descrição                          |
| ------------- | ----------- | ----------- | ---------------------------------- |
| id            | Integer     | Sim         | Identificador do livro             |
| titulo        | String(200) | Sim         | Nome do livro                      |
| autor         | String(150) | Sim         | Autor do livro                     |
| preco_compra  | Float       | Sim         | Valor pago pelo livro              |
| quantidade    | Integer     | Sim         | Quantidade em estoque              |
| data_entrada  | DateTime    | Sim         | Data em que o livro foi cadastrado |
| id_prateleira | Integer     | Sim         | Referência à prateleira            |

## Exemplo de registro

| id | titulo   | autor   | preco_compra | quantidade | id_prateleira |
| -- | -------- | ------- | ------------ | ---------- | ------------- |
| 1  | O Hobbit | Tolkien | 5.00         | 3          | 1             |

## Modelo SQLAlchemy

```python
class Livro(db.Model):

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    titulo = db.Column(
        db.String(200),
        nullable=False
    )

    autor = db.Column(
        db.String(150),
        nullable=False
    )

    preco_compra = db.Column(
        db.Float,
        nullable=False
    )

    quantidade = db.Column(
        db.Integer,
        nullable=False
    )

    data_entrada = db.Column(
        db.DateTime
    )

    id_prateleira = db.Column(
        db.Integer,
        db.ForeignKey("prateleira.id"),
        nullable=False
    )
```

---

# 6. Relacionamento entre as tabelas

Um livro pertence a uma prateleira.

Tipo de relacionamento:

```
1 Prateleira
    ↓
Muitos Livros
```

Exemplo:

```
Prateleira A1

- Livro 1
- Livro 2
- Livro 3
```

---

# 7. Como inserir dados no banco (SQLAlchemy)

## Criar uma prateleira

```python
prateleira = Prateleira(nome="A1")

db.session.add(prateleira)
db.session.commit()
```

---

## Inserir um livro

```python
livro = Livro(
    titulo="O Hobbit",
    autor="Tolkien",
    preco_compra=5.00,
    quantidade=1,
    id_prateleira=1
)

db.session.add(livro)
db.session.commit()
```

---

# 8. Como consultar dados

## Buscar todos os livros

```python
livros = Livro.query.all()
```

---

## Buscar livros por prateleira

```python
livros = Livro.query.filter_by(
    id_prateleira=1
).all()
```

---

## Buscar uma prateleira

```python
prateleira = Prateleira.query.get(1)
```

---

# 9. Regras atuais do sistema

Atualmente o sistema realiza:

* Cadastro de prateleiras
* Entrada de livros no estoque
* Associação do livro a uma prateleira
* Registro automático da data de entrada

---

# 10. Padrões adotados

## Nomes de tabelas

Sempre em:

```
minúsculo
singular
português
```

Exemplo:

```
livro
prateleira
venda
caixa
usuario
```

---

## Nomes de campos

Sempre em:

```
snake_case
português
```

Exemplo:

```
id_prateleira
preco_compra
data_entrada
quantidade
```

---

# 11. Próximas tabelas previstas

Estas tabelas serão adicionadas futuramente ao sistema:

* movimentacao_estoque
* venda
* item_venda
* caixa
* usuario
* forma_pagamento

Essas tabelas permitirão implementar:

* Saída de estoque
* Controle de vendas
* Controle de caixa
* Relatórios

---

# 12. Observação importante

Nunca armazenar informações duplicadas desnecessariamente.

Exemplo correto:

```
Livro guarda apenas o id da prateleira
```

Não:

```
Livro guardar o nome da prateleira
```

Isso mantém o banco consistente e evita erros futuros.

---

Fim da documentação inicial do banco de dados.
