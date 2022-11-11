from Repositorios.RepositorioCandidato import RepositorioCandidato
# from Repositorios.RepositorioPartido import RepositorioPartido
from Modelos.Candidato import Candidato
# from Modelos.Partido import Partido

class ControladorCandidato():
    def __init__(self):
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioCandidato.findAll()
    def create(self,infoCandidato):
        nuevoCandidato=Candidato(infoCandidato)
        return self.repositorioCandidato.save(nuevoCandidato)
    def show(self,id):
        elCandidato=Candidato(self.repositorioCandidato.findById(id))
        return elCandidato.__dict__
    def update(self,id,infoCandidato):
        cadidatoActual=Candidato(self.repositorioCandidato.findById(id))
        cadidatoActual.numeroresolucion = infoCandidato["numero_resolucion"]
        cadidatoActual.cedula =infoCandidato["cedula"]
        cadidatoActual.nombre = infoCandidato["nombre"]
        cadidatoActual.apellido = infoCandidato["apellido"]
        return self.repositorioCandidato.save(cadidatoActual)
    def delete(self,id):
        return self.repositorioCandidato.delete(id)

    # """
    #   Relación candidato y partido
    #   """
    #
    # def asignarPartido(self, id, id_partido):
    #     cadidatoActual= Candidato(self.repositorioCandidato.findById(id))
    #     partidoActual= Partido (self.repositorioPartido.findById(id_partido))
    #     cadidatoActual.candidato = cadidatoActual
    #     return self.repositorioMesa.save(cadidatoActual)