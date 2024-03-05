import numpy as np
import config
import tools

class Tablero():
    def __init__(self):
        self.tablero = np.zeros((8,8), dtype=object)
        self.status = np.zeros((8,8)) #igual que tablero pero con los valores numericos de las piezas
        self.movimientos = []
        self.game = True
        self.white2play = True

    def setup(self, piezas=config.piezas):
        for p in piezas:
            self.tablero[p.posicion[0], p.posicion[1]] = p #un tablero de objetos
            self.status[p.posicion[0], p.posicion[1]] = int(p.pieza) #un tablero de números
    

    def is_legal(self, pieza, casillas_accesibles, casilla1): #pieza es un objeto, casillas accesibles en un futuro debe contener información de los jaques y demas vainas
        movimiento = casilla1 - pieza.posicion
        direccion = tools.get_direccion(movimiento) #vemos en que dirección tenemos que comprobar el movimiento
        x = pieza.posicion #inicializamos la casilla para las iteraciones
        legal = True
        while not np.array_equal(x, casilla1): #i.e., x no es la casilla a la que queremos mover
            x = x + direccion #vemos la siguiente casilla
            if casillas_accesibles[x[0], x[1]] == pieza.pieza: #casillas_accesibles es el tablero de movimientos de la pieza + el tablero de posiciones (será igual a .pieza si la casilla está vacía) 
                continue #vemos la siguiente
            else: #por el motivo que sea, no es una casilla accesible directamente (captura o pieza aliada)
                legal = False 
                break
            #futura implementacion: una vez decidido codigo de numeros estaría que por ejemplo, casilla = 4 ==> captura (es legal por lo que se añade), elif casilla = 2 ==> pieza aliada (ilegal)
        return legal
                



