class Professor:
    def __init__(self,nome):
        self.nome = nome
        pass

    def ministrar_aula(assunto,self):
        print(f"O professor {self.nome} está ministrando uma aula sobre {assunto}")

class Aluno:
    def __init__(self,nome):
        self.nome = nome
        pass

    def presenca(self):
        print(f"O aluno {self.nome} está presente.")

class Aula:
    def __init__(self,Professor,assunto):
        self.prof = Professor
        self.assunto = assunto
        self.alunos = []
        pass

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
    
    def listar_presenca(self):
        print(f"Presença na aula sobre {self.assunto} ministrada pelo professor {self.prof.nome}")
        for i in range (0,len(self.alunos)):
            self.alunos[i].presenca()
