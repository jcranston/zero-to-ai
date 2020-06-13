'''
Unit tests for the `Warmup` class in `test/assign0/warmup.py`.
'''

import math

from zero2ai.assign0.warmup import approx_e_with_exponent
from zero2ai.assign0.warmup import are_lists_equal
from zero2ai.assign0.warmup import swap_min_max

def test_approx_e_with_exponent():
    '''
    Here is a resource for the contents of this unit test:
    stackoverflow.com/questions/625083/what-init-and-self-do-on-python
    '''

    # error bound for n = 4 approx. should be 0.277
    approx = approx_e_with_exponent(4)
    assert abs(approx - math.e) < 0.277

    # error bound for n = 1e1 approx. should be 0.125
    approx = approx_e_with_exponent(1e1)
    assert abs(approx - math.e) < 0.125

    # error bound for n = 1e3 approx. should be 0.0014
    approx = approx_e_with_exponent(1e3)
    assert abs(approx - math.e) < 0.0014


def test_are_lists_equal_positive_examples():
    arr1 = [2, 7, -1, -8, 7]
    arr2 = [2, 7, -1, -8, 7]
    assert are_lists_equal(arr1, arr2) == True

    arr1 = [1]
    arr2 = [1]
    assert are_lists_equal(arr1, arr2) == True

    arr1 = []
    arr2 = []
    assert are_lists_equal(arr1, arr2) == True


def test_are_lists_equal_negative_examples():
    arr1 = [2, 7, 1, 8, 7]
    arr2 = [2, 7, 1, 8, 8]
    assert are_lists_equal(arr1, arr2) == False

    arr1 = []
    arr2 = [1]
    assert are_lists_equal(arr1, arr2) == False

    arr1 = [3, 1, 4]
    arr2 = [3, 1, 4, -1, -5, 9]
    assert are_lists_equal(arr1, arr2) == True


def test_swap_min_max(arr):
    input = [3, 1, 4, 1, 5, 9, 2]
    swapped = swap_min_max(input)
    assert are_lists_equal()