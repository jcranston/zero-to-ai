# Step 7: Build the Zero-To-AI Documentation

[Getting Started as a Student](./getting-started.md)

[previous: Activate the Conda Environment for `assign0`](./activate-conda-env.md) 

The instructions rooted from [`getting-started.md`](getting-started.md) 
(including this final page of instructions) are meant to kick off working
through the assignments. However, specific assignments instructions are going
to be located in the `docs` folder, which you will need to programmatically
build. In general, production-grade Python projects will have documentation
that is generated programmatically, so it is good practice to do so here as
well.

1. First, switch to the `python` directory where the `Makefile` that contains
the target necessary for building the documentation. For the purpose of
learning Python, you don't need to open up the Makefile per-se, but if you are
curious to see how the documentation (and other `make` targets) execute, feel
free to read the file in greater detail.
    ```bash
    cd ~/sandbox/zero-to-ai/python
    ```
1. Now, build the documentation as follows:
    ```bash
    make docs
    ```
    You will see command line output as the documentation gets built. If the
documentation gets built correctly, you will see the last line of the
terminal output as
    ```bash
    open ../docs/_build/html/index.html
    ```
    Copy and paste this command into your terminal and execute it. It should
open the documentation in your browser (ideally Chrome)!

Please note, `make docs` calls a target called `sphinx-build` which is
installed in your current conda environment, `assign0`. Issuing
`make docs` would fail if you did not have your conda environment activated
(see above for more information).

When working in `zero-to-ai` going forward, please issue `make docs` to
recompile the documentation if the source code for the documentation changes.
Please open the documentation in your Chrome browser using the above `open`
command every time you work on assignments and need to read assignment
documentation.