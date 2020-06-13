.. _conda-installation-label:

Installing Conda
================

What is conda?
~~~~~~~~~~~~~~

Conda is a Python package manager, meaning it manages 3rd party Python libraries
you may need when writing your code. There are other package management systems
for Python, including Python virtual environments as well as ``pip``. Generally,
Python package management is a historically `messy subject
<https://xkcd.com/1987/>`_, and so it's good practice for Python developers to
try and stick with one package manager.

.. danger::
   For the entirety of working in this project, do NOT use any other package
   manager other than ``conda`` to install and manager 3rd party software. There
   are insidious bugs that come from mixing ``pip`` with ``conda``. This is a
   lesson that's not worth learning the hard way.

Once ``conda`` is installed, let's say you need to use the ``numpy`` package to
do some linear algebra operations in Python. You would be able to install it
using ``conda install numpy``

``conda`` is available by installing either Anaconda or Miniconda. The
difference between the two only has to do with what Python packages ship with
Anacdona vs. what packages ship with Miniconda. Anaconda is considered a
"one-stop shop" for many packages that are useful for Python development. If
the package you need isn't available from Anaconda, you can always additionally
install it with ``conda install <name_of_package>``.

As the name implies, Miniconda is a "bare bones" set of packages that does not
include most of the packages that ship with Anaconda. For this project, we are
going to install Miniconda so that we can get practice installing the
dependencies we need manually, as they are probably included with Anaconda. The
purpose here is purely educational.

Here are some more links about Anaconda vs. Miniconda:

- `official release notes for Anaconda Individual Edition <https://docs.anaconda.com/anaconda/reference/release-notes/>`_
   - you can see here what packages ship with each release of anaconda
   - note that the each release of Anaconda specifies specific versions for the
     packages included in that Anaconda release
   - let's pay attention only to the Individual Edition, not Enterprise Editions
- `official documentation page for Miniconda <https://docs.conda.io/en/latest/miniconda.html>`_
   - there's not much here. Don't download yet; we'll do this together in the next step

Here are some more good resources that explain ``conda`` depending on your
preferred learning style:

- `official conda documentation <https://docs.conda.io/en/latest/>`_
- `Wikipedia page on Anaconda <https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)>`_
- `official docs: difference between conda and pip <https://www.anaconda.com/blog/understanding-conda-and-pip>`_
- `26-minute youtube video called "Conda - What & Why?" with 32k views <https://www.youtube.com/watch?v=23aQdrS58e0>`_
- `StackOverflow post on difference between pip and conda <https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda>`_

Installing Conda via Miniconda
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Visit the `Miniconda documentation <https://docs.conda.io/en/latest/miniconda.html>`_
page in your browser. I'm going to provide download instructions for ``conda``
if you are running entirely in a shell (i.e. on AWS) that do not require
clicking on links. So don't click on these links just yet; but read this page
if you'd like to learn more.

2. Open a shell in the operating system you'd like to download ``conda`` (i.e.
a shell on your local machine, or a server you've ``ssh``'d into). These
instructions may change as these links change going forward, but for now, they
should work. These are installing ``conda`` for Python 3.7:

- This isn't necessary, but for consistency, switch to your home directory (``cd ~``).
- If you are running a 64-bit Linux OS (Ubuntu, FreeBSD, Debian, etc.), issue:

.. code-block:: bash

   curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

- Otherwise, if you are running macOS, issue:

.. code-block:: bash

   curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh

- This downloads a shell script called the installer into your home directory.

3. Now, you have to execute the shell script in order to install ``conda``
(make sure you are in your home directory):

- If you are running Linux, issue:

.. code-block:: bash

   /bin/bash Miniconda3-latest-Linux-x86_64.sh

- If you are running macOS, issue:

.. code-block:: bash

   /bin/bash Miniconda3-latest-MacOSX-x86_64.sh

- In either case, you'll be prompted in the installer to accept the legal agreement, as well as approve of the install location for ``conda``. By default, the installer will chose a location underneath your home directory, for example:

.. code-block:: bash

   /Users/$HOME/miniconda3/bin/conda

4. Finally, once the installer runs, you'll have to quit your shell and restart
it for the ``conda`` program to be recognized in the ``PATH``. Issue a
``which conda`` to verify that conda is installed (and that it is installed in
a ``miniconda3`` directory, not ``anaconda3`` directory).

5. Optional step: feel free to remove the installer now, to keep your home
directory clean (but you can leave it around if you'd like too, or move it):

.. code-block:: bash

   rm Miniconda3-latest-Linux-x86_64.sh

(or similar command if you have the macOS installer).

Now that you've read this, set up your conda environment
for the Zero to AI project in :ref:`conda-env-setup-label`.



