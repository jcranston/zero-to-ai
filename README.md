# zero-to-ai

## Current Project Status
Please note that `zero-to-ai` is actively under development and not in its
final stage. Please explore the various feature branches for the latest
material: merges to master will be considered official "developments" of the
curriculum and will only come from feature branches.

## Getting Started as a Student
Please follow the instructions in
[Getting Started as a Student](./docs/setup/getting-started.md) for getting
started with your Python environment setup, checking out the code base, and
beginning `assign0`.

## Contributing as an Instructor

Please refer to the [CONTRIBUTING.md](./CONTRIBUTING.md) document for specific
instructions on how to contribute as a curriculum developer/instructor. Please
note that pushes to `master` are not allowed, and there are specific guidelines
for enabling changes to the code base on `master`.

## Feedback

I hope to see this course evolve as I receive feedback from students
and curriculum contributors, and your feedback is especially important. Please
submit a Github [issue](https://github.com/jcranston/zero-to-ai/issues) in the
`zero-to-ai` project so that we can centralize updates, maintain transparency,
and have a sense of version control and conversation as well.

## About this Project
Zero-to-AI (Z2AI) is an open-source curriculum that introduces Python at a
beginner level (read: zero programming or Unix experience). The assignments in
the course guide a student through various aspects of Python programming,
algorithmic design, and software engineering principles, with a flavor of "AI"
specific problems.

### Audience
I am developing Z2AI open-source as an introductory Python
curriculum for my larger group at work, with sign-off from my teammates
and superiors. Once developed, the curriculum is meant to provide a learning
framework for investors, researchers, and portfolio managers to learn the
skills necessary for conducting independent analysis with scientific data. 

### Assignments and Learning Goals
There are eight assignments (named `assign0` through `assign7`) administered
as subdirectories of this code base. Each assignment is composed of student
assignment code and testing directories, which is meant to reflect the flavor
of industry/production-based Python project directories.

Zero to AI is meant to teach the following concepts through eight project-based
assignments (please note, these are subject to change slightly with time):
* `assign0`: Introduce control flow in code, code decomposition, checking out 
a code repository from Github, source control, running tests, and basic
algorithmic thinking. `assign0` uses Stanford's Karel framework but with
different assignments.
* `assign1`: Python language features up to but not including data structures.
Test driven design and debugging.
* `assign2`: Python data structures (set, lists, dicts) with an emphasis on
implementing linear algebra computations and basic statistics.
* `assign3`: Recursion. Explore some of the classic recursive problems and ways
of problem solving through algorithmic design in Python.
* `assign4`: String manipuation: this assignment will piece together knowledge
of data structures and algorithms and introduce string manipulation in Python
with the "shortest common superstring" problem.
* `assign5`: I/O in Python, including Unix pipes and redirects, `cat`, Python
context managers and annotations, `mkdir`, etc. Execute meaningful linear
algebra computations from data sources and write files out to disk locally.
* `assign6`: AI algorithms with computation executed locally, but data sources
fetched remotely (exact location TBD, likely AWS).
* `assign7`: Final assignment. The final assignment will culminate as a
project and most likely be related to student interest as it applies to their
specific application for learning Python and ML. Candidates include building
a financial portfolio and modeling portfolio holdings, designing a support
vector classifier or regression. Project should be robust and demonstrate the
principles from the previous seven assignments.

### Qualifiers
Z2AI is not meant to replace a computer science education or any rigorous
classwork in statistics, mathematics or machine learning. Rather, it is a
"steel thread" to implementing a robust piece of artificial intelligence
software, mostly guided by student interest (`assign7`). I will frequently
refer to existing documentation and sources elsewhere such as YouTube videos
or articles where necessary as opposed to "reinvent the wheel". My goal is to
carefully curate material to help drive towards a robust final assignment, as
opposed to recreate material that likely already exists in better form
elsewhere.

In this sense, Z2AI exists as a code repository to help guide learning
through assignments, while each assignment instruction will lay the groundwork
and educational material by referencing concepts taught elsewhere via links.
Where appropriate, I will compile and present educational concepts that I feel
are appropriate for the specific assignments or concepts.