from services.nlp_service import NLPService
from models.solicitacao_model import SolicitacaoModel

class ClassificacaoController:
    def __init__(self):
        self.nlp_service = NLPService()
        self.model = SolicitacaoModel()

    def processar_solicitacao(self, texto):
        categoria, palavra_encontrada = self.nlp_service.classificar(texto)
        self.model.salvar(texto, categoria, palavra_encontrada)
        return {
            "texto": texto,
            "categoria": categoria,
            "palavra_encontrada": palavra_encontrada
        }

    def obter_historico(self):
        return self.model.listar_todos()