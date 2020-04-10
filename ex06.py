from pprint import pprint
from scipy.optimize import linprog
import numpy as np

from ex00 import nn2na
from ex01 import get_selected_arcs
from ex03 import get_arcs_as_tuple_list

beq = np.array([10, 20, 15, -25, -20])
NN = np.array([
   # 1  2  3  4  5
    [0, 0, 0, 1, 1],  # 1
    [0, 0, 0, 1, 1],  # 2
    [0, 0, 0, 1, 1],  # 3
    [0, 0, 0, 0, 0],  # 4
    [0, 0, 0, 0, 0]   # 5
])
C = np.array([10, 20, 10, 10, 10, 30])

node_names = ['1', '2', '3', 'a', 'b']

if __name__ == '__main__':
    Aeq, arc_idxs = nn2na(NN)
    bounds = tuple([(0, None) for arcs in range(0, Aeq.shape[1])])

    res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds)

    print(f"The total cost is: {res.fun:0.2f}")
    arcs = [(node_names[x[0]], node_names[x[1]]) for x in get_arcs_as_tuple_list(NN)]
    usage = dict(zip(arcs, np.round(res.x)))

    print("## Results ##")
    print(f"The channel use is: {usage}")
    print(f"The total cost is: {res.fun:0.2f}")
