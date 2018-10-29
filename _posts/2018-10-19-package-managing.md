---
title: Package Managing in Python
date: 2018-10-19T16:35:28+02:00
---

**Notice!** This page is still in progress!
{: .notice--primary}

# Package Managing in Python

This is a short overview of package managing in python utilizing pip, pipenv, virtualenv and anaconda.
The general workflow while working on python projects can be visualized by this steps:

1. Create virtual environment   (if not already present)
2. Activate virtual environment
3. Install required packages    (if needed)
4. Do all the coding/testing etc.
5. Deactivate virtual environment

## Setting up a Virtual Environment

First it is important to create a virutal environment for your project, mostly because of specified package dependencies
(some packages only work on specific python versions whereas others do not) and/or to avoid name conflict in your
python modules and packages.

### Virtualenv Environment

### Pipenv Environment

### Conda Environment

When doing data science it is most recommand to utilize [Anaconda](https://www.anaconda.com/). It is a very
popular package managing tool which comes with all the most important data science tools like numpy, pandas,
scipy, scikit-learn and matplotlib and solves all the dependency issues regarding those packages.
Before we can start you have to download [anaconda](https://www.anaconda.com/download/). Select your OS and your prefered
python version (at this point I would recommand python 3.6) and click on `Download`.

#### Create the virtual environment

To create an anaconda virtual environment you can either use the anaconda GUI or do it using the terminal.
For me the terminal is the most straight forward way and it's pretty easy as well.
When in terminal you just have to type in

```sh
conda create -n EnvName                  # creates an virtual environment named EnvName
conda create -n EnvName python=3.7       # specifies python version to 3.7
conda create --clone EnvName -n Env2     # creates an exact clone of EnvName named Env2
```

to create your anaconda environment. For this to work you have to make sure your anaconda folder is linked to your PATH.
Normaly you will be asked during the installation process if you want to add anaconda to your path. If that is not working for you for some 
reason you have to set it manually.  You can do this on Windows by typing `PATH=%PATH%;C:\Anaconda3;C:\Anaconda3\Scripts\` depending 
where your anaconda folder is located. On Linux and MaxOS open your `.bashrc` and add the line `export PATH="/<path to anaconda>/bin:$PATH"`.
For more infos and help on the installation process see the [Anaconda FAQ](https://docs.anaconda.com/anaconda/faq/).

To view all your conda environments you can either type `conda info --envs` or `conda env list`. It is also possible to save your environment as a txt file
`conda list --explicit > EnvName.txt` and/or to built your environment using a txt file `conda env create --file EnvName.txt`.
If you want to see what packages are installed in your  environemnts you can type `conda list -n EnvName` or in case your environment is already 
activated (see next chapter) `conda list`. When using conda
and your environment is not yet activated you have to specify all your conda commands by adding the `-n EnvName` or `--name EnvName` flag.

#### Update packages in your enviornment

Anaconda offers an easy way to update packages using the `conda update` command. For example:

```sh
conda update conda                  # updates anaconda to the most recent version
conda update SomePackage            # updates SomePackage in MyEnv (if already activated)
conda update -n MyEnv SomePackage   # updates SomePackage in MyEnv
conda update  --all                 # updates all packages in MyEnv (if already activated)
conda update -n MyEnv --all         # updates all packages in MyEnv
```

If you want to delete your conda environment type `conda remove -n EnvName`.

Anaconda offers a cheat sheet for the most useful tasks: [Conda CheatSheet](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)

**Notice!** You can also use pip installs in your conda virtual environment! (see the pip install chapter)
{: .notice--info}

## Activate/Deactivate Virtual Environment

Before working in your environment you have to activate it.
Activating and deactivating your environments is independent of your used package managing tool.
The basic commands are:

```sh
source activate EnvName # activates EnvName
source deactivate       # deactivates EnvName
```

for Linux and MacOS and on Windows:

```sh
activate EnvName    # activates EnvName
deactivate          # deactivates EnvName
```

## Package Installation

### Pip Install

The packages for pip installs will be requested from the official [PyPi website](https://pypi.org).
Most common option flags for pip installs.

```sh
pip install SomePackage           # installs latest version
pip install SomePackage==1.0.4    # specific version
pip install SomePackage>=1.0.4  # minimum version
pip install -r requirements.txt   # install all packages specified in the requirements.txt file
pip install -U SomePackage        # upgrades installed package
pip install --pre SomePackage     # installs the pre-release version
```

See the examples provided on [pip.pypa.io](https://pip.pypa.io/en/stable/reference/pip_install/#examples) for more information.

**Tipp!** If you want to use a project hosted on [GitHub](https://github.com) and this project has not (yet) a
suported or updated version on PyPi or Anaconda but a `setup.py` file and a `requirments.txt` file you can install it by using the command
`pip install git+https://github.com/UserName/Package`. This will install the project into your currently activated environment.
{: .notice--info}

### Pipenv Install


### Conda Install

The packages for conda installs will be requested from the [Anaconda website](https://pypi.org).
Most common option flags for conda installs.

```sh
conda install --help                 # command line help
conda install SomePackage             # installs latest version
conda install -y SomePackage          # ignores confirmation
conda install -f SomePackage          # force installation even if the package is already installed
conda install -n EnvName SomePackage # installs package into the specified environment
conda install SomePackage==1.0.4     # specific version
pip install SomePackage>=1.0.4     # minimum version
pip install -r requirements.txt      # install all packages specified in a requirements.txt file
pip install --upgrade SomePackage    # upgrades installed package
pip install --pre SomePackage        # installs the pre-release version
```

### Import package

