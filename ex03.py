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


NN = np.array([
   # s  2  3  4  5  t
    [0, 2, 2, 0, 0, 0],  # s
    [0, 0, 0, 2, 0, 5],  # 2
    [0, 0, 0, 0, 2, 0],  # 3
    [0, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 0, 0, 2],  # 5
    [0, 0, 0, 0, 0, 0]   # t
])

def recorrido(prec):
    ruta = [len(prec) - 1]
    pos = len(prec) - 1
    while pos > 0:
        pos = (prec[pos])
        ruta.insert(0, pos)
    return ruta

def dijkstra_path(graph):
    weight = np.full(graph.shape[0], np.inf)
    prec = np.zeros(graph.shape[0], int)

    # inicializo en 0
    weight.flat[0] = 0

    # construyo una lista de nodos
    nodes = list(range(weight.shape[0]))
    for i in range(weight.shape[0]):
        # busco el nodo con menor peso
        head = reduce(lambda y, x: x if weight.flat[x] < weight.flat[y] else y, nodes, nodes[0])
        # lo saco de la lista de nodos
        nodes.remove(head)
        #
        for v in np.where(graph[head] > 0)[0]:
            potential_weight = weight[head] + graph[head][v]
            if potential_weight < weight[v]:
                weight[v] = potential_weight
                prec[v] = head
    return recorrido(prec)

if __name__ == '__main__':
    pprint(dijkstra_path(NN))