from random import shuffle


def bogosort(arr):
    arr = arr[:]
    while not _is_sorted(arr):
        shuffle(arr)
    return arr


def _is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in xrange(len(arr)-1))
