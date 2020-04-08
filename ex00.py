#!/usr/bin/env python
from pprint import pprint

import numpy as np


"""
#EX0: Build a function that transforms Node-Node matrix (incidence matrix) to Node-Arc matrix
"""
def nn2na(NN):
  idx = np.argwhere(NN)
  NA = np.zeros([NN.shape[0], idx.shape[0]]).astype(int)
  for i, arc in enumerate(idx):
    NA[arc[0], i] = 1
    NA[arc[1], i] = -1

  arc_idx = [ (arc[0], arc[1]) for arc in idx]
  return NA, arc_idx

if __name__ == '__main__':
  una_NN = np.array([[0, 1, 1],[ 0, 0, 0],[0, 0, 0 ]])
  pprint(nn2na(una_NN))
