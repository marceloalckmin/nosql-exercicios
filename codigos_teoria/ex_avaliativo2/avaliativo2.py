"""
Parte1 - Queries do Neo4j:

#Criando os nodes:
CREATE(:Pessoa:Engenheiro{nome:'Marcelo',sexo:'Masculino',idade:'20'})
CREATE(:Pessoa:Advogado{nome:'Rodrigo',sexo:'Masculino',idade:'47'})
CREATE(:Pessoa:Estudante{nome:'Fernanda',sexo:'Feminino',idade:'11'})
CREATE(:Pet:Cachorro{nome:'Bebel',sexo:'Feminino',idade:'2'})
CREATE(:Pessoa:Estudante{nome:'Caroline',sexo:'Feminino',idade:'20'})
CREATE(:Pet:Gato{nome:'Gragas',sexo:'Masculino',idade:'1'})
CREATE(:Pet:Cachorro{nome:'Melissa',sexo:'Feminino',idade:'5'})
CREATE(:Pessoa:Administrativo{nome:'Suellen',sexo:'Feminino',idade:'40'})
CREATE(:Pessoa:Aposentado{nome:'Marilene',sexo:'Feminino',idade:'63'})
CREATE(:Pessoa:Administrativo{nome:'Wilson',sexo:'Masculino',idade:'62'})

#Criando os relacionamentos:
MATCH(p1:Pessoa{nome:'Marcelo'}),(p2:Pessoa{nome:'Rodrigo'})
CREATE(p2)-[:PAI_DE]->(p1)
MATCH(p1:Pessoa{nome:'Marcelo'}),(p2:Pessoa{nome:'Suellen'})
CREATE(p2)-[:PAI_DE]->(p1)
MATCH(p1:Pessoa{nome:'Fernanda'}),(p2:Pessoa{nome:'Suellen'})
CREATE(p2)-[:PAI_DE]->(p1)
MATCH(p1:Pessoa{nome:'Suellen'}),(p2:Pessoa{nome:'Marilene'})
CREATE(p2)-[:PAI_DE]->(p1)
MATCH(p1:Pessoa{nome:'Marcelo'}),(p2:Pessoa{nome:'Marilene'})
CREATE(p2)-[:AVO_DE]->(p1)
MATCH(p1:Pessoa{nome:'Marcelo'}),(p2:Pessoa{nome:'Wilson'})
CREATE(p2)-[:AVO_DE]->(p1)
MATCH(p1:Pessoa{nome:'Fernanda'}),(p2:Pessoa{nome:'Marilene'})
CREATE(p2)-[:AVO_DE]->(p1)
MATCH(p1:Pessoa{nome:'Fernanda'}),(p2:Pessoa{nome:'Wilson'})
CREATE(p2)-[:AVO_DE]->(p1)
MATCH(p1:Pessoa{nome:'Marcelo'}),(p2:Pessoa{nome:'Caroline'})
CREATE(p2)-[:NAMORADO_DE{desde:'setembro de 2023'}]->(p1)
CREATE(p1)-[:NAMORADO_DE{desde:'setembro de 2023'}]->(p2)
MATCH(p1:Pessoa{nome:'Marcelo'}),(pet:Pet)
CREATE (p1)-[:DONO_DE]->(pet)
MATCH(p1:Pessoa{nome:'Marilene'}),(p2:Pessoa{nome:'Wilson'})
CREATE (p1)-[:ESPOSO_DE]->(p2)
CREATE (p2)-[:ESPOSO_DE]->(p1)
MATCH(p1:Pessoa{nome:'Marcelo'}),(p2:Pessoa{nome:'Fernanda'})
CREATE (p1)-[:IRMAO_DE]->(p2)
CREATE (p2)-[:IRMAO_DE]->(p1)
"""



from neo4j import GraphDatabase, basic_auth
from neo4j.exceptions import ServiceUnavailable

uri = 'neo4j+s://fd8bf9c5.databases.neo4j.io'
user = 'neo4j'
password = 'MKkOtjS7UbaiaE9YPZ1843EHjwflnMtGWN3z93gUYfc'

driver = GraphDatabase.driver(
  "bolt://3.237.74.207:7687",
  auth=basic_auth("neo4j", "supermarket-ladder-detection"))


def busca_engenheiro(tx):
    cypher_query='''
        MATCH (p:Engenheiro)
        RETURN p.nome
    '''
    result = tx.run(cypher_query)
    try:
        return [nome["p.nome"] for nome in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=cypher_query, exception=exception))
        raise

def busca_filhos(tx,nome_pai):
    cypher_query=f'''
        MATCH (p:Pessoa)-[:PAI_DE]->(p1:Pessoa)
        WHERE p.nome = "{nome_pai}"
        RETURN p1.nome as nome
    '''
    result = tx.run(cypher_query, m=nome_pai)
    try:
        return [nome["nome"] for nome in result]
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=cypher_query, exception=exception))
        raise

def busca_namorado_e_duracao(tx, nome_pessoa):
    cypher_query=f'''
        MATCH (p:Pessoa)-[n:NAMORADO_DE]->(p1:Pessoa)
        WHERE p.nome = "{nome_pessoa}"
        RETURN p1.nome, n.desde
    '''
    result = tx.run(cypher_query)
    try:
        if result:
            return [(nome["p1.nome"], nome["n.desde"]) for nome in result]
        else:
            return []
    except ServiceUnavailable as exception:
        print("{query} raised an error: \n {exception}".format(query=cypher_query, exception=exception))
        raise


while True:
    print("Bem vindo ao cliente de busca da familia!")
    print("Por enquanto só temos 3 funções :c")
    print("As opções são:")
    print("1.Buscar o nome dos engenheiros da familia")
    print("2. Saber quem são os filhos de certa pessoa")
    print("3. Saber com quem e por quanto tempo certa pessoa está namorando")
    op = int(input("Escolha sua opção: "))
    if op == 1:
        with driver.session() as session:
            print("Engenheiros na familia: ", session.read_transaction(busca_engenheiro))
        break
    elif op==2:
        nome_pai = str(input("Digite o nome do pai:"))
        with driver.session() as session:
            print("Filhos de : ", session.read_transaction(busca_filhos, nome_pai))
        break
    elif op == 3:
        nome_pessoa = str(input("Digite o nome da pessoa:"))
        with driver.session() as session:
            print("Nome do(a) namorado(a) + desde quando namoram: ", session.read_transaction(busca_namorado_e_duracao, nome_pessoa))
        break
    else:
        print("Digite uma opção válida!")

driver.close()