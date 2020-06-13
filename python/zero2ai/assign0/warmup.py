'''
Practice with Python fundamentals using the Warmup class.
'''


class Warmup:
    '''
    Class that contains warmup methods for you to fix so that unit tests pass.
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
