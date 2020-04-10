#!/usr/bin/env python

"""
Dijkstra algorithmPseudocode:
# Initialize the weights:
foreach node_iin graph:
  weight(node_i) = inf
  prec[node_i] = 0
  weight(initial_node) = 0

# Iterate:
  while unexplored_nodes not empty:
    head = node with minimum weight in unexplored_nodes
    pop head node from unexplored_nodes

    foreach neighbor_iof head:
      potential_weight= weight[head] + dist[head, neighbor_i]
      if potential_weight< weight[neighbor]:
        weight[neighbor] = potential weight
        prec[neighbor] = head
"""
from functools import reduce
from pprint import pprint
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

def graph2NNplusArcs(graph):
    NN = np.where( graph > 0, 1, 0 )
    arcs = graph[graph > 0]
    #print(np.transpose(np.nonzero(NN)))

    return NN, arcs

def recorrido(prec):
    pos = len(prec) - 1
    ruta = [pos]
    while pos > 0:
        pos = (prec[pos])
        ruta.insert(0, pos)
    return ruta

def dijkstra_path(graph):
    NN, C = graph2NNplusArcs(graph)
    return dijkstra_path_NN_C(NN,C)

def get_arcs_as_tuple_list(NN):
    return [ tuple(x) for x in (np.transpose(np.nonzero(NN)).tolist())]

def dijkstra_path_NN_C(NN,C):
    weight = np.full(graph.shape[0], np.inf)
    prec = np.zeros(graph.shape[0], int)

    # relacionar arista con Cs
    arcs = get_arcs_as_tuple_list(NN)
    pesos = dict(zip(arcs, C))
    #return pesos
    # pesos = dict(enumerate(graph.flatten(), 1))#list(zip(np.transpose(np.nonzero(NN)), C))#[ (x, C[i]) for i,x in enumerate(np.transpose(np.nonzero(NN)))]

    # inicializo en 0
    weight.flat[0] = 0

    # construyo una lista de nodos
    nodes = list(range(weight.shape[0]))
    for i in range(weight.shape[0]):
        # busco el nodo con menor peso
        head = reduce(lambda y, x: x if weight[x] < weight[y] else y, nodes, nodes[0])
        # lo saco de la lista de nodos
        nodes.remove(head)
        # recorro el "vecindario"
        for v in np.where(graph[head] > 0)[0]:
            # calculo el costo de incluir este arco

            potential_weight = weight[head] + pesos[(head,v)]
            # si mejora el costo que ya había hacia el vecino, reemplazo
            if potential_weight < weight[v]:
                weight[v] = potential_weight
                prec[v] = head
    # devuelvo de manera amigable
    return recorrido(prec)

if __name__ == '__main__':
    NN, C = graph2NNplusArcs(graph)
    sol1 = dijkstra_path_NN_C(NN, C)
    sol2 = dijkstra_path(graph)
    assert sol1 == sol2
    print(sol2)