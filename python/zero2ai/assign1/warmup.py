'''
Practice with Python fundamentals using the Warmup class.
'''


def approx_e_with_exponent(n):
    '''
    Given a positive integer n, approximates math.e using the following
    limit: https://en.wikipedia.org/wiki/E_(mathematical_constant)#History

    Here's a hint in case you run into problems:
    https://stackoverflow.com/questions/30148740/how-do-i-do-exponentiation-in-python

    Here's another hint:
    https://www.geeksforgeeks.org/division-operator-in-python/
    '''
    return (1 + 1/n)*n


def are_lists_equal(arr1, arr2):
    '''
    Given two lists, checks to see if the lists have identical contents where
    the contents are also in the same order.
    '''
    if len(arr1) != len(arr2):
        return False

    for i in range(1, len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True


def find_min_idx(arr):
    min_idx = 0
    for i in range(0, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i
    return min_idx


def find_max_idx(arr):
    max_idx = 0
    for i in range(0, len(arr)):
        if arr[i] >= arr[max_idx]:
            max_idx = i
    return max_idx


def swap(arr, idx1, idx2):
    tmp = arr[idx1]
    arr[idx1] = arr[idx2]
    arr[idx2] = tmp


def swap_min_max(arr):
    '''
    Given an array of integers, swap the smallest element of the array with
    the largest element. If there multiple min or max elements, the first min
    or max appearing from left to right will be chosen.
    '''
    min_idx = find_min_idx(arr)
    max_idx = find_max_idx(arr)
    swap(arr, min_idx, max_idx)
