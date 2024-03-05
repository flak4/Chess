import numpy as np
import tools
import pieces as p


#PIEZAS DEL JUEGO DEFINIDAS:
torre_1 = p.Torre('w', 4, 'a1')
torre_2 = p.Torre('w', 4, 'h1')
torre_3 = p.Torre('b', 4, 'a8')
torre_4 = p.Torre('b', 4, 'h8')

alfil_1 = p.Alfil('w', 5, 'c1')
alfil_2 = p.Alfil('w', 5, 'f1')
alfil_3 = p.Alfil('b', 5, 'c8')
alfil_4 = p.Alfil('b', 5, 'f8')

caballo_1 = p.Caballo('w', 6, 'b1')
caballo_2 = p.Caballo('w', 6, 'g1')
caballo_3 = p.Caballo('b', 6, 'b8')
caballo_4 = p.Caballo('b', 6, 'g8')

reina_1 = p.Reina('w', 3, 'e4')
reina_2 = p.Reina('b', 3, 'd8')

rey_1 = p.Rey('w', 2, 'e1')
rey_2 = p.Rey('b', 2, 'e8')

peon_1 = p.Peon('w', 1, 'a2')
peon_2 = p.Peon('w', 1, 'b2')
peon_3 = p.Peon('w', 1, 'c2')
peon_4 = p.Peon('w', 1, 'd2')
peon_5 = p.Peon('w', 1, 'e6')
peon_6 = p.Peon('w', 1, 'f2')
peon_7 = p.Peon('w', 1, 'g2')
peon_8 = p.Peon('w', 1, 'h2')
peon_9 = p.Peon('b', 1, 'a7')
peon_10 = p.Peon('b', 1, 'b7')
peon_11 = p.Peon('b', 1, 'c7')
peon_12 = p.Peon('b', 1, 'e2')
peon_13 = p.Peon('b', 1, 'e7')
peon_14 = p.Peon('b', 1, 'f7')
peon_15 = p.Peon('b', 1, 'g7')
peon_16 = p.Peon('b', 1, 'h7')

#SET INICIAL DE PIEZAS (Tablero.setup() toma esta lista como argumento)
piezas = [reina_1, peon_5, peon_12]