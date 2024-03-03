import numpy as np

def notacion_a_indices(input):
    filas = ['1', '2', '3', '4', '5', '6', '7', '8']
    columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    f,c = input[1],input[0]
    posicion = [7 - filas.index(f), columnas.index(c)]
    return(posicion)


def get_direccion(move):
    if move[0] != 0 and move[1] != 0:
        dir = np.array([int(move[0]/abs(move[0])), int(move[1]/abs(move[1]))])
    else:
        if move[0] < 0:
            dir = np.array([-1, 0])
        elif move[0] > 0:
            dir = np.array([1, 0])
        elif move[1] < 0: 
            dir = np.array([0, -1])
        elif move[1] > 0:
            dir = np.array([0, 1])
    return dir

