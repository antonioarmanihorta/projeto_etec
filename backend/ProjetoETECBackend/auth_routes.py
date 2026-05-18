from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel
from jose import jwt
import os
from dotenv import load_dotenv

load_dotenv()

auth_router = APIRouter(prefix="/api/auth", tags=["auth"])

MOCK_USERS_DB = {
    "joao@aluno.cps.sp.gov.br": {
        "senha": "123",
        "nome": "João (Aluno)",
        "is_coordenador": False,
        "is_deleted": False
    },
    "maria@cps.sp.gov.br": {
        "senha": "123",
        "nome": "Maria (Professora)",
        "is_coordenador": False,
        "is_deleted": False
    },
    "carlos@cps.sp.gov.br": {
        "senha": "123",
        "nome": "Carlos (Coordenador / Super Professor)",
        "is_coordenador": True,
        "is_deleted": False
    }
}

SECRET_KEY = os.getenv("SECRET_KEY", "chave-padrao-caso-nao-ache-o-env")
ALGORITHM = "HS256"

def criar_token_jwt(dados: dict):
    return jwt.encode(dados, SECRET_KEY, algorithm=ALGORITHM)

class LoginData(BaseModel):
    email: str
    senha: str

class Token(BaseModel):
    access_token: str
    token_type: str
    tipo_usuario: str

def classificar_usuario(email: str, is_coordenador: bool) -> str:
    if is_coordenador:
        return "coordenador"
    if email.endswith("@aluno.cps.sp.gov.br"):
        return "aluno"
    if email.endswith("@cps.sp.gov.br"):
        return "professor"
    return "desconhecido"

@auth_router.post("/login", response_model=Token)
async def login(login_data: LoginData):
    usuario = MOCK_USERS_DB.get(login_data.email)
    
    if not usuario or usuario["senha"] != login_data.senha:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou senha incorretos"
        )
        
    if usuario.get("is_deleted", False):
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado: Usuário desativado ou removido pelo coordenador."
        )
    
    tipo = classificar_usuario(login_data.email, usuario.get("is_coordenador", False))
    
    dados_do_token = {"sub": login_data.email, "tipo": tipo}
    token_real = criar_token_jwt(dados_do_token)
    
    return {
        "access_token": token_real, 
        "token_type": "bearer",
        "tipo_usuario": tipo
    }

@auth_router.post("/logout")
async def logout():
    return {"mensagem": "Sessão encerrada com sucesso."}
