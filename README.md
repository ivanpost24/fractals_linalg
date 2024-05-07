# fractals_linalg

Playing with fractals :)

## How to get the project set up on your computer

First make sure you have Git installed and your GitHub account set up properly. Follow
[this tutorial](https://github.com/arpost/learning-git-and-github) if you haven't done that yet.

Then you can get the project onto your computer by running this Terminal command in the directory you want the
project folder to be placed (you'll need to `cd` into that directory):
```shell
git clone git@github.com:luximus/fractals_linalg.git
```
Alternatively, using VS Code you can click the "Clone Git repository" button on the welcome screen, choose to
clone a Git repository, sign in, and then choose the repository.

Once you've done that, you'll want to create a new virtual environment so all the packages we're installing don't
pollute your main environment. In the base project folder (fractals_linalg), run the following command:
```shell
python3 -m venv .venv
```
Then run
```shell
source .venv/bin/activate
```
to activate your virtual environment for the Terminal session.

Finally run
```shell
pip install -r requirements.txt
```
to install all the packages you'll need. If we install new packages, you'll need to run this command again later.

I can show you how to set everything up in your VS Code environment as well.

## Navigating around

All main program code should be placed in the `fractals/__main__.py` file. We'll also want to split things up into
other files at some point. If you want to import something from another file in the `fractals` directory, use
the following import statement:
```python
from fractals import ...  # name of file here, without the .py
```

