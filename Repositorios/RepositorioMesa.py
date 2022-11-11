from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Mesa import Mesa

# from bson import ObjectId

class RepositorioMesa(InterfaceRepositorio[Mesa]):
    pass
    #
    # def sumaCedulasCandidatos(self, id_candidatos):
    #     query1 = {
    #         "$match": {"materia.$id": ObjectId(id_candidatos)}
    #     }
    #     query2 = {
    #         "$group": {
    #             "_id": "$materia",
    #             "totalcedulasinscritas": {
    #                 "$sum": "$nota_final"
    #             }
    #         }
    #     }
    #     pipeline = [query1, query2]
    #     return self.queryAggregation(pipeline)