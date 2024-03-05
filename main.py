import numpy as np
import tools
import tablero as table

game = True
white_to_move = True

chess = table.Tablero()
chess.setup() #se inician los dos tableros (obj y num) para las piezas incluidas en la lista de piezas de config
print(chess.tablero)

while game:

    pieza = np.array(tools.notacion_a_indices(input('pieza: '))) #pregunta casilla inical

    if chess.status[pieza[0], pieza[1]] != 0: #si hay pieza

        moving_piece = chess.tablero[pieza[0], pieza[1]]

        acceso = moving_piece.getmoves() #tablero con los movimientos de la pieza
        datos = acceso + chess.status #tablero con más informacion a parte de los movimientos
        print(datos)

        movimiento = np.array(tools.notacion_a_indices(input('move: '))) #pregunta casilla final y la convierte a indices de array

        if acceso[movimiento[0], movimiento[1]] == moving_piece.pieza: #es un movimiento posible para esa pieza?
            print(chess.is_legal(moving_piece, datos, movimiento)) #comprueba la legalidad del movimiento
        else:
            print('Esa pieza no mueve así') #y el programa se acaba



        game = False
    else:
        print('no hay pieza')