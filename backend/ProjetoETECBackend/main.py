from fastapi import FastAPI

app = FastAPI()

from auth_routes import auth_router
from match_routes import match_router

app.include_router(auth_router)
app.include_router(match_router)

# obviamente baixar o python e marcar a caixa "Add python to PATH"
# baixar os arquivos do projeto "ProjetoETECBackend"
# para criar no ambiente virtual, executar no powershell: py -m venv venv
# caso precise permitir a criacao de ambientes virtuais: (Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned)
# para ativar o ambiente virtual: .\venv\Scripts\activate
# para baixar os requerimentos: pip install -r requirements.txt
# para rodar o codigo, executar no terminal: uvicorn main:app --reload
# caso nao consiga baixar os requerimentos pelo comando pip install baixar: pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose[cryptography] python-dotenv python-multipart
# para criar a secret key rodar: python -c "import secrets; print(secrets.token_hex(32))"

# endpoint:
# dom.com/match/
# dom.com/auth/

# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put/Patch -> editar
# Delete -> deletar