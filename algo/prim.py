#!/usr/bin/env python
'''
An implementation of the Prim-Jarnik algorithm, a greedy method of finding
the minimum spanning tree for a connected, weighted, undirectred graph.
'''

import data.heap
        

# Elements in the heap will hold the vertices we have yet to span (V-X) - the horizon or fringe
# For each v in V-X, key[v] = cheapest edge (u, v) with u in X; if there does not exist u,
#   then key[v] = +infinity

# After moving a vertex from V-X to X, the key values of other vertices change.
# We must now update the key values for all vertices adjacent to the pulled in one
def update():
    when v added to X:
        for each (v, w) in E:
            if w in V-X:
                delete w from heap
                recompute key[w] = min(key[w], c[v, w])
                re-insert w into heap
