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

def max_capacity(path, quedan):
    # map(lambda x: )
    return np.min(path)

def ruta(arcos, s, t, arcos2):
    if (s == t):
        return arcos2
    for a in arcos:
        if a[0] != s:
            continue
        if a not in arcos2:
            arcos_extendido = ruta(arcos, a[1], t, arcos2)
            if arcos_extendido != None:
                arcos2.append(a)
                return arcos_extendido
    return None

def DFS(arcs, s, t):
    arcos = ruta(arcs, s, t, [])
    if arcos: arcos.reverse()
    return arcos

if __name__ == '__main__':
  NN, C = graph2NNplusArcs(graph)
  arcs = get_arcs_as_tuple_list(NN)
  residual_g = np.zeros(NN.shape)
  quedan = C
  flow = graph
  path = DFS(arcs, 0, 5)
  print(path)

  while path:
    # minimo flujo
    path_max_capacity = max_capacity(path, quedan)
    path = None
    """
    for e in path:
      u = e[0]
      v = e[1]
      residual_g[u][v] = flow[u][v] - max_capacity(path)
      residual_g[v][u] = flow[v][u] + max_capacity(path)
    path = DFS(arcs, 0, 5)
    """
  print("Falta el implementador de rutas")
