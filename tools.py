import numpy as np

def notacion_a_indices(input):
    filas = ['1', '2', '3', '4', '5', '6', '7', '8']
    columnas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    f,c = input[1],input[0]
    posicion = [7 - filas.index(f), columnas.index(c)]
    return(posicion)


def get_direccion(move):
    if move[0] != 0 and move[1] != 0: #es movimiento en diagonal o de caballo
        direccion = np.array([int(move[0]/abs(move[0])), int(move[1]/abs(move[1]))]) #"normalizamos la direccion"; el valor absoluto del divisor es para que cuando el movimiento sea negativo, la direccion no se vuelva positiva
    else: #los demas casos posibles son con una de las dos componentes cero
        if move[0] < 0: #la primera es distinta de 0? la segunda es cero
            direccion = np.array([-1, 0]) #distinta de cero pero negativo?
        elif move[0] > 0:
            direccion = np.array([1, 0]) # o positivo? 
        elif move[1] < 0: #etc
            direccion = np.array([0, -1])
        elif move[1] > 0:
            direccion = np.array([0, 1])
    return direccion

