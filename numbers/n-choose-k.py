#!/usr/bin/env python2

def n_choose_k(list, k):
    """
    Given a list and a number k, returns all combinations of k-tuples from the
    list.

    This has the property than len(n_choose_k(list, k)) = (len(list) choose k).
    """
    # Base cases
    if k < 0 or k > len(list):
        # Out of bounds
        return []
    elif k == 0:
        # n choose 0 = 1, by choosing the empty set
        return [[]]
    else:
        # Recursive step
        # For each item in the list, find all (k-1)-tuples of the sublist of
        # elements immediately after it, and then join them together
        result = []
        for i in range(0, len(list)-k+1):
            singleton = [list[i]]
            result += [singleton + x for x in n_choose_k(list[i+1:], k-1)]

        return result

        # We could also do the terse but cryptic double list comp:
        # return [[list[i]] + x for i in range(0, len(list-k+1)) for x in n_choose_k(list[i+1:], k-1)]

list = [1, 2, 3, 4, 5]
for k in range(0, len(list)+1):
    print "All {0}-tuples of {1}:".format(k, list)
    print "\t{0}\n".format(n_choose_k(list, k))
