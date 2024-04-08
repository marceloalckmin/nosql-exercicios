from neo4j import GraphDatabase, basic_auth
from neo4j.exceptions import ServiceUnavailable

driver = GraphDatabase.driver(
  "bolt://3.237.74.207:7687",
  auth=basic_auth("neo4j", "supermarket-ladder-detection"))

"""
uri = 'neo4j+s://fd8bf9c5.databases.neo4j.io'
user = 'neo4j'
password = 'MKkOtjS7UbaiaE9YPZ1843EHjwflnMtGWN3z93gUYfc'
"""

def get_amount_data(tx):
    query = """
        MATCH(n) RETURN COUNT(n) AS amount;
    """
    try:
        result = tx.run(query)
        return [{
            'amount':row['amount']
        } for row in result]

    except ServiceUnavailable as exception:

        print("{query} raised an error: \n {exception}".format(query=query, exception=exception))

        raise

get_amount_data(driver)

"""
primeira query: "Quem dá familia é engenheiro?"

cypher_query: '''
MATCH (p:Engenheiro)
RETURN p.nome
'''
"""

"""
segunda query: "Fulano é pai de quem?"
nome_pai = input("Digite o nome de quem quer procurar os filhos: ")

cypher_query: '''
MATCH (p:Pessoa)-[:PAI_DE]->(p1:Pessoa)
WHERE p.nome = nome_pai
RETURN p1.nome
'''
"""

"""
terceira query: "Sicrana namora com quem desde quando?"
nome_sicrana = input("Digite o nome da sicrana: ")

cypher_query: '''
MATCH (p:Pessoa)-[n:NAMORADO_DE]->(p1:Pessoa)
WHERE p.nome = nome_sicrana
RETURN p1.nome, n.desde
'''
"""