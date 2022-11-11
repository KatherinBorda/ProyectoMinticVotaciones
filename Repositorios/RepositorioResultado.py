from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado


from bson import ObjectId
class RepositorioResultado(InterfaceRepositorio[Resultado]):
    #pass


    def getVotosObtenidosGeneral(self):
        query1 = {
            "$group": {
                "_id": "$candidato",
                "count": {
                        "$count": {}
                }
            }
        }
        query2 = {
            "$sort": {
                    "count": "-1"
            }
        }
        pipeline = [query1,query2]
        return self.queryAggregation(pipeline)

# candidato, partido politico
#
#
# def getVotosObtenidosGeneralporMesa(self, ):
# candidato, partido politico, mesa



