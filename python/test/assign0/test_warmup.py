'''
Unit tests for the `Warmup` class in `test/assign0/warmup.py`.
'''

import math

from pytest import fixture

from zero2ai.assign0.warmup import Warmup


@fixture
def warmup_class():
    '''
    Provides an instance of the Warmup() class accessible via the `warmup`
    variable name in parameter lists, thanks to the @fixture keyword from the
    pytest framework:
    https://docs.pytest.org/en/stable/fixture.html
    '''
    return Warmup()


def test_approx_e_with_exponent(warmup_class):
    '''
    Here is a resource for the contents of this unit test:
    stackoverflow.com/questions/625083/what-init-and-self-do-on-python
    '''

    # error bound for n = 4 approx. should be 0.277
    approx = warmup_class.approx_e_with_exponent(4)
    assert abs(approx - math.e) < 0.277

    # error bound for n = 1e1 approx. should be 0.125
    approx = warmup_class.approx_e_with_exponent(1e1)
    assert abs(approx - math.e) < 0.125

    # error bound for n = 1e3 approx. should be 0.0014
    approx = warmup_class.approx_e_with_exponent(1e3)
    assert abs(approx - math.e) < 0.0014
