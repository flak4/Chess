import numpy as np
import tools
import tablero as table

game = True
white_to_move = True

chess = table.Tablero()
chess.setup()
print(chess.tablero)

while game:

    pieza = np.array(tools.notacion_a_indices(input('pieza: '))) #pregunta casilla inical

    if chess.status[pieza[0], pieza[1]] != 0: #si hay pieza
        moving_piece = chess.tablero[pieza[0], pieza[1]]
        print(type(moving_piece))

        acceso = moving_piece.getmoves() #guarda todos los movimientos de la pieza
        print(acceso)

        movimiento = np.array(tools.notacion_a_indices(input('move: '))) #pregunta casilla final

        if acceso[movimiento[0], movimiento[1]] == moving_piece.pieza:
            print('esa pieza mueve así')
            chess.is_legal(moving_piece, acceso, movimiento) #comprueba la legalidad del movimiento
        else:
            print('Esa pieza no mueve así')



        game = False
    else:
        print('no hay pieza')