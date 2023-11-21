#definición de las clases
class Jugador:
    '''
    Definición de una clase jugador que diferenciará que tipo de jugador es:
     un humano o una máquina y que será fundamental para posteriormente seguir un 
     orden de turnos
    '''
    def __init__(self, tipo):
        self.tipo = tipo
## el tipo esta mas abajo

class Tablero:
    '''
    Definición de una clase con dos atributos:
    - Uno son las medidas del trablero
    - El segundo es la creación del propio tablero relleno con la variable agua
    '''
    def __init__(self, medida = medida_tablero):
## medida_tablero que es una variable constante
        self.medida = (medida_tablero, medida_tablero)
        
    def crear_tablero():
        return np.full((medida_tablero, medida_tablero), agua)
## crear np array y rellenado de agua donde no van a estar los barcos
    
class Barco:
    '''
    Definición de una clase barco que estará definida por el nombre, tipo de barco y las coordenadas donde estará situado
    '''
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.len = barcos[tipo][1]
        self.coordenadas = []
        
