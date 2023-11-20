import funciones as fun
import numpy as np
import random
import variables as var

class Tablero: 
    def __init__(self, lado, barcos, id_usuario):
        self.lado = lado
        self.barcos = barcos
        self.id = id_usuario
    def crea_tablero (lado):
        fun.crea_tablero(var.lado)
    


class Jugador:
        
    def __init__ (self,id_jugador):    
        self.id = id_jugador

    def generar_id_aleatorio(self,id_jugador): 
        fun.generar_id_jugador()

   
class Barco: 
    def __init__(self, eslora, orientacion, coord_inicial):
        self.eslora = eslora
        self.orientacion = orientacion
        self.coord_inicial = coord_inicial

    def barco_aleatorio (self)