# Step 6: Activate the Conda Environment for `assign0`

[Getting Started as a Student](./getting-started.md)

[previous: Conda Installation](./conda-install.md)

[next: Build the Zero-To-AI Documentation](./build-z2ai-documentation.md)

Here is a fantastic
[cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)
for working with conda environments. Bookmark it!

## Conda Environments

A conda "environment" provides virtualization around dependencies. Instead
of installing a bunch of dependencies directly on your computer that will
always be accessed any time you try to run Python, conda proposes the notion
that each environment can have its own custom tailored version of dependencies.

As an example, if I'm working on a Python project called `personal-website`,
perhaps I have a conda environment called `website` for that project which I
have set up. I can issue a
```bash
conda activate website
```
which will activate the `website` conda environment, where all my dependencies
for that project will be stored (including Python version for that specific
project). I can view the dependencies for that project
using a
```bash
conda list
```
which shows all the dependencies and their corresponding versions. If I now
want to work on a different Python project on my same machine that has a
different set up project dependencies, I can switch conda environments. As an
example, let's say I have a project called `interview-prep` with a
corresponding conda environment I've created called `interviews`. Now, I can
issue a
```bash
conda activate interviews
```
which will switch my conda environment, and now I have access to those
dependencies in that environment.

Different conda environments can specify different versions of Python as well.
This is a great way to manage versions of Python, especially if one project is
running Python 2.7 and another project is running Python 3.7. Just create
separate conda environments for each project!

### Setting up the `assign0` Conda Environment

Each assignment will have its own conda environment. As an example, `assign0`
will rely on the `stanfordkarel` Python package, but `assign1` wil not. To
keep Python dependenices logically organized, you will create a separate
conda environment for each assignment.

Now that you have `conda` installed, in any directory on your machine, issue
a
```bash
conda env list
```
You should see output similar to:
```bash
# conda environments:
#
base                     /Users/jamescranston/miniconda3
```
Here, you have a `base` environment. Think of the `base` environment as the
main environment you will use without specialized dependencies for projects.
If you want to install specialized software for a project, it's better not to
do so in the `base` environment, but instead create a different environment
(like what we will be doing for each assignment).

Activate the `base` environment as follows:
```bash
conda activate base
```
Now, your bash prompt should indicate a `(base)` to the left, indicating that
you are in your `base` conda environment.

If you issue a
```bash
conda list
```
from within your `base` environment, you'll see all the software that shipped
with the bare-bones Miniconda distribution. For what it's worth, if you
installed `conda` from Anaconda, there would be a lot more packages.

Now, we're going to create the `assign0` conda environment with the proper
software (Python packages) installed for `assign0`. There are a few ways to
create a conda environment, but for this project we will be creating them
from dependency YAML files located in the `conf` directory.

Please look at the dependencies you will be installing for `assign0`. 

TODO: Finish documentation.

[next: Build the Zero-To-AI Documentation](./build-z2ai-documentation.md)
