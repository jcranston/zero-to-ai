.. _conda-env-setup-label:

Setting Up Your Conda Environment
=================================

Make sure you've read through :ref:`conda-installation-label` before reading
this page.

.. note::

    Here is a fantastic `cheat sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_
    for working with conda environments. Bookmark it!

Conda Environments
~~~~~~~~~~~~~~~~~~

A conda "environment" is provides virtualization around dependencies. Instead
of installing a bunch of dependencies directly on your computer that will
always be accessed any time you try to run Python, conda proposes the notion
that each environment can have its own custom tailored version of dependencies.

As an example, if I'm working on a python project called ``personal-website``,
perhaps I have a conda environment called ``website`` for that project which I
have set up. I can issue a

.. code-block:: bash

    conda activate website

which will activate the ``website`` conda environment, where all my dependencies
for that project will be stored. I can view the dependencies for that project
using a

.. code-block:: bash

    conda list

which shows all the dependencies and their corresponding versions. If I now want
to work on a different python project on my same machine that has a different
set up project dependencies, I can switch conda environments. As an example,
let's say I have a project called ``interview-prep`` with a corresponding
conda environment I've created called ``interviews``. Now, I can issue a

.. code-block:: bash

    conda activate interviews

which will switch my conda environment, and now I have access to those
dependencies in that environment.

Different conda environments can specify different versions of Python as well.
This is a great way to manage versions of Python, especially if one project is
running Python 2.7 and another project is running Python 3.7. Just create
separate conda environments for each project!

Setting up the ``ai`` conda environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have ``conda`` installed, in any directory on your machine, issue
a

.. code-block:: bash

    conda env list

You should see output similar to:

.. code-block:: bash

    # conda environments:
    #
    base                     /Users/jamescranston/miniconda3

Here, you have a ``base`` environment. Think of the ``base`` environment as the
root level environment from which all other environments inherit. If you want to
install specialized software for a project, it's better not to do so in the
``base`` environment, but instead create a different environment.

Activate the ``base`` environment as follows (this is also available on the
`cheat sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_
):

.. code-block:: bash

    conda activate base

Now, your bash prompt should indicate a ``(base)`` to the left, indicating that
you are in your ``base`` conda environment.

If you issue a

.. code-block:: bash

    conda list

from within your ``base`` environment, you'll see all the software that shipped
with the bare-bones Miniconda distribution. For what it's worth, if you were to
have installed ``conda`` from Anaconda, there would be a lot more packages.

Now, we're going to create the ``ai`` conda environment with the proper software
(Python packages) installed for the Zero to AI project. There are two ways to do
this, and I'll explain both of them here (pick either step 1. or step 2. to
follow, but perhaps read through them both).

1. Set up the ``ai`` environment directly from the ``dev.yaml`` file:

    a. You can create the ``ai`` environment with the proper dependencies installed in one fell swoop by issuing the following (make sure you are in your ``zero-to-ai`` directory before starting these commands).::

        pwd # should end in your zero-to-ai directory
        cd python # change to the python directory within zero-to-ai
        conda env --file dev.yaml --name ai

    b. The last command creates a conda environment called ``ai`` (specified by
       the ``--name`` tag). Furthermore, it reads all the dependencies that it
       needs to install from the ``dev.yaml`` file. `Here <https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#create-env-file-manually>`_
       is more information on how the environment YAML files are structured, if
       you are curious to read more.

2. First create the ``ai`` environment, and then update it from the ``dev.yaml``
   file:

    a. Create the ``ai`` environment first::

        conda env create --name ai

    b. Update the newly created ``ai`` environment with the dependencies from
       the ``dev.yaml`` file::

        pwd # should end in your zero-to-ai directory
        cd python # change to the python directory within zero-to-ai
        conda env update --name ai --file dev.yaml

      This now updates the ``ai`` environment by installing the dependencies
      from the ``dev.yaml`` file. If you ever need to install a new dependency
      to the ``ai`` environment, just add it to the ``dev.yaml`` file and then
      issue the previous update command. It will just go and find the new
      dependencies and install them.

Alternately, you could have manually installed each dependency manually from
the ``dev.yaml`` file. For example, you could have issued::

    conda env create --name ai # create the ai environment
    conda install --channel conda-forge nbsphinx # install nbsphinx from the conda-forge channel
    conda install python=3.7 # explicitly install version 3.7 of python
    conda install --channel defaults recommonmark # install recommonmark from defaults channel
    # ... etc

The reason for putting all the dependencies in the ``dev.yaml`` file is that
it makes installation and package management a lot cleaner, and also more easily
maintainable by developers. See below for more information on conda channels.

Conda Channels
~~~~~~~~~~~~~~

A conda "channel" is a location to install packages from with conda. If you
issue a::

    conda install <some_package>

it will attempt to search for the package from the ``defaults`` channel. (You
can also specify ``--channel defaults`` in that command). However, if it fails
to find the package in ``defaults``, you can specify the ``conda-forge``
channel::

    conda install --channel conda-forge <some_package>

Notice that we specify ``defaults`` as well as ``conda-forge`` in the
``dev.yaml`` file, meaning that when conda attempts to install packages
specified in the ``dev.yaml``, it will first look at ``defaults`` to see if the
software is available, and if not, it will check ``conda-forge``. Generally,
``conda-forge`` is seen as a "last resort" measure, should the software not be
available in ``defaults``.

Here are some more resources on conda channels:

- `Official documentation on conda channels <https://docs.conda.io/projects/conda/en/latest/user-guide/concepts/channels.html>`_
- `StackOverflow post titled "Explanation of different conda channels" <https://stackoverflow.com/questions/42309333/explanation-of-different-conda-channels>`_
- `The official conda-forge.org website <https://conda-forge.org/>`_

Anyways, now you should be good to go with a healthy Python environment for this
project! If you are ever having trouble running the project, make sure you are
in the ``ai`` environment. Refer to the `cheat sheet <https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf>`_
for quick references to conda commands!

Now you're ready to move onto the assignments: See