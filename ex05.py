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

NN = np.array([                            # el grafo
    # s  2  3  4  5  t
    [0, 1, 1, 0, 0, 0],  # s
    [0, 0, 0, 1, 0, 1],  # 2
    [0, 0, 0, 0, 1, 0],  # 3
    [0, 0, 0, 0, 0, 1],  # 4
    [0, 0, 0, 0, 0, 1],  # 5
    [0, 0, 0, 0, 0, 0]   # t
])

C = [7, 1, 2, 3, 2, 1, 2]                  # la capacidad de cada arco

"""
  dada una ruta devuelve 
"""
def max_capacity(arcos, ruta, capacidad_disponible):
    a = ruta[0]                                            # tomo el primero
    max_capac = capacidad_disponible[arcos.index(a)]       # maximo como capacidad maxima
    for i in range(1, len(ruta)):
        a = ruta[i]
        nuevo = capacidad_disponible[arcos.index(a)]
        #print("%i -> %s: %d"%(arcos.index(a), a,nuevo))
        if nuevo < max_capac:                              # si se reduce
            max_capac = nuevo
    return max_capac

"""
Recursion para buscar rutas
si llegue 
  corto
si no 
  busco en vecinos hasta que me quedo sin vecinos recursivamente
sino 
  devuelvo vacio None.
"""
def ruta(todos_los_arcos, s, t, la_ruta):
    if (s == t):                         # corete de la iteracion
        return la_ruta
    for a in todos_los_arcos:
        if a[0] != s:                    # solo los vecinos de este vértice
            continue
        if a not in la_ruta:             # evita ciclos
            arcos_extendido = ruta(todos_los_arcos, a[1], t, la_ruta)
            if arcos_extendido != None:  # si devuelve algo
                la_ruta.insert(0, a)     #  inserto al pcpio
                return arcos_extendido   #  devuelvo la ruta con el arco extra
    return None

"""
  Búsqueda depth first de rutas entre dos vertices s y t
"""
def DFS(arcs, s, t):
    arcos = ruta(arcs, s, t, [])
    return arcos

if __name__ == '__main__':
  arcs = get_arcs_as_tuple_list(NN)          # busco los arcos del grafo
  quedan = [q for q in C]                    # residuo de cada arco
  arcos_restantes = [a for a in arcs]        # arcos restantes

  flujo = 0                                  # inicializo las variables de respuesta
  min_cut = []
  uso = np.zeros(len(C),int)                 # cuanto use en cada arco

  path = DFS(arcos_restantes, 0, 5)          # busco la primera ruta
  while path:
    capacidad_usada = max_capacity(arcs, path, quedan)    # obtengo la capacidad de esa ruta

    flujo += capacidad_usada                 # incremento el flujo

    for a in path:                           # para cada arco de la ruta
        idx = arcs.index(a)                  # por legibilidad reduzco los arcos
        quedan[idx] -= capacidad_usada       # decremento la capacidad restante
        uso[idx] += capacidad_usada          # incremento el uso de cada nodo
        if quedan[idx] == 0:                 # arco exhausto
            min_cut.append(a)                # lo agrego a corte minimo
            arcos_restantes.remove(a)        # saco el arco para las proximas rutas

    path = DFS(arcos_restantes, 0, 5)        # a buscar otra ruta

  uso = [  f"{x[0]}: {x[1]}/{x[2]}" for x in list(zip(arcs, uso,C)) ]
  print(f"minimo corte:   {min_cut}")
  print(f"uso:            {uso}")
  print(f"flujo:          {flujo}")

