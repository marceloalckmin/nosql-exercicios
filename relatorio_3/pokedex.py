from database import Database
from writeAJson import writeAJson
class Pokedex:
    def __init__(self, db: Database):
        self.db = db

    def poke_por_nome(self,name: str):
        pokemon = self.db.collection.find({"name": name})
        writeAJson(pokemon,name)
        

    def poke_por_tipo(self,types: list):
        pokemons = self.db.collection.find({"type": {"$in": types}})
        writeAJson(pokemons, "pokemon_por_tipo")

    def poke_por_fraqueza(self,types: list):
        pokemons = self.db.collection.find({"weaknesses": {"$all": types}})
        writeAJson(pokemons, "pokemons_por_fraqueza")
    
    def poke_por_numDeFraqueza(self,num):
        pokemons = self.db.collection.find({"weaknesses": {"$size": num}})
        writeAJson(pokemons, f"pokemons_com_{num}_fraquezas")

    def poke_sem_evo(self):
        pokemons = self.db.collection.find({"$and": [{"next_evolution": {"$exists": False}},{"prev_evolution.num": {"$exists": False}}]})
        writeAJson(pokemons, "pokemons_sem_evo")


