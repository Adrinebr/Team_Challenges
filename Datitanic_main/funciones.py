import clases as cl
import numpy as np
import random 
import variables as var


def disparo(jugador: cl.Jugador, tablero: cl.Tablero): #función para declarar un disparo
    if jugador.tipo == "Humano":
        while True:#Bucle para cerciorarse de que las coords están dentro del tablero
            while True:#Bucle para cerciorarse de que las coordenadas escritas tienen sentido dentro de la lógica del juego
                try:
                    fila, col = [int(coord) for coord in input("Por favor, escribe unas coordenadas (separadas por un espacio) para poder disparar ->").split()]
                    break #salida del segundo while
                except ValueError:
                    print("Es posible que usted haya incorporado una coma o otra simbolo para separar las coordenadas. Por favor, vuelve a intentar de nuevo con coordenadas entre 0 y 9, sepradas por un espacio")
            if (fila < 0 or fila > 9) or (col < 0 or col > 9):
                print("Las coordenadas introducidas están fuera del tablero","\n")
            else:
                break #salida del primer while
                
    else: #disparo aleatorio de la máquina
        fila = random.randint(0,var.medida_tablero-1)
        col = random.randint(0,var.medida_tablero-1)
    
    if tablero[fila, col] == var.barco: ##se aplica a los 2 tipos de jugador
        print("BINGO: BARCO TOCADO", "\n")
        tablero[fila, col] = var.barco_tocado #Barco tocado será representado con X en dicha fila y columna
        if var.barco not in var.barco:#Si no hay más barcos sobre el tablero que declare el final del juego y el ganador
            fin_juego()
        #Si no, y hay barcos todavía, sigue la partida
        disparo(jugador, tablero)
        
    elif tablero[fila, col] == var.agua: #Disparo al mar
        print("El Disparo se ha caido en el agua", "\n")
        tablero[fila, col] = var.disparo_al_mar
        
    elif tablero[fila, col] == var.barco_tocado or tablero[fila, col] == var.disparo_al_mar:
        print("Ya has disparado en estas coordenadas! Un poco de concentracion please", "\n")
        disparo(jugador, tablero)
        
def menu(): #función que declara un menú para que el jugador humano decida qué hacer durante su turno
    print("Opciones de juego:", "\n",
          "1. Disparar", "\n",
          "2. Mirar tu tablero", "\n",
          "3. Mirar tablero rival(intentar no mirar)", "\n",
          "4. Mirar tablero visible de mis attaques", "\n",
          "5. Exit")
    
def fin_juego(tablero1: cl.Tablero, tablero2: cl.Tablero):#función para declarar cuándo el juego ha terminado(es decir, si hay barcos en el tablero del jugador humano, significa que ha ganado la partida, si no es que ha ganado la máquina)
    if var.barco in tablero1:
        print("Enhorabuena! Has ganado", "\n")
        exit() 
    else:
        print("Lo siento. Has perdido", "\n")
        exit() 
        
def exit():
    print("Gracias por haber jugado conmigo. Hasta la proxima.")

def crear_flota(tablero: cl.Tablero):
    flota = []
    for i in var.barcos.keys():
        for num in range(var.barcos[i][0]): 
            barco_nuevo = cl.Barco(i + str(num), i) ## str(num) porque solo se puede concatenate str juntos y no str y int\n
            situar_barco(barco_nuevo, tablero)
            flota.append(barco_nuevo)
    return flota

def situar_barco(bote: cl.Barco, tablero: cl.Tablero):
    situado = False    
    while not situado:
        fila = random.randint(0,var.medida_tablero-1)
        col = random.randint(0,var.medida_tablero-1)
        orientacion = random.choice(var.orientaciones)

        if tablero[fila, col] == var.agua:
            if orientacion == 'N':
                if fila - (bote.len - 1) < 0:
                    ## No hay sitio para poner el barco, asi que situado sigue devolviendo False y el bucle vuelve a empezar y asigna otra orientacion
                    continue
                else: #comprobar si el barco puede situarse
                    for celda in range(bote.len):
                        if tablero[fila-celda, col] == var.agua: # aqui es decir si las filas son aguas (entonces no hay barcos tampoco)
                            situado = True
                            continue
                        else:
                            situado = False
                            break #Si puede situarse, el barco se coloca y salir del bucle
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila-celda, col] = var.barco
                            bote.coordenadas.append([fila-celda, col]) 
                        break
                    
            elif orientacion == 'E':
                
                if col + (bote.len -1) > var.medida_tablero-1:
                    continue
                else:
                    for celda in range(bote.len):
                        if tablero[fila, col+celda] == var.agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila, col+celda] = var.barco
                            bote.coordenadas.append([fila, col+celda]) 
                        break
                    
            if orientacion == 'S':
                
                if fila + (bote.len -1) > var.medida_tablero-1:
                    continue
                else:
                    for celda in range(bote.len):
                        if tablero[fila+celda, col] == var.agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila+celda, col] = var.barco
                            bote.coordenadas.append([fila+celda, col]) 
                        break

            elif orientacion == 'W':
                
                if col - (bote.len -1) < 0:
                    continue
                else:
                    for celda in range(bote.len):
                        if tablero[fila, col-celda] == var.agua:
                            situado = True
                            continue
                        else:
                            situado = False
                            break
                    if situado == True:
                        for celda in range(bote.len):
                            tablero[fila, col-celda] = var.barco
                            bote.coordenadas.append([fila, col-celda]) 
                        break
