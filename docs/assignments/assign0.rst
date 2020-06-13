Assignment 0: Welcome to Python!
================================

Background
----------

Welcome to Python! Woohoo! This is where things get fun, now that you are set
up with git, conda, basic Unix navigation skills, and your IDE/text editor.

Assignment 0 is going to focus on Python types, variable assignments, control
flow, and basic I/O. Well, more so the "0" (output), less so the "I" (input).
We'll get to reading from a file other other data inputs later on.

You're going to learn about **test-driven development** (TDD) as well. Test
driven development is the concept of *writing tests* to verify *how* you want
your code to behave before you actually go write your code. In addition to
teaching you how to write code, you'll also be learning *good coding practices*
along the way, like TDD.

Here's an example: let's say you're trying to write a Python method that tries
to select the maximum (largest) number from a list of numbers. I.e., you want to
write a method called ``find_max`` which, given a list of numbers, will select
the maximum element. In TDD, you will write a test first that verifies how you
want your method ``find_max`` to behave. Before going and writing ``find_max``,
you'll write a few methods that test the behavior of ``find_max``:

.. code-block:: python

    def test_find_max_first_elem():
        nums = [ 10, 4, -3, 0 ] # declare the list of numbers in `num` variable
        max = find_max(nums)    # we haven't written find_max yet, but are writing how it is used
        assert max == 10        # this asserts how we want find_max to behave

This test checks to see if ``find_max`` can find a maximum element if that
number is at the beginning of the list. But to make our testing more robust,
we should go and write more tests for ``find_max``, such as:

.. code-block:: python

    def test_find_max_inner_elem():
        nums = [ 0, 2, 4, -1 ]
        max = find_max(nums)
        assert max == 4

    def test_find_max_last_elem():
        nums = [ 0, 2, 4, 20 ]
        max = find_max(nums)
        assert max == 20

    def test_find_max_duplicate():
        nums = [ 0, 6, 4, 6 ]
        max = find_max(nums)
        assert max == 6

    def test_find_max_no_elems():
        nums = [ ]
        max = find_max(nums)
        assert max is None

In our last test, we explicitly direct how we want our implementation of
``find_max`` to perform if there are no elements in the list: we are saying in
our test that we expect ``find_max`` to return ``None``.

Requirements
------------

Your task is as follows:

1. Start watching the 3Blue1Brown `"Essence of Linear Algebra" <https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab>`_
series. Linear algebra is going to lay the foundation for algorithms in AI. The
content of the Python methods will be related to linear algebra in this
assignment.

2. Boot up either the interactive python interpreter by issuing simply::

    python

   or boot up ``ipython`` by similarly issuing::

    ipython

to play around with defining variables and types. Once you are in either
command prompt, follow along with `Learn Python in Y minutes <https://learnxinyminutes.com/docs/python/>`_
and enter the same variables in your python interpreter. Alternately, you can
practice writing in your text editor of choice and writing a file that contains
the same content (so you can practice keystrokes in your text editor). If you
chose to use an interpreter to practice, copy and paste the interpreter output
from your terminal (from when you ran either ``python`` or ``ipython``) into a
file called ``interpreter-output.txt``. Put this in the ``zero2ai/assign0``
directory. If you instead chose to write a file with the content from the "Learn
Python in Y minutes" page, save it in a file called ``practice.py`` and verify
it can run by issuing::

    python practice.py

and then saving this file in the ``zero2ai/assign0`` directory. I would
probably recommend using a Python interpreter instead of writing a file, though.
Or you could do both for extra practice!

1. Warmup: For every unit test in
``python/test/assign0/test_warmup.py`` that does not currently pass, go and fix
the corresponding methods in the source code to ensure the tests pass. If the
source code is actually correct, there may be a problem with the unit tests,
and you'll have to go fix those as well.

    a. please check in a git commit that is titled
       ``"assign0/warmup: tests fixed`` once you are done with Part 1, and I
       will be able to evaluate your work for just this commit.

