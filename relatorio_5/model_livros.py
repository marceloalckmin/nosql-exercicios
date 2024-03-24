from pymongo import MongoClient
from bson.objectid import ObjectId

class ModelLivros:
    def __init__(self,database):
        self.db = database

    def create_livro(self,titulo:str, autor:str, ano:int, preco):
        try:
            result = self.db.collection.insert_one({"titulo":titulo, "autor":autor, "ano": ano, "preco":preco})
            print(f"Livro criado com o id: {result.inserted_id}")
            return result.inserted_id
        except Exception as e:
            print(f"Um erro ocorreu ao criar o livro: \n {e}")
            return None
    
    def read_livro(self, id):
        try:
            result = self.db.collection.find_one({"_id":ObjectId(id)})
            print(f"Livro encontrado: {result}")
            return result
        except Exception as e:
            print(f"Um erro ocorreu ao ler o livro: \n {e}")
            return None
    
    def update_livro(self,id,titulo:str,autor:str,ano:int,preco):
        try:
            result = self.db.collection.update_one({"_id":ObjectId(id)},{"$set":{"titulo":titulo, "autor":autor, "ano": ano, "preco": preco}})
            print(f"Livro atualizado: {result.modified_count} documento(s) modificado(s)")
            return result
        except Exception as e:
            print(f"Um erro ocorreu ao atualizar o livro: {e}")
            return None
        
    def delete_livro(self, id):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Livro deletado: {result.deleted_count} documento(s) deletado(s)")
            return result
        except Exception as e:
            print(f"Um erro ocorreu ao deletar o livro: \n {e}")
            return None