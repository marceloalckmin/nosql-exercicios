
class questao_1:
    def __init__(self, database):
        self.db = database
    
    def letra_a(self):
        query = "MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf;"
        resultado =self.db.execute_query(query)
        return resultado
    
    def letra_b(self):
        query = ""