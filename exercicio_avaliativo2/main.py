from database import Database
from query import questao_1

#criando a instancia da classe Database, que faz a conexão com o neo4j
db = Database("bolt://18.206.90.55:7687", "neo4j", "catchers-chairs-seamen")

q1 = questao_1(db)
print(q1.letra_a())
