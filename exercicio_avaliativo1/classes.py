
class Passageiro:
     def __init__(self, nome: str, documento: str):
        self.nome = nome
        self.documento = documento

class Corrida:
    def __init__(self, nota: int, distancia: float, valor: float, passageiro: Passageiro):
        self.nota_corrida = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro

class Motorista:
    def __init__(self, corridas: list, nota_motorista:int):
        self.corridas = corridas
        self.nota_motorista = nota_motorista
    