2. TDD: You're going to practice test-driven-development. In
``python/zero2ai/assign0/utils.py``, there are many "utility" Python classes
that contain methods you need to implement. This is where you're going to do
the bulk of your very first Python programming! However, here's the catch:
you first have to write the tests for how you want the methods to behave in
``python/tests/assign0/test_utils.py``. Once you are finished writing the tests
for a specific class, and you feel as if those tests are robust, you can go and
implement the methods in the corresponding classes in ``utils.py``.

    a. please check in a git commit that is titled
       ``assign0/tdd: tests written`` once you finish writing the tests in
       ``test_utils.py``. Please not that at this git commit, you should not
       have implemented any of the methods in ``utils.py`` yet. This, in
       essence, is the most important commit for the spirit of TDD: I want to
       see that you are writing robust tests for all edge cases.
    b. please check in a git commit that is titled
       ``assign0/tdd: methods implemented`` once you implement the methods and::

            make test-assign0

       passes, calling all the tests you have written which in turn call the
       methods you have implemented. In addition to implementing the methods in
       ``utils.py``, include docstring comments on the methods (you can read
       more about This should be your last commit.

3. Submit your code in a branch to the remote git repository for code review.

Learning Goals
--------------

Here is what we are trying to have you take away from Assignment 0:

- A sense for the reason behind Test Driven Development and why it is important.
- The difference between TDD and unit tests.
- What problems can arise for developers if they don't practice TDD.
- Python types, control flow, and basic I/O.
- Executing the tests using a ``make`` target.
- Basic understanding of ``pytest``.
- More familiarity with your operating system, Unix commands, and text editor.


Mathematical Resources
----------------------

Frobenius Norm of the Matrix
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Given a matrix :math:`A\in\mathbb{R}^{n\times k}`, the Frobenius Norm of the
matrix is defined as

.. math::

    \|A\|_\text{Fro}=\left(\sum_{i=1}^{n}\sum_{j=1}^{k} |A_{ij}|^2\right)^{1/2}

:math:`A_{ij}` corresponds to the :math:`(i,j)^\text{th}` element of the
matrix, meaning the element at row :math:`i` and column :math:`j`.

This is a consise way of summing the squares of each element in the matrix and
then taking the square root. Sort of like finding the hypotenuse lenghth of a
triangle in a higher dimension, if each side of the triangle was an element of
the matrix.

Your task will be to implement computing the Frobenius Norm in Python.


Web Resources
~~~~~~~~~~~~~

- `Learn Python in Y minutes: a very gentle introduction: <https://learnxinyminutes.com/docs/python/>`_
- `*Fantastic* YouTube series from 3Blue1Brown that gently introduces linear algebra <https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab>`_ (Grant was one year ahead of me at Stanford)
- `pytest documentation <https://docs.pytest.org/en/latest/>`_
- `How to document Python code <https://realpython.com/documenting-python-code/>`_
- `An 11-minute YouTube video on Python unit testing <https://www.youtube.com/watch?v=_0soBPejyu4>`_ (note that his code setup is slightly different; just pay more attention to the "spirit" than the actual code setup)
- `YouTube video on Test Driven Development <https://www.youtube.com/watch?v=QCif_-r8eK4>`_
- `CS41 "Welcome to Python!" condensed notes <https://drive.google.com/file/d/1R-evFxkEfzMS20U-YuMzir5tr8Rb2M3A/view>`_
- `CS41 "Python Basics" condensed notes <https://drive.google.com/file/d/1JUu_bDSA08R1tNdjeJnBGq0GRY4FNc2f/view>`_
- `Official Python docs on Python classes <https://docs.python.org/3/tutorial/classes.html>`_
- `PEP 8 Style Guide for Python <https://www.python.org/dev/peps/pep-0008/>`_
- `flake8 Python linter <https://medium.com/python-pandemonium/what-is-flake8-and-why-we-should-use-it-b89bd78073f2>`_
