class Contrato:
    def __init__(self, id_contrato = None, no_contrato = None, costo = None, fecha_ini = None, fecha_fin = None) -> None:
        self.id_contrato = id_contrato
        self.no_contrato = no_contrato
        self.costo = costo
        self.fecha_ini = fecha_ini
        self.fecha_fin = fecha_fin

    def __str__(self) -> str:
        return f'Id contrato: {self.id_contrato}, No. Contrato: {self.no_contrato}, Costo: {self.costo} Fecha Inicial: {self.fecha_ini}, Fecha Final: {self.fecha_fin}'
        


