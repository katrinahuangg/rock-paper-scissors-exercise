# rock-paper-scissors-exercise

An example Python application to play rock, paper, scissors against a computer.

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository] (https://github.com/katrinahuangg/rock-paper-scissors-exercise) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd rock-paper-scissors-exercise
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-game-env":

```sh
conda create -n my-game-env python=3.8
conda activate my-game-env
```

From inside the virtual environment, install package dependencies:

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above)

## Setup

In in the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username:

    USER_NAME="John Snow"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [.gitignore](/.gitignore) file)

## Usage

Run the game script:

```py
python game.py

# alternative module-style invocation (only required if importing from one file to another):
python -m app.game
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment

