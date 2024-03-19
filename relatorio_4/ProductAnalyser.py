from pymongo import MongoClient

class ProductAnalyzer:
    def __init__(self,db):
        self.db = db        

    def total_vendas_dia(self):
        return self.db.aggregate([
            {
            "$group": {
            "_id": {"$dateToString": {"date": "$data_compra", "format": "%Y-%m-%d"}},
            "totalVendas": {"$sum": "$valorTotal"}
            }
            },
            {"$sort": {"_id": 1}}
            ])

    def mais_vendido(self):
        #Retorna o produto mais vendido em todas as compras
        result = self.db.aggregate([
            {"$unwind": "$produtos"},
            {
             "$group": {
              "_id": "$produtos.descricao",
              "totalVendido": {"$sum": "$produtos.quantidade"}
            }
            },
            {"$sort": {"totalVendido": -1}},
            {"$limit": 1}
            ]).next()
        return result
        

    def mais_gastou(self):
        #Encontra o cliente que mais gastou em uma única compra.
        result = self.db.aggregate([
        {
            "$group": {
            "_id": "$cliente.nome",
            "maiorCompra": {"$max": "$valorTotal"}
            }
        },
        {"$sort": {"maiorCompra": -1}},
        {"$limit": 1}
        ]).next()
        return result
        

    def products_sold_more_than_once(self):
        #Lista todos os produtos que tiveram uma quantidade vendida acima de 1 unidades.
        return self.db.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"produtos.quantidade": {"$gt": 1}}},
            {
            "$group": {
            "_id": "$produtos.descricao",
            "totalVendido": {"$sum": "$produtos.quantidade"}
            }
            },
            {"$sort": {"totalVendido": -1}}
            ])