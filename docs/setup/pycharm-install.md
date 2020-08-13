# Step 4: Pycharm Installation

[Getting Started as a Student](./getting-started.md)

[previous: Install the Codebase for `zero-to-ai`](./codebase-install.md)

[next: Conda Installation](./conda-install.md)

## What is PyCharm?

Pycharm is the interactive development environment (IDE) we will be using to
write code for assignments in Zero-to-AI. An IDE is software that assists
with writing code, and makes interacting with version control (git) a lot
easier than working directly in the command line.

All that matters at the end of the day is that you write the correct code and
that tests pass. You can do this directly in the terminal by writing to files
and saving them. You do not need an IDE to do this. That said, having an IDE
saves up a lot of time by providing a convenient interface to work with.

PyCharm is supported by JetBrains, a phenomenal software company that also
supports IntelliJ, another popular IDE that is used for Java-based languages.
IntelliJ and PyCharm are very similar, and you could technically choose to use
IntelliJ with Python plugins as well: it's really up to you. If you want, you
can use another IDE like [Atom](https://atom.io/) or even
[Sublime Text](https://www.sublimetext.com/) to write code for Zero-to-AI, but
any instructions I provide in documentation will be using PyCharm.

I am using PyCharm community edition, which does not cost any money. There is
no reason to buy the professional version of PyCharm. Please note that
PyCharm ships with many bells and whistles and different plugins, but all that
matters at the end of the day is that you write the correct code and that tests
pass: you do not need a fancy IDE to do this (and in fact, in the early days
of systems programming, there was no such thing as an IDE!).

## Download and Install PyCharm

Please visit https://www.jetbrains.com/pycharm/ to download: it is available
for a few different operating systems. Make sure you are downloading the
community version. Follow the necessary install steps for your OS.

## Load Zero-to-AI Into PyCharm

Since you've checked out the code base already into the `~/sandbox/zero-to-ai`
directory, it is time to load this into PyCharm! Follow
[these](https://www.jetbrains.com/help/pycharm/importing-project-from-existing-source-code.html)
steps for loading the `zero-to-ai` directory into PyCharm. When selecting the
directory that contains the desired source code, on a Mac you can type
```
Ctrl + Shift + G
```
to go go a specific folder. When the dialog opens, type `~/sandbox` and then
click on the `zero-to-ai` folder.

Once the code base is loaded, you should be able to navigate the folders of
the project in PyCharm on the left hand side. Feel free to open up a few
files.

## Mark ``python`` Directory as Sources Root

Finally, once you have installed the code into PyCharm, right-click on the
``python`` directory, go down to "Mark directory as" and click on
"Sources Root". This will enable PyCharm to recognize your Python imports
when you are writing code.

[next: Conda Installation](./conda-install.md)
