import funciones as fun
import numpy as np
import random
import variables as var

class Tablero():
    def __init__(self, dimension, barcos=[]):
        self.dimension = dimension
        self.matrix = np.full((dimension,dimension), var.AGUA_SIMB)
        self.barcos = barcos

    def casilla_random(self):
        fila_random = random.randint(0,9)
        columna_random = random.randint(0,9)
        casilla_random = (fila_random, columna_random)
        return casilla_random


    def generar_b_aleatorio(self):
        
        for barcos_prop in var.LISTA_BARCOS:
            contador = 0
            while contador < barcos_prop [1]:
                posicion = self.casilla_random()
                fila = self.casilla_random()[0]
                columna = self.casilla_random()[1]

                orien_norte = self.matrix[fila: fila - barcos_prop[0]:-1, columna]
                orien_sur = self.matrix[fila: fila + barcos_prop[0], columna]
                orien_oeste = self.matrix[fila, columna:columna - barcos_prop[0]:-1]
                orien_este = self.matrix[fila, columna: columna + barcos_prop[0]]

                if var.BARCO_SIMB not in orien_norte and len(orien_norte) == barcos_prop[0]:
                    self.matrix[fila: fila - barcos_prop[0]: -1, columna] = var.BARCO_SIMB
                    contador += 1
                elif var.BARCO_SIMB not in orien_sur and len(orien_sur) == barcos_prop[0]:
                    self.matrix[fila: fila + barcos_prop[0], columna] = var.BARCO_SIMB
                    contador += 1
                elif var.BARCO_SIMB not in orien_oeste and len(orien_oeste) == barcos_prop[0]:
                    self.matrix[fila, columna:columna - barcos_prop[0]:-1] = var.BARCO_SIMB
                    contador += 1
                elif var.BARCO_SIMB not in orien_este and len(orien_este) == barcos_prop[0]:
                    self.matrix[fila, columna: columna + barcos_prop[0]] = var.BARCO_SIMB
                    contador += 1

        
    def mostrar_tablero(self):

        return self.matrix

    def colocar_barco(self, barco):
        fila = barco.posicion[0] - 1
        columna = var.coord_letras.index(barco.posicion[1])

        if barco.axis == 0:
            self.matrix[fila: barco.eslora + fila, columna] = var.BARCO_SIMB
        else:
            self.matrix[fila, columna: barco.eslora + columna] = var.BARCO_SIMB

    def colocar_barcos(self):
        for barco in self.barcos:
            self.colocar_barco(barco)


class Jugador():
    
    def __init__(self):
        self.tablero_barcos = Tablero(10)
        self.tablero_barcos.generar_b_aleatorio()
        self.tablero_disparos = Tablero(10)
        self.vidas = 20
        self.disparos = []

    def muestra_tablero(self):
        eje_x = np.array(var.LISTA_EJE_X)
        print("  ",eje_x, "           ",eje_x,"\n")
        for i in range(len(var.LISTA_EJE_Y)):
            if i!= 9:
                eje_y = str(var.LISTA_EJE_Y[i]) + " "
            else:
                eje_y = str(var.LISTA_EJE_Y[i])

            print(eje_y, self.tablero_barcos.matrix[i],
            "        ", eje_y, self.tablero_disparos.matrix[i])
    
    def disparar(self, posicion, objetivo):

        self.disparos.append(posicion)

        posicion_interpretada = self.interpretar_posicion(posicion)

        if objetivo.tablero_barcos.matrix[posicion_interpretada[0], posicion_interpretada[1]] == var.BARCO_SIMB:
            self.tablero_disparos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.TOCADO_SIMB
            objetivo.tablero_barcos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.TOCADO_SIMB
            objetivo.vidas -= 1
            return True
        else:
            self.tablero_disparos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.FALLAR_SIMB
            objetivo.tablero_barcos.matrix[posicion_interpretada[0], posicion_interpretada[1]] = var.FALLAR_SIMB
            return False

    def interpretar_posicion(self, posicion):
        fila = posicion[0] - 1
        columna = var.LISTA_EJE_X.index((posicion[1]))

        return (fila, columna)