import numpy as np
import tools

color_to_meth = {'w' : -1, 'b' : 1}
salida_cond = {'w' : 6, 'b' : 1} #fila en la que tienen que estar los peones para poder mover dos casillas

class Pieza: #clase principal pieza
    def __init__(self, color, pieza, posicion): #una pieza se caracteriza por un color, el tipo y la posición que ocupa
        self.pieza = pieza
        self.color = color
        self.posicion = np.array(tools.notacion_a_indices(posicion))
    
    def getmoves(self): #metodo para obtener los movimientos
        movimientos = np.zeros((8,8))
        if type(self) == Peon: #todo este if es solo para los peones
            for m in self.movimientos:
                if np.array_equal(m,np.array([2*color_to_meth.get(self.color),0])) and self.posicion[0] == salida_cond.get(self.color): #peones moviendo dos casillas
                    coord = self.posicion + m
                    if np.all(0 <= coord) and np.all(coord < 8): #esto puede ser que sobre porque por las condiciones y el tipo de movimiento no debería poder salirse del tablero, pero bueno
                        movimientos[coord[0], coord[1]] = self.pieza

                elif not np.array_equal(m,np.array([2*color_to_meth.get(self.color),0])): #si no es mover dos es mover uno
                    coord = self.posicion + m
                    if np.all(0 <= coord) and np.all(coord < 8):
                        movimientos[coord[0], coord[1]] = self.pieza #y nada mas porque son peones
        else: #aqui entran las demas piezas
            for m in self.movimientos:
                coord = self.posicion + m
                while np.all(0 <= coord) and np.all(coord < 8):
                    movimientos[coord[0], coord[1]] = self.pieza #se añade el primero
                    if type(self) == Rey or type(self) == Caballo: #estas dos solo tienen "1 movimiento de rango"
                        break
                    else:
                        coord = coord + m #para alfil, torre y dama sigue hasta topar con los bordes del tablero
        return movimientos

'''
La idea de la clase Pieza era reutilizar el codigo lo más que se pudiera, pues todas las piezas se definen mediante los mismos parametros
asi solo hay que añadirle a cada pieza sus movimientos característicos (tanto el construtor como la funcion getmoves() se escriben una sola vez en el codigo y no para todas las piezas)
Igualmente hay que revisitar esta "clasificacion" porque los movimientos de los peones se calculan separados de los demás porque tienen
condiciones especiales (igual que pasa con el rey)
'''
class Alfil(Pieza): #poniendo la clase Pieza ahi indicamos que Alfil es una clase derivada de Pieza (Pieza es la "clase padre")
    def __init__(self, color, pieza, posicion): #este es el constructor de la clase alfil
        super().__init__(color, pieza, posicion) #que llama al constructor de la clase Pieza usando super()
        self.movimientos = [np.array([1, 1]), np.array([-1, 1]), np.array([1, -1]), np.array([-1, -1])]

class Torre(Pieza):
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
        self.movimientos = [np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1])]

class Reina(Pieza):
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
        self.movimientos = [np.array([1, 1]), np.array([-1, 1]), np.array([1, -1]), np.array([-1, -1]),
                            np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1])]
        
class Rey(Pieza):
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
        self.movimientos = [np.array([1, 1]), np.array([-1, 1]), np.array([1, -1]), np.array([-1, -1]),
                            np.array([1, 0]), np.array([0, 1]), np.array([-1, 0]), np.array([0, -1])]

class Peon(Pieza): #Creo que si dentro de esta clase definimos un metodo getmoves() sobreescribiría el de la clase pieza, para más info whatsapp
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
        self.movimientos = [np.array([color_to_meth.get(self.color),0]), np.array([2*color_to_meth.get(self.color),0]), np.array([color_to_meth.get(self.color),1]), np.array([color_to_meth.get(self.color),-1])]

class Caballo(Pieza):
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
        self.movimientos = [np.array([2,1]), np.array([2,-1]), np.array([-2,1]), np.array([-2,-1]), np.array([1,2]), np.array([1,-2]), np.array([-1,2]), np.array([-1,-2])]