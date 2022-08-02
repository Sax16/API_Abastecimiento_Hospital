from enum import Enum

class Genero(Enum):
    """Clase género para poder restringir ingreso de datos en las columnas
    que incluyan genero

    Args:
        Enum (_type_): _description_
    """
    masculino: str = "Masculino"
    femenino: str = "Femenino"