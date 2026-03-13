class TextoExtraido:
    def __init__(self, conteudo, status="secesso"):
        self.conteudo = conteudo
        self.status = status

    def to_dict(self):
        return {"message": self.conteudo, "status": self.status}