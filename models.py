from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey # importando o banco de  dados
from sqlalchemy.orm import declarative_base # importando base de estrutura do banco

# cria conexão do seu banco
db = create_engine("sqlite:///banco.db")

Base = declarative_base()# instanciando e declarando a base

# cria as classes/tabelas de banco

class Usuario (Base):
 __tablename__ = "usuarios"

 id = Column ("id", Integer, Primary_key = True, autoincrement=True) 
 nome = Column("nome", String)
 email = Column("email", String)
 senha = Column ("Senha", String, nullable=False)
 ativo = Column ("ativo", Boolean)
 admin = Column ("admin" , Boolean, default=False)
  
def __init__ (self, nome, email, senha, ativo=True , admin = False):
 self. nome = nome
 self.email = email
 self.senha = senha
 self.ativo = ativo
 self.admin = admin

 # pedido
class pedido(Base):
 __tablenem__ = "pedidos"
 id = Column ("status", String , Primary_key = True, autoincrement=True) 

 id = Column ("id", Integer,Primary_key = True, autoincrement=True)
 status = Column ("status" , String) #pendente, cancelado, finalizado
 Usuario =
 preco =

#executa a criação dos metadados do seu banco (cria efetivamente o banco de dados)





