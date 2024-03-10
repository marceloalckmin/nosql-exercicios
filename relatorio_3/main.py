from database import Database
from writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
db.resetDatabase()
pd = Pokedex(db)

#função 1: buscando por nome
pd.poke_por_nome("Blastoise")

#função 2: buscando por tipo
types = ["Dragon"]
pd.poke_por_tipo(types)

#função 3: buscando pela fraqueza a fogo e voador
types = ["Fire", "Flying"]
pd.poke_por_fraqueza(types)

#função 4: buscando pokemons que tem apenas 2 fraquezas
num = 2
pd.poke_por_numDeFraqueza(2)

#função 5:  buscando pokemons que não são evolução e que não tenham evolução
pd.poke_sem_evo()
