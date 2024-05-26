
class questao_1:
    def __init__(self, database):
        self.db = database
    
    def letra_a(self):
        query = "MATCH (t:Teacher{name:'Renzo'}) RETURN t.ano_nasc, t.cpf;"
        resultado = self.db.execute_query(query)
        print(resultado)
    
    def letra_b(self):
        query = '''
                match(n:Teacher)
                where n.name starts with 'M'
                return n.name, n.cpf'''
        resultado = self.db.execute_query(query)
        print(resultado)
    
    def letra_c(self):
        query = "match(c:City) return c.name"
        resultado = self.db.execute_query(query)
        print(resultado)
    
    def letra_d(self):
        query = "match(s:School) where s.number>=150 AND s.number<=550 return s.name, s.address, s.number"
        resultado = self.db.execute_query(query)
        print(resultado)
    
class questao_2:
    def __init__(self, database):
        self.db = database

    def letra_a(self):
        query = "match(t:Teacher) return max(t.ano_nasc) as mais_jovem, min(t.ano_nasc) as mais_velho"
        resultado = self.db.execute_query(query)
        print(resultado)
    
    def letra_b(self):
        query = "match(c:City) return avg(c.population) as media_populacao"
        resultado = self.db.execute_query(query)
        print(resultado)
    
    def letra_c(self):
        query = "match(c:City) where c.cep = '37540-000' return replace(c.name, 'a', 'A')"
        resultado = self.db.execute_query(query)
        print(resultado)
    
    def letra_d(self):
        query = "match (t:Teacher) return substring(t.name, 2, 1)"
        resultado = self.db.execute_query(query)
        print(resultado)