from pprint import pprint
from scipy.optimize import linprog
import numpy as np

from ex00 import nn2na

beq = np.array([0, 0, 0, 0, 0, 0])
max_q = [7, 1, 2, 3, 2, 1, 2, None]
NN = np.array([
    # s  2  3  4  5  t
    [0, 1, 1, 0, 0, 0],  # s
    [0, 0, 0, 1, 0, 1],  # 2
    [0, 0, 0, 0, 1, 0],  # 3
    [0, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 0, 0, 1],  # 5
    [1, 0, 0, 0, 0, 0]   # t
])

def get_selected_arcs(arc_idxs, selected_arcs):
    arc = []
    for idx, i in enumerate(selected_arcs):
        if round(i) == 1:
            arc.append(arc_idxs[idx])
    return arc


def get_usage(arc_idxs, use, max_flow):
    return  ["%s -> %d / %s"%(x, use[i], max_flow[i]) for i,x in enumerate(arc_idxs)]

def min_cut(arc_idxs, use, max_flow):
    return list(filter(lambda x: x is not None, [ x if max_flow[i] != None and np.isclose(use[i], max_flow[i]) == [True]  else None for i,x in enumerate(arc_idxs)]))


if __name__ == '__main__':
    Aeq, arc_idxs = nn2na(NN)
    bounds = tuple([(0, max_q[arcs]) for arcs in range(0, Aeq.shape[1])])
    C = np.zeros(len(bounds))
    C[-1] = -1

    res = linprog(C, A_eq=Aeq, b_eq=beq, bounds=bounds)
    pprint(res)

    usage = get_usage(arc_idxs, res.x.astype(int), max_q)
    min_cut = min_cut(arc_idxs, res.x, np.array(max_q))
    max_flow = - res.fun
    print("## Results ##")
    print("Usage: (from,to) -> used/max: %s"% usage)
    print("Min arcs to be cut to cut: (from,to) %s"% min_cut)
    print("Max flow: %0.2f"% max_flow)