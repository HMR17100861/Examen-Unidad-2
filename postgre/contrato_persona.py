class Contrato_persona:
    def __init__(self, id_persona = None, id_contrato = None) -> None:
        self.id_persona = id_persona
        self.id_contrato = id_contrato
    
    def __str__(self) -> str:
        return f'Id persona: {self.id_persona}, Id Contrato: {self.id_contrato}'