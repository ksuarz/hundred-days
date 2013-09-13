'''
Given a path graph (that is, a 'linear' undirected graph) with weights assigned
to each edge, this calculates the maximum weight independent set of the graph.

Here, an independent set of a graph is a subset S of the vertices such that for
all u, v in S, u and v are not adjacent.

If we used brute force, the number of subsets of the graph is exponential;
however, we can use a dynamic algorithm that runs in linear time. Observe the
following:

    1. The last vertex v is not in the maximum-weight independent set S. Then,
       S must be the MWIS of the subgraph G' = G - {v}; if it was not, then we
       could come up with an even better MWIS for G by adding v. However, this
       contradicts the invariant that S is the MWIS.
    2. The last vertex v is, in fact, in S. Then, let G'' = G - {v, u}, where u
       is the penultimate vertex (in other words, remove the last two). So
       there must be a MWIS for G'' that we'll call S*. Then S = S* + {v}.

If we knew whether or not this last vertex is in in S or not, we can remove
either {v} or {u, v} and recurse, finding the MWIS for either G' or G''. There
is no real way to determine this without calculating a MWIS for both G' and
G'' + {v}, so we calculate both and return whichever is greater.

Normally, this takes exponential time; however we only really solve O(n) unique
subproblems. By using memoization, we can cut down the algorithm to calculate
the value of the MWIS in linear time.
'''

class OptimalIndependentSet():
    '''
    Calculates the optimal (that is, maximum weight) independent set of a path
    graph.
    '''
    def __init__(self, vertex):
        '''
        Initializes the graph with a positive-valued array, where vertex[i] is
        the weight of vertex i.
        '''
        self.vertex = vertex
        self.progress = [vertex[0]]

    def max_weight_indp_set(self):
        '''
        Does all the work and calculates the value of the maximum weight
        independent set of the class' path graph.
        '''
        for i in xrange(1, len(self.vertex)):
            # There's an obvious bug when i=2, but this conveys the idea
            progress[i] = max(progress[i-1], progress[i-2] + vertex[i])
