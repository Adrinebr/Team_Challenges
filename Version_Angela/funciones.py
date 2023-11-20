import numpy as np
import random
import uuid
import variables as var

def crea_tablero(lado): 
    tablero = np.full(lado,lado, " ")
    print(tablero)
    return tablero
 
def coloca_barco(tablero,barco):
    for pieza in barco:
        tablero[pieza] = "O"
    return tablero

def coloca_barco_aleatorio(tablero, barcos): 
    ''' 
    Hay que modificar la función para que incluya los 10 barcos que queremos. 
    Antes del while, incluir un for que recorra los barcos definidos
    '''
    num_filas = tablero.shape[0]
    num_columnas = tablero.shape[1]
    for eslora in var.lista_barcos: # Hacer la lista un objeto más "sofisticado"
        while True:
            orientacion = random.choice(var.orientaciones)
            origen = (random.randint(0,num_filas-1), random.randint(0,num_columnas -1))
            fila = origen[0]
            columna = origen[1]
            barco_temp = []
            if tablero[origen] != "O" and tablero[origen] != "X": 
                barco_temp.append(origen)
                for i in range(eslora - 1):
                    if orientacion == "N":
                        fila -= 1
                    elif orientacion == "S":
                        fila += 1
                    elif orientacion == "E":
                        columna += 1
                    else:
                        columna -= 1
                    if fila >= num_filas or fila < 0:
                        print("Me salgo del tablero")
                        break
                    elif columna >= num_columnas or columna <0:
                        print("Me salgo del tablero")
                        break
                    elif tablero[fila,columna] == "O":
                        print("Me encontré un barco")
                        break
                    elif tablero[fila, columna] == "X":
                        print("Me encontré un barco")
                        break
                    barco_temp.append((fila,columna))

                if len(barco_temp) != eslora:
                    continue
                else:
                    coloca_barco(tablero, barco_temp)
                    break 
            else:
                continue

def dispara(tablero, coordenada):
    if tablero[coordenada] == "O":
        tablero[coordenada] = "X"
        print("Tocado")
    elif tablero[coordenada] == "X":
        print("Ya habías disparado a este punto")
    else:
        tablero[coordenada] = "-"
        print("Agua")

def generar_id_jugador ():
    id_jugador = str(uuid.uuid1())[:8]
    return id_jugador