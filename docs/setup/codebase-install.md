# Step 3: Install the Codebase for `zero-to-ai`

[Getting Started as a Student](./getting-started.md)

[previous: Create a Github Account](./create-github-account.md)

[next: Pycharm Installation](./pycharm-install.md)

Now that you've created a Github account and installed a public SSH key onto
your account, you are ready to check out the code base!

Switch into your `sandbox` directory (please see previous instructions on
creating this directory if you have not done so):
```bash
cd ~/sandbox
```
Now, clone the git repository from the remote on Github:
```bash
git clone git@github.com:jcranston/zero-to-ai.git
```
You should now be on the master branch. You can issue:
```
git branch
```
to see the list of local Git branches you have available. For now, you will
only have the `master` branch. As time goes on and you work on different
assignments, you will have more branches.

I will do my best to tell you the git commands you need in the setup and
assignment documentation when you are working in `zero-to-ai`. I'm not here to
teach you git, only to help you use it to complete your assignments. On its
own, git is a truly complex piece of software that takes years to feel any
sanity using (so don't worry if it feels confusing).

Google is your friend. Also, here are some references for starters:
* [How to use Git and Github (12:18 minute YouTube video)](https://www.youtube.com/watch?v=HkdAHXoRtos)
* [Official Git Tutorial](https://git-scm.com/docs/gittutorial)

Once you have `zero-to-ai` installed, you can search for it in your `sandbox`
directory with `ls -lsah`.

Now, move into the `zero-to-ai` directory:
```bash
cd zero-to-ai
```
Issue `ls -a` again and you will see the top-level contents of the
directory (which is also what you see if you visit the page on Github):
 ```bash
✗ ls -a
total 40
 0 drwx------   9   288B Aug 11 17:57 .
 0 drwxr-xr-x  16   512B Aug  8 23:01 ..
 0 drwx------  15   480B Aug 11 18:37 .git
 8 -rw-------   1   232B Aug  9 02:32 .gitignore
 0 drwxr-xr-x   8   256B Aug 11 18:40 .idea
16 -rw-------   1   5.2K Aug 11 15:31 CONTRIBUTING.md
16 -rw-------   1   5.0K Aug 11 17:57 README.md
 0 drwx------   8   256B Aug 11 17:57 docs
 0 drwx------  11   352B Aug 11 17:57 python
 ```
Since this is a git directory, there is a `.git` directory and `.gitignore`
file within the `zero-to-ai` directory. The `.git` directory keeps track of
information needed to maintain version control of the software, such as commits
and branches. The `.gitignore` file specifies which directories and file
patterns within the `zero-to-ai` directory and corresponding subdirectories to
ignore in version control.

All `make` targets for `zero-to-ai` must be issued in the `python` directory,
where the `Makefile` is stored. You will use `make` targets to run tests
and issue other commands to interact with the codebase.

Here are some references for git commands:
* [Official git documentation](https://git-scm.com/docs)
* [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
* [Alvin Alexander's Git Command Reference (this one is good)](https://alvinalexander.com/git/git-cheat-sheet-git-reference-commands/)
* [Git Tutorial for Beginners (30:32 minute YouTube video)](https://www.youtube.com/watch?v=HVsySz-h9r4)
* [Git Commands With Examples (29:53 minute YouTube video)](https://www.youtube.com/watch?v=b5oQZdzA37I)

[next: Pycharm Installation](./pycharm-install.md)
