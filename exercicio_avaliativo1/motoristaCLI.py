from classes import Motorista, Passageiro, Corrida
class SimpleCIS:
    def __init__(self):
        self.commands = {}
    
    def add_command(self,name, function):
        self.commands[name] = function
    
    def run(self):
        while True:
            command = input("Entre com um comando:")
            if command == "sair":
                print("Falou!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando Inválido! Tente novamente!")

class MotoristaCLI(SimpleCIS):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("criar", self.create_motorista)
        self.add_command("ler", self.read_motorista)
        self.add_command("atualizar", self.update_motorista)
        self.add_command("deletar", self.delete_motorista)

    def create_motorista(self):
        nota_motorista = int(input("Digite a nota do motorista:"))
        corridas = []
        op = input("Você deseja adicionar uma corrida? s/n \n")
        while op.lower() == "s":
            nome = input("Digite o nome do passageiro: ")
            documento = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)

            nota_corrida = int(input("Digite a nota da corrida: "))
            distancia = float(input("Digite a distancia da corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)

            op = input("Deseja adicionar outra corrida para esse motorista? s/n \n")
        
        motorista = Motorista(corridas, nota_motorista)
        self.motorista_model.create_motorista(motorista)
    
    def read_motorista(self):
        id = input("Digite o id do motorista a ser lido:")
        motorista = self.motorista_model.read_motorista(id)

        print(f"Nota do motorista: {motorista.nota_motorista}")
        for corrida in motorista.corridas:
            print(f"Nota da corrida: {corrida.nota_corrida}")
            print(f"Distancia da corrida: {corrida.distancia}")
            print(f"Valor da corrida: {corrida.valor}")
            print(f"Nome do passageiro: {corrida.passageiro.nome}")
            print(f"Documento do passageiro: {corrida.passageiro.documento}")
    
    def update_motorista(self):
        id = input("Digite o id do motorista a ser atualizado: ")
        nota_motorista = int(input("Digite a nota do motorista: "))
        corridas = []
        op = input("Você deseja adicionar uma corrida? s/n \n")
        while op.lower() == "s":
            nome = input("Digite o nome do passageiro: ")
            documento = input("Digite o documento do passageiro: ")
            passageiro = Passageiro(nome, documento)

            nota_corrida = int(input("Digite a nota da corrida: "))
            distancia = float(input("Digite a distancia da corrida: "))
            valor = float(input("Digite o valor da corrida: "))
            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)

            op = input("Deseja adicionar outra corrida para esse motorista? s/n \n")
        
        motorista = Motorista(corridas, nota_motorista)
        self.motorista_model.update_motorista(id,motorista)

    def delete_motorista(self):
        id = input("Digite o id do motorista a ser deletado: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Bem vindo ao menu dos motoristas!")
        print("Comandos: criar, ler, atualizar, deletar e sair")
        super().run()