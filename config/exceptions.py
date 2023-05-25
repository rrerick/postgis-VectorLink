
class ExecutionFailed(Exception):
    def __init__(self):
        super().__init__("Execução Mal Sucedida")

class MissingParam(Exception):
    def __init__(self,parametro):
        self.element=parametro
        super().__init__(f'Faltando o parametro {self.element}, por favor verificar')

class NoParameters(Exception):
    def __init__(self):
        super().__init__("Nenhum Parametro Passado")

class NoFileLocation(Exception):
    def __init__(self):
        super().__init__("No Vector File Location")
    

class FormationError(Exception):
    def __init__(self):
        super().__init__('No arquivo passado a array "path" não tem o mesmo tamanho \
            que a Array "tables"')