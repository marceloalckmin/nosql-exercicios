from database import Database
from bson.objectid import ObjectId
from classes import Motorista, Corrida, Passageiro
from pymongo import MongoClient

class MotoristaDAO:
    def __init__(self, database: Database):
        self.db = database

    def create_motorista(self,motorista:Motorista):
        try:
            corridas_dicts = [corrida.__dict__ for corrida in motorista.corridas]
            for corrida_dict in corridas_dicts:
                corrida_dict['passageiro'] = {'nome': corrida_dict['passageiro'].nome, 'documento': corrida_dict['passageiro'].documento}
            motorista.corridas = corridas_dicts
            result = self.db.collection.insert_one({"nota_motorista": motorista.nota_motorista, "corridas": motorista.corridas})
            print(f"Motorista criado com o id: {str(result.inserted_id)}")
            return result.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def update_motorista(self, id_motorista, motorista):
        try:
            corridas = []
            corridas = motorista.corridas
            motorista_doc = {
                "nota_motorista": motorista.nota_motorista,
                "corridas": corridas
            }
            result = self.db.collection.update_one({"_id": ObjectId(id_motorista)},{"$set":motorista_doc})
            print(f"Motorista atualizado!")
            return result.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def read_motorista(self, id_motorista):
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(id_motorista)})
            if motorista:
                motorista["_id"] = str(id_motorista)
                motorista["nota_motorista"] = int(motorista["nota_motorista"])
                corridas = motorista.get("corridas", [])
                for corrida in corridas:
                    corrida["nota_corrida"] = int(corrida["nota_corrida"])
                    corrida["distancia"] = float(corrida["distancia"])
                    corrida["valor"] = float(corrida["valor"])
                    corrida["passageiro"] = Passageiro(corrida["passageiro"]["nome"],corrida["passageiro"]["documento"])
                motorista["corridas"] = corridas
            return motorista
        except Exception as e:
            print(f"Ocorreu um erro ao procurar o motorista: {e}")
            return None

    def delete_motorista(self, id_motorista):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(id_motorista)})
            if result.deleted_count == 0:
                print(f"Motorista com o id {id_motorista} não foi encontrado.")
            else:
                print(f"Motorista deletado, {result.deleted_count} documento(s) deletados.")
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None