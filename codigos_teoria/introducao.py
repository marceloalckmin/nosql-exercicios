from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client['dbworld']
paises = db.countries

"""
resultado = paises.insert_one({
    'name': 'Brasil',
    'temp': {
        'SP' :26,
        'RJ': 32,
        'MG': 26
    }
})
"""

"""
resultado = paises.update_one(
    {'temp.MG': {'$exists':True}},
    {'$set':{'temp.MG':30}}
)
"""

#if resultado.acknowledged:
#    print("Documento adicionado!")
#else:
#    print("Erro na inserção")

resultado = paises.delete_one({'name':'Brasil'})
if resultado.acknowledged:
    print("Documento removido!")
else:
    print("Erro na deleção")

resultado = paises.find({'name': 'Brasil'})
for aux in resultado:
    print(aux)
