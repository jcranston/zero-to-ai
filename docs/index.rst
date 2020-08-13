.. _index-label:

Zero to AI Assignment Documentation
===================================

Prerequisites
~~~~~~~~~~~~~

Please follow all the installation instructions outlined in
"Getting Started as a Student" before following the assignment documentation
here.

.. toctree::
   :maxdepth: 2
   :caption: Assignment Documentation

   assignments/assign0/assign0
   assignments/assign1/assign1

Creating Assignment Conda Environments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Note: if your shell is not recognizing the ``conda`` executable, you can
issue a ``source ~/.bash_profile`` which will add ``conda`` as a target in
your ``PATH`` bash variable.

To create the conda environment necessary to complete ``assignN`` (i.e. for
``assign0``, ``assign1``, etc), switch to the ``zero-to-ai/python`` directory
and execute:

.. code-block:: bash

    conda env create -f conf/assignN-deps.yml

replacing ``assignN`` with your specific assignment. Alternately, from the
same ``zero-to-ai/python`` directory you can issue the ``make`` target:

.. code-block:: bash

    make conda-env-assignN

which will create the conda environment for you (again, replace ``assignN``
with your specific assignment).

Once you have created the conda environment for your specific environment,
you can activate it using:

.. code-block:: bash

    conda activate assignN

Refer to the conda
`cheat sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_
for other conda operations.

Building the Assignment Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From ``~/sandbox/zero-to-ai/python``, issue:

.. code-block:: bash

    make docs

Open the documentation (HTML files) in your browser by issuing:

.. code-block:: bash

    open ../docs/_build/html/index.html

Destroying the Assignment Documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

From ``~/sandbox/zero-to-ai/python``, issue:

.. code-block:: bash

    make docs-clean

This will destroy all the HTML files generated from ``make docs``. You can
always rebuild the documentation.

