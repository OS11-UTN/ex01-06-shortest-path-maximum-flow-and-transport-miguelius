#!/usr/bin/env python

"""
Shortest Path

Xi -> variable binaria paso por el arco o no.

Modelo

min c'.X
st: A x = b

l <= x <= u

Para que se balancee la entrada con la salida s = t, es decir, lo que sale de s entra en t.

-> b = [ 1 0 0 0 0 -1 ]
"""
from pprint import pprint
from scipy.optimize import linprog
import numpy as np

from ex00 import nn2na

beq = np.array([1, 0, 0, 0, 0, -1])
NN = np.array([
    # s  2  3  4  5  t
    [0, 1, 1, 0, 0, 0],  # s
    [0, 0, 0, 1, 0, 1],  # 2
    [0, 0, 0, 0, 1, 0],  # 3
    [0, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 0, 0, 1],  # 5
    [0, 0, 0, 0, 0, 0]   # t
])
C = np.array([2, 2, 2, 5, 2, 1, 2])

def get_selected_arcs(arc_idxs, selected_arcs):
    arc = []
    for idx, i in enumerate(selected_arcs):
        if round(i) == 1:
            arc.append(arc_idxs[idx])
    return arc

if __name__ == '__main__':
    Aeq, arc_idxs = nn2na(NN)
    bounds = tuple([(0, None) for arcs in range(0, Aeq.shape[1])])

    res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds)
    pprint(res)
    print("El camino es: %s"%get_selected_arcs(arc_idxs, res.x))
