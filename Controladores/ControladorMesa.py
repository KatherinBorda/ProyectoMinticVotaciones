from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Modelos.Mesa import Mesa
from Modelos.Candidato import Candidato
class ControladorMesa():
    def __init__(self):
        self.repositorioMesa = RepositorioMesa()
        self.repositorioCandidato = RepositorioCandidato()
    def index(self):
        return self.repositorioMesa.findAll()
    def create(self,infoMesa):
        nuevoMesa=Mesa(infoMesa)
        return self.repositorioMesa.save(nuevoMesa)
    def show(self,id):
        elMesa=Mesa(self.repositorioMesa.findById(id))
        return elMesa.__dict__

    def update(self,id,infoMesa):
        mesaActual=Mesa(self.repositorioMesa.findById(id))
        mesaActual.numerodemesa=infoMesa["numerodemesa"]
        return self.repositorioMesa.save(mesaActual)
    def delete(self,id):
        return self.repositorioMesa.delete(id)

    # """
    #   Relación candidato y mesa
    #   """
    #
    # def asignarCandidato(self, id, id_candidato):
    #     mesaActual = Mesa(self.repositorioMesa.findById(id))
    #     cadidatoActual= Candidato (self.repositorioCandidato.findById(id_candidato))
    #     mesaActual.candidato = cadidatoActual
    #     return self.repositorioMesa.save(mesaActual)