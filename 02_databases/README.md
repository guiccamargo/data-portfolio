# 🗄️ Portfolio Database — CRUD com SQL e NoSQL

Implementação de um sistema de **gerenciamento de estoque** desenvolvido em múltiplos bancos de dados relacionais e não relacionais. O objetivo é demonstrar como o mesmo domínio de negócio pode ser modelado e operado em diferentes tecnologias de persistência, usando Python e Java.

---

## 📦 Domínio da aplicação

Sistema de controle de estoque de uma loja, com as seguintes operações sobre produtos:

| Operação | Descrição |
|----------|-----------|
| **Create** | Cadastro de produto com nome, preço e quantidade |
| **Read** | Consulta individual e listagem do estoque |
| **Update** | Atualização de preço e quantidade |
| **Delete** | Remoção de produto do estoque |

---

## 🛠️ Tecnologias

### Linguagens
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat&logo=openjdk&logoColor=white)

### Bancos de dados

| Banco | Tipo | Python | Java |
|-------|------|--------|------|
| MySQL | SQL | ✅ | ✅ |
| PostgreSQL | SQL | ✅ | ✅ |
| SQLite | SQL | ✅ | ✅ |
| MongoDB | NoSQL (Documento) | ✅ | ✅ |
| Redis | NoSQL (Chave-valor) | ✅ | ✅ |
| CouchDB | NoSQL (Documento) | ✅ | ✅ |
| Firebase | NoSQL (Tempo real) | ✅ | ✅ |

---

## 🗂️ Estrutura do repositório

```
02_databases/
│
├── mysql/
│   ├── python/
│   └── java/
├── postgresql/
│   ├── python/
│   └── java/
├── sqlite/
│   ├── python/
│   └── java/
├── mongodb/
│   ├── python/
│   └── java/
├── redis/
│   ├── python/
│   └── java/
├── couchdb/
│   ├── python/
│   └── java/
└── firebase/
    ├── python/
    └── java/
```

---

## ▶️ Como executar

Cada subpasta contém seu próprio conjunto de dependências. Navegue até o banco e linguagem desejados e siga as instruções abaixo.

**Python (exemplo com MySQL):**
```bash
cd mysql/python
pip install -r requirements.txt
python programa.py
```

**Java (exemplo com MySQL):**
```bash
cd mysql/java
javac Programa.java
java Programa
```

> Certifique-se de configurar as credenciais de conexão no arquivo de configuração de cada projeto antes de executar.

---

## 🎯 Objetivo

Este repositório foi desenvolvido como exercício comparativo entre paradigmas de bancos de dados — relacional vs. não relacional — e entre linguagens de programação, aplicando os mesmos requisitos de negócio em cada contexto.

---

## 👤 Autor

**Guilherme Camargo** — [@guiccamargo](https://github.com/guiccamargo)
