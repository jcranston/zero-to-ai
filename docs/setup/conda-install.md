# Step 5: Conda Installation

[Getting Started as a Student](./getting-started.md)

[previous: Pycharm Installation](./pycharm-install.md)

[next: Activate the Conda Environment for `assign0`](./activate-conda-env.md)

## What is Conda?
Conda is a Python package manager, meaning it manages 3rd party Python
libraries you may need when writing your code. There are other package
management systems for Python, including Python virtual environments as well
as `pip`. Generally, Python package management is a historically
[messy subject](https://xkcd.com/1987/), and so it's good practice for Python
developers to try and stick with one package manager.

For the entirety of working in this project, do NOT use any other package
manager other than ``conda`` to install and manager 3rd party software. There
are insidious bugs that come from mixing ``pip`` with ``conda``. This is a
lesson that's not worth learning the hard way.
My danger paragraph.

Here is an example of Python code that attempts to import the library
`stanfordkarel`:
```python
from stanfordkarel import *
```
This line of code attempts to import all the dependencies under the
`stanfordkarel` package. Without having a package manager in your current
Python environment, the Python interpreter will not know where to go find
the `stanfordkarel` package and its subsequent sub-packages. This example is
relevant because you will be using the `stanfordkarel` library for `assign0`.

Here is another example: once `conda` is installed, let's say you need to use
the `numpy` package to do some linear algebra operations in Python. You would
be able to install it using `conda install numpy` at the command line, if
`numpy` is not already installed in your current Python environment. Then at
the top of your Python file, you would be able to import the dependency as
follows:
```python
import numpy as np
```
where the `np` variable will enable you to access the various methods in the
`numpy` package.

## Miniconda vs. Anaconda

`conda` is available by installing either Anaconda or Miniconda. The
difference between the two only has to do with what Python packages ship with
Anacdona vs. what packages ship with Miniconda. Anaconda is considered a
"one-stop shop" for many packages that are useful for Python development. If
the package you need isn't available from Anaconda, you can always additionally
install it with `conda install <name_of_package>`.

As the name implies, Miniconda is a "bare bones" set of packages that does not
include most of the packages that ship with Anaconda. For this project, we are
going to install Miniconda so that we can get have a lean working environment.
The purpose here is purely educational.

In a scientific computing environment, it is more common to use Anaconda, but
both will suffice at any time (you just may have to do more manual package
installs if you are using Miniconda).

- [Official release notes for Anaconda Individual Edition](https://docs.anaconda.com/anaconda/reference/release-notes/)
   - You can see here what packages ship with each release of anaconda
   - Note that the each release of Anaconda specifies specific versions for the
     packages included in that Anaconda release
   - Let's pay attention only to the Individual Edition, not Enterprise Editions
- [Official documentation page for Miniconda](https://docs.conda.io/en/latest/miniconda.html)
   - There's not much here. Don't download yet; we'll do this together in the next step

Here are some more good resources that explain ``conda`` depending on your
preferred learning style:

- [official conda documentation](https://docs.conda.io/en/latest/)
- [Wikipedia page on Anaconda](https://en.wikipedia.org/wiki/Anaconda_(Python_distribution)
- [official docs: difference between conda and pip](https://www.anaconda.com/blog/understanding-conda-and-pip)
- [26-minute youtube video called "Conda - What & Why?" with 32k views](https://www.youtube.com/watch?v=23aQdrS58e0)
- [StackOverflow post on difference between pip and conda](https://stackoverflow.com/questions/20994716/what-is-the-difference-between-pip-and-conda)

## Installing Conda via Miniconda

1. Visit the
[Miniconda documentation](https://docs.conda.io/en/latest/miniconda.html)
page in your browser. I'm going to provide download instructions for `conda`
if you are running entirely in a shell (i.e. on AWS) that do not require
clicking on links in a graphical user interface (GUI). So don't click on these
links just yet; but read that page if you'd like to learn more.
1. Open a shell in the operating system you'd like to download `conda` (i.e.
a shell on your local machine, or a server you've `ssh`'d into). These
instructions may change as these links change going forward, but for now, they
should work. These are installing `conda` for Python 3.7:
    - For consistency, switch to your home directory
    with
        ```bash
        cd ~
        ```
    - If you are running a 64-bit Linux OS (Ubuntu, FreeBSD, Debian, etc.),
    issue:
        ```bash
        curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
        ```
    - Otherwise, if you are running macOS, issue:
        ```bash
        curl -O https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh
        ```
    - Either of the above command will download a shell script called the
    installer into your home directory on your machine.
1. Now, you have to execute the shell script in order to install `conda`
(make sure you are in your home directory, see above):
    - If you are running Linux, issue:
        ```bash
        /bin/bash Miniconda3-latest-Linux-x86_64.sh
        ```
    - If you are running macOS, issue:
        ```bash
        /bin/bash Miniconda3-latest-MacOSX-x86_64.sh
        ```
    - In either case, you'll be prompted in the installer to accept the legal
    agreement, as well as approve of the install location for `conda`. By
    default, the installer will chose a location underneath your home
    directory, for example (if on macOS):
        ```bibtex
        /Users/$HOME/miniconda3/bin/conda
        ```
        (Do not run this, I am just showing where it is installed.)
1. Finally, once the installer runs, you'll have to quit your shell and restart
it for the `conda` program to be recognized in the `PATH`. Issue a
`which conda` to verify that conda is installed (and that it is installed in
a `miniconda3` directory, not `anaconda3` directory). If issuing `which conda`
succeeds to report an installed location, you are ready to move on to the next
step.
1. Optional step: feel free to remove the installer now, to keep your home
directory clean (but you can leave it around if you'd like too, or move it):
    ```bash
    rm Miniconda3-latest-Linux-x86_64.sh
    ```
    (or similar command if you have the macOS installer).

[next: Activate the Conda Environment for `assign0`](./activate-conda-env.md)
