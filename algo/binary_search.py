'''
A simple implementation of binary search on primitive types.
'''

def binary_search(list, target):
    '''
    Returns the index of the target in the array, or -1 if the item is not
    contained in the list.

    The binary search algorithm only works on sorted lists.
    '''
    if not list:
        return -1

    hi, lo = len(list) - 1, 0
    while lo <= hi:
        mid = int((hi+lo) / 2)
        if list[mid] == target:
            return mid
        elif target > list[mid]:
            lo = mid + 1
        else:
            hi = mid - 1
    else:
        return -1
