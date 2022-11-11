from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Modelos.Partido import Partido
from Modelos.Resultado import Resultado
from Repositorios.RepositorioCandidato import RepositorioCandidato
from Repositorios.RepositorioMesa import RepositorioMesa
from Repositorios.RepositorioPartido import RepositorioPartido
from Repositorios.RepositorioResultado import RepositorioResultado
from Repositorios.RepositorioResultado import Resultado


class ControladorResultado():
    def __init__(self):
        self.repositorioPartido = RepositorioPartido()
        self.repositorioCandidato = RepositorioCandidato()
        self.repositorioMesa = RepositorioMesa()
        self.repositorioResultado = RepositorioResultado()
    def index(self):
        return self.repositorioResultado.findAll()
    """
    Asignacion candidato y partido a resultado
    """
    def create(self,infoResultado,id_candidato,id_partido):
        nuevoResultado= Resultado(infoResultado)
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        elpartido=Partido(self.repositorioPartido.findById(id_partido))
        nuevoResultado.candidato=elCandidato
        nuevoResultado.partido=elpartido
        return self.repositorioResultado.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        return elResultado.__dict__
    """
    Modificación de Resultado (candidato y partido)
    """
    def update(self,id,infoResultado,id_candidato,id_partido):
        elResultado=Resultado(self.repositorioResultado.findById(id))
        elResultado.nmesa=infoResultado["nmesa"]
        elCandidato=Candidato(self.repositorioCandidato.findById(id_candidato))
        elpartido=Partido(self.repositorioPartido.findById(id_partido))
        elResultado.candidato = elCandidato
        elResultado.partido = elpartido
        return self.repositorioResultado.save(elResultado)

    def delete(self, id):
        return self.repositorioResultado.delete(id)

    def listarVotosGeneral(self):
        return self.repositorioResultado.getVotosObtenidosGeneral()
