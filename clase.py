import funciones as fun
import numpy as np
import uuid as uuid
import variables as var
class tablero: 
    dimensiones = [var.lado, var.lado]
    def __init__ (self,dimensiones,id_jugador,barcos=[]):
        self.dimensiones = dimensiones
        self.barcos = barcos
        self.id = id_jugador

    def crear_tablero(self): #Esta funcion debe crearse en funciones.py e importarse 
        tablero = np.full([self.dimensiones,self.dimensiones]," ")
        print(tablero)
        return tablero
        
    def asignar_id (self):
        id_jugador = str(uuid.uuid1())
        id_jugador = str(np.random.randint(0,9,6))

    def colocar_barco_random(self):
# Durante el desarrollo queremos poder verlo para comprobar que se está ejecutando ok, cuando iniciemos el juego incluiermos un argumento 
# como mostrar_contrincante = False para que no se vea
        print(tablero_actual) 
        return tablero_actual
        

    def colocar_barco_jugador(self, barcos, colocar_barco):

        print(tablero_actual)
        return tablero_actual

    def disparar (self):


class Barco: 
    def __init__ (self, eslora, n_barcos, n_impactos, posicion, orientacion):
        self.eslora = eslora
        self.n_barcos = n_barcos
        self.posicion = posicion
        self.n_impactos = n_impactos
        self.orientacion = orientacion

    


id_jugadores =
tablero = np.full((lado, lado), ' ')
barcos = 
tablero_sin_barcos = 
disparo
colocar_barco
