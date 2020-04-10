"""
Ford-Fulkerson algorithm

Pseudocode:

residual_G = G for all edges(u, v) and 0 for all edges (v, u)

path = perform DFS(source, sink) to find an augmenting path

while path exists:
  for each edge in path:
    residual_G(v, u) = flow(v, u) + path max_capacity
    residual_G(u, v) = flow(u, v) - path max_capacity

  path = perform DFS(source, sink)
"""
from ex03 import graph2NNplusArcs, get_arcs_as_tuple_list
import numpy as np

graph = np.array([
   # s  2  3  4  5  t
    [0, 2, 2, 0, 0, 0],  # s
    [0, 0, 0, 2, 0, 5],  # 2
    [0, 0, 0, 0, 2, 0],  # 3
    [0, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 0, 0, 2],  # 5
    [0, 0, 0, 0, 0, 0]   # t
])

def max_capacity(path):
    map(lambda x: )
    return np.min(path)


def DFS(param, param1):
    return []

if __name__ == '__main__':
  NN, C = graph2NNplusArcs(graph)
  arcs = get_arcs_as_tuple_list(NN)
  residual_g = np.zeros(NN.shape)
  flow = graph
  path = DFS(0, 5)

  while len(path) > 0:
    # minimo flujo
    path_max_capacity = max_capacity(path)

    for e in path:
      u = e[0]
      v = e[1]
      residual_g[u][v] = flow[u][v] - max_capacity(path)
    path = DFS(0, 5)

  print("Falta el implementador de rutas")