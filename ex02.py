#!/usr/bin/env python

"""
En este caso se cambia uno de los pesos por lo que hay dos caminos que tienen el mismo valor lo que enloquece al solver

para eso usamos dos solvers y comparamos.

- interior point
- simplex

"""
from pprint import pprint
from scipy.optimize import linprog

from ex00 import nn2na
from ex01 import NN, beq, C, get_selected_arcs

if __name__ == '__main__':
    Aeq, arc_idxs = nn2na(NN)
    bounds = tuple([(0, None) for arcs in range(0, Aeq.shape[1])])
    C.flat[1] = 1
    for method in 'interior-point', 'simplex':
      res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds, method=method)
      print("Usando el método %s:"%method)
      pprint(res)
      print("El camino es: %s" % get_selected_arcs(arc_idxs, res.x))
