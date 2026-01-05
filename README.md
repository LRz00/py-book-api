# Book API

Uma API simples para gerenciamento de livros, construída com FastAPI.

## Tecnologias

- [FastAPI](https://fastapi.tiangolo.com/)
- SQLAlchemy (ORM)
- Pydantic (Validação de dados)
- Python-Jose (Autenticação JWT)
- Passlib (Hashing de senhas)

## Instalação

1. Clone o repositório
2. Crie um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   .\venv\Scripts\activate  # Windows
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Como Rodar

Para iniciar o servidor de desenvolvimento:

```bash
uvicorn app.main:app --reload
```

O servidor estará rodando em `http://127.0.0.1:8000`.

## Documentação

A documentação interativa da API (Swagger UI) está disponível em:

- `http://127.0.0.1:8000/docs`

## Funcionalidades

- **Autenticação**: Registro e Login de usuários.
- **Livros**: Listagem, criação, atualização e remoção de livros.
