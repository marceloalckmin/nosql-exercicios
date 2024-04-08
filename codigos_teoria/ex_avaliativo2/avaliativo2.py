from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

"""
primeira query: "Quem dá familia é engenheiro?"

MATCH (p:Engenheiro)
RETURN p.nome

"""

"""
segunda query: "Fulano é pai de quem?"
nome_pai = input("Digite o nome de quem quer procurar os filhos: ")

MATCH (p:Pessoa)-[:PAI_DE]->(p1:Pessoa)
WHERE p.nome = nome_pai
RETURN p1.nome
"""

"""
terceira query: "Sicrana namora com quem desde quando?"
nome_sicrana = input("Digite o nome da sicrana: ")

MATCH (p:Pessoa)-[n:NAMORADO_DE]->(p1:Pessoa)
WHERE p.nome = nome_sicrana
RETURN p1.nome, n.desde
"""