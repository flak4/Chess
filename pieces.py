import numpy as np
import tools

color_to_meth = {'w' : -1, 'b' : 1}
salida_cond = {'w' : 6, 'b' : 1}

class Pieza:
    def __init__(self, color, pieza, posicion):
        self.pieza = pieza
        self.color = color
        self.posicion = np.array(tools.notacion_a_indices(posicion))
    
    def getmoves(self):
        movimientos = np.zeros((8,8))
        if type(self) == Peon:
            for m in self.movimientos:
                if np.array_equal(m,np.array([2*color_to_meth.get(self.color),0])) and self.posicion[0] == salida_cond.get(self.color):
                    coord = self.posicion + m
                    if np.all(0 <= coord) and np.all(coord < 8):
                        movimientos[coord[0], coord[1]] = self.pieza

                elif not np.array_equal(m,np.array([2*color_to_meth.get(self.color),0])):
                    coord = self.posicion + m
                    if np.all(0 <= coord) and np.all(coord < 8):
                        movimientos[coord[0], coord[1]] = self.pieza
        else: 
            for m in self.movimientos:
                coord = self.posicion + m
                while np.all(0 <= coord) and np.all(coord < 8):
                    movimientos[coord[0], coord[1]] = self.pieza
                    if type(self) == Rey or type(self) == Caballo:
                        break
                    else:
                        coord = coord + m
        return movimientos

class Alfil(Pieza):
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
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

class Peon(Pieza):
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
        self.movimientos = [np.array([color_to_meth.get(self.color),0]), np.array([2*color_to_meth.get(self.color),0]), np.array([color_to_meth.get(self.color),1]), np.array([color_to_meth.get(self.color),-1])]

class Caballo(Pieza):
    def __init__(self, color, pieza, posicion):
        super().__init__(color, pieza, posicion)
        self.movimientos = [np.array([2,1]), np.array([2,-1]), np.array([-2,1]), np.array([-2,-1]), np.array([1,2]), np.array([1,-2]), np.array([-1,2]), np.array([-1,-2])]