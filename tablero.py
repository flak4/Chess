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
            self.tablero[p.posicion[0], p.posicion[1]] = p
            self.status[p.posicion[0], p.posicion[1]] = int(p.pieza)
    

    def is_legal(self, pieza, casillas_accesibles, casilla1):
        movimiento = casilla1 - pieza.posicion
        print(f'movimiento: {movimiento}')
        direccion0,direccion1 = tools.get_direccion(movimiento)
        print(f'dir: {tools.get_direccion(movimiento)}')
    
        i1, i0 = max(int(pieza.posicion[0]), int(casilla1[0])), min(int(pieza.posicion[0]), int(casilla1[0])) 
        j1, j0 = max(int(pieza.posicion[1]), int(casilla1[1])), min(int(pieza.posicion[1]), int(casilla1[1]))

        submatrix = np.diag(np.fliplr(casillas_accesibles),k=-1)
    
        print(f'subd: {submatrix}')

'''
        if np.array_equal(dir, np.array([1,1])):
            #print(np.fliplr(submatrix)) #gira con respecto la horizontal
            camino = np.diag(np.fliplr(submatrix))
            if np.all(camino != 0):
                print(camino)
                print('bien')
            else:
                print('puede no ser legal')

        elif np.array_equal(dir, np.array([1,0])):
            print('caso2')

        elif np.array_equal(dir, np.array([0,1])):
            print('caso3')

        #para vectores columna (dir = [1,0])
        #print(submatrix[i0+1:i1]) 

'''


