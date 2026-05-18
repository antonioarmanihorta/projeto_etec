from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

# cria a conexao do banco 
db = create_engine("sqlite:///banco.db")

# cria a base do banco de dados
Base = declarative_base()

# criar as classes/tabelas do banco
# usuario
# partidas
# historico


# executa a craicao dos metadados do banco(cria o banco de dados)


