# Datitanic

![image](https://github.com/Adrinebr/Datitanic/assets/147253096/7358c0c8-8645-4cdc-b860-2130a9476311)
### Autores
* [Adrián Nebril](https://github.com/Adrinebr)
* [Samuel Seuru](https://github.com/SamuelSeuru)
* [Ángela López](https://github.com/AngelaLM14)



**Primer proyecto por equipos para el Bootcamp de Data Science.**

Hemos desarrollado el juego de *Hundir la Flota* utilizando Programación Orientada a Objetos en Python. 

### Liberías
* Numpy
* Random

## El proyecto está estructurado en 4 ficheros .py:

#### Main

En este archivo se ejecuta el programa del juego.

#### Variables
* agua
* barco
* barco_tocado
* disparo_al_mar
* medida_tablero
* orientaciones
* barcos

#### Funciones
* **disparo** - Utiliza como argumentos las coordenadas del disparo y comprueba si hay agua, barco o ya se ha disparado a ese punto.
* **menu** - Muestra las opciones de juego: Disparar, mirar tu tablero, el tablero del rival y salir del juego.
* **fin_juego** - Declara cuándo termina el juego. Es decir, si hay barcos en el tablero del jugador humano, significa que ha ganado la partida. Si no, habrá ganado la máquina.
* **exit** - Permite terminar el juego antes de que uno de los dos jugadores gane.
* **crear_flota** - Crea todos los barcos para cada jugador
* **situar_barco** - Sitúa los barcos de la flota de manera aleatoria en el tablero de cada jugador

#### Clases
* **Jugador** - Esta clase diferencia si el jugador es humano o máquina
* **Tablero** - Clase con el atributo *medidas_del_tablero* y el método *crear_tablero* que genera un tablero de las medidas indicadas lleno de la variable *agua*
* **Barco** - Esta clase define el tipo de barco (su tamaño) y las coordenadas en las que se sitúa

