class TeacherCRUD:
    def __init__(self, database):
        self.db = database
    
    def create_teacher(self, name, ano_nasc, cpf):
        query = "CREATE (t:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        result = self.db.execute_query(query, {"name": name, "ano_nasc": ano_nasc, "cpf": cpf})
        return result
    
    def read_teacher(self, name):
        query = "match (t:Teacher {name: $name}) return t limit 1"
        result = self.db.execute_query(query, {"name": name})
        print(result)

    def update_teacher(self, name, newCpf):
        query = "match (t:Teacher{name:$name}) set t.cpf = $newCpf"
        result = self.db.execute_query(query, {"name": name, "newCpf": newCpf})
        return result

    def delete_teacher(self, name):
        query = "match (t:Teacher {name: $name}) detach delete t"
        result = self.db.execute_query(query, {"name": name})
        return result