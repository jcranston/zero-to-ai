# Step 2: Create a Github Account

[Getting Started as a Student](./getting-started.md)

[previous: The Command Line](./command-line.md)

[next: Install the Codebase for `zero-to-ai`](./codebase-install.md)

## What is Github?

Github is where the public codebase repository for this project is stored
(and where you are probably reading these instructions right now!).

In order to check out the codebase onto your local computer, you will need
need to issue `git` commands to obtain a copy of the remote.

`git` is versional control software running on your machine already that you
can access via the command line (issue `which git` to see where it is natively
installed). `git` is used to track changes to projects, and is overall an
incredibly complex tool. We will only be using a small subset of `git`
commands. Finally, `git` is capable of talking to a remote code repository,
which in our case is the code that is hosted on Github (which you are reading
the documentation for right now).

Here are some useful resources:
* [Google search of "what is github"](https://www.google.com/search?q=what+is+github)
* [Difference between Git and Github](https://stackoverflow.com/questions/13321556/difference-between-git-and-github)

## Create an Account

Visit [`https://github.com/join`](htts://github.com/join) and fill out the
account creation form. I recommend a short username like `jcranston` since
you will be typing your username frequently. Please store a strong password
(consider using a password manager to generate your password; I like
[1Password](https://1password.com/) personally) and enable two-factor
authentication on your account. You will likely have to save backup codes
when enabling 2FA on your account, and I definitely recommend storing this
information in a password manager.

## Set up SSH Keys
This is the most confusing step for checking out the code base. In order to
securely check out the code using the `git` command on your machine, your
comptuer needs to make a secure, authorized, and authenticated connection to
the remote code repository hosted on Github.

Normally when you are browsing the internet, your browser is doing this for
you automatically in an exchanged known as asymmetric key encryption.
However, in order for you to make a secure connection to Github from your
terminal, you'll need to manually enable this secure connection by registering
a public SSH key on Github.

If you are more interested to learn why this is necessary, feel free to read
these following pages. If you would rather just "follow the instructions", you
can skip this supplemental reading.
* [What is Asymmetric Cryptography? (1:57 minute YouTube video)](https://www.youtube.com/watch?v=Tw5q-SN9ZM8)
* [Add an SSH Key on Github (3:07 minute YouTube video)](https://www.youtube.com/watch?v=WgZIv5HI44o)
* [Using SSH Keys with Github (13:12 minute YouTube video)](https://www.youtube.com/watch?v=nQDFBd5NFA8)

You will need to follow Github's official documentation here for adding an
SSH key to Github:

* [Connecting to GitHub with SSH](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh)

Their documentation is the official way I recommend to do it. Please attempt
the entire instructions on that page yourself, and if you cannot follow them,
please file an issue on the `zero-to-ai`
[issues](https://github.com/jcranston/zero-to-ai/issues) page and indicate
what I can do to help make this process less confusing.

A word of caution: when generating an SSH key-pair using `ssh-keygen`, do NOT
store your private SSH key anywhere else, including on the internet (like on
Github). Your private keys should always be on your machine and nowhere else.
As soon as your private keys are shared, all connections using that key will
be compromised.

[next: Install the Codebase for `zero-to-ai`](./codebase-install.md)
