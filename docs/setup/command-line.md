# Step 1: The Command Line

[Getting Started as a Student](./getting-started.md)

[next: Create a Github Account](./create-github-account.md)

There are ample tutorials on getting started using a command line. I'm not
going to reinvent the wheel here. You can spend as little or as much time as
you want exploring Unix via a terminal. For the purpose of this project, I am
not going to teach Unix except for specific commands where they are necessary
for the purpose of completing the assignment. If you are interested in reading
further, please Google search or look on YouTube for videos on "Unix commands".

Having a sense of the difference between "Linux", "Unix", "Shell", "Terminal",
and "Operating System" are good to have as well.

## Terminal Software
I recommend using
[iTerm2](https://www.iterm2.com/) on a Mac. The Terminal in Linux is just fine.
But, this does not matter for what we are doing.

## Shell
A shell is the software interface that powers your command line and enables
you to interact with your operating system. A terminal like iTerm is a
1-to-many concept when it comes to shells: iTerm can run the shell `bash`, or
`zsh`, or `csh`, etc. The shell is just the software running that powers your
command line interface, which is hosted in a terminal application like iTerm.

Please feel free to use whichever shell you are comfortable with. I recommend
using `bash` if you are new to the command line. Personally, I use `zsh` but it
does not matter. Please use your preferred command line application for running
the various commands I describe in this (and subsequent) documentation.

I will usually describe commands to be entered at the command line using
preformatted text, such as `ls -lsah ~`. I will do my best to make commands
operating system and shell-agnostic, and indicate differences where necessary
between Linux and Mac. Please file an
[issue](https://github.com/jcranston/zero-to-ai/issues) if a specific command
is not working or you are running into problems.  

## Learning Resources
You can spend as much or as little time glamming out your shell customizations.
For the purpose of this project, you do not need to do any customizations.
I recommend perusing the following resources until you are comfortable with
basic Unix commands like `cd`, `ls`, `rm`, `mkdir`, etc. The internet and a
Google search are your best resources if you are confused about a specific
command.

Here are some resources I found that I think are helpful for getting used to
the command line (some are for Linux, some for Mac, but both have large
overlaps and are relevant for either OS. After all, macOS is built on Darwin,
which is a version of the Unix operating system).
* https://lifehacker.com/a-command-line-primer-for-beginners-5633909
* https://ubuntu.com/tutorials/command-line-for-beginners#1-overview
* https://www.davidbaumgold.com/tutorials/command-line/
* Finally, YouTube is a fantastic resource.

## Create your `sandbox` Directory
From the command line, issue:
```bash
cd ${HOME}
```
Here, `HOME` is a bash variable that stores the location of your home
directory, and `${}` is bash syntax for extracting the value from that
variable. Another alias for your home directory is `~`, which is more
commonly used, so you can also switch to your home directory by using
```bash
cd ~
```
Here, `cd` is the Unix command to "change directories". Once you've done this,
issue a
```bash
pwd
```
The `pwd` Unix command will "print your working directory". If you are ever
confused about a specific Unix command, just issue
```bash
man pwd
```
(or whatever command you are trying to learn about). `man` opens the manual
pages for specific commands.

Now that you are in your home directory (`~`), you can list contens as follows
using `ls`:
```bash
ls
```
Alternately, you can supply `ls` with different flags to display different
information about the files and directories stored at your current working
directory, such as:
```bash
ls -lsah
```
To read about each flag, issue a `man ls`. There are many!

Now, in your home directory, you will create the `sandbox` directory, which is
where we are going to install the code for `zero-to-ai` in the next
documentation page you will read. Issue:
```bash
mkdir sandbox
```
Now, you can move into the `sandbox` directory with a:
```bash
cd sandbox
```
and list the contents using:
```bash
ls -lsah .
```
The `.` at the end of the command means "the current working directory". So
here you are listing all the contents of the `sandbox` directory. If `.` is not
supplied, it is inferred to be the current working directory. However, it could
be any other location on your machine as well: you do not need to be inside
the directory you are trying to list the contents of.

To verify you are in the correct location, issue `pwd` again. You should
see that you are in the `sandbox` directory within your home directory.

[next: Create a Github Account](./create-github-account.md)
