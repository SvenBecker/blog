---
title: Package Managing in Python
date: 2018-10-19T16:35:28+02:00
header:
   overlay_image: /assets/images/galleries/g1_overlay.jpeg
   teaser: /assets/images/galleries/g1_teaser.jpeg
excerpt: How to efficiently manage the dependencies in your Python projects. A short introduction to virtual environments and package installation.
---

# Package Managing in Python

**Notice!** This page is still in progress!
{: .notice--primary}

This is a short overview of package managing in python utilizing *pip*, *virtualenv*, *pipenv* and *anaconda*.
The general workflow while working on python projects can be visualized by this steps:

1. Create a virtual environment         (if not already present)
2. Activate the virtual environment
3. Install all the required packages    (if needed)
4. Do all the coding/testing etc.
5. Deactivate the virtual environment

# Setting up a Virtual Environment

First it is important to create a virutal environment for your project, mostly because of specified package dependencies
(some packages only work on specific python versions whereas others do not) and/or to avoid name conflict in your
python modules and packages.

## Virtualenv Environment

You have to install `virtualenv` if it is not already present. You can do it by using a pip install:

```sh
pip install virtualenv  # installs the virtualenv package
```

Virtualenv has basically only one real command:

```sh
virtualenv EnvFolder  # create a virtual environment
```

This file create a folder containing your virtual environment defined by *EnvFolder*.
*EnvFolder* consists of the path to the virutal environment directory and the virtual environment name.
Say I want to create a virtual environment named *EnvName* and I want to have it located in my Documents folder
I would have to type:

```sh
virtualenv ~/Documents/EnvName
```

*EnvName* will be a folder containing some subfolders depending on your OS. To activate the example virtual environment 
you have to use the command:

```sh
source ~/Documents/EnvName/bin/activate # normal activation
.~/Documents/EnvName/bin/activate       # if source command is not available
```

On Windows it is a littl bit different. The activation file on Windows is located in the `Script` folder in your environment directory `\path\to\EnvName\Scripts\activate`.

To deactivate the virtual environment you just have to use the command `deactivate` and to remove the
deactivated environment you can manually select the directory and delete it or use the command `rm -r /path/to/EnvName`.
See the [official Docs](https://virtualenv.pypa.io/en/latest/userguide/) for more information.

## Pipenv Environment

> Pipenv is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world.

[Pipenv](https://pipenv.readthedocs.io/en/latest/) is a much more versatile way to manage your virtual environments as well as your packages contained in those environments. It combines *pip*, *virtualenv* and *PipFile*.

For non scientific projects I would highly recommand using Pipenv.

## Conda Environment

But when doing data science it is most recommand to utilize [Anaconda](https://www.anaconda.com/). It is a very
popular package managing tool which comes with all the most important data science tools like numpy, pandas,
scipy, scikit-learn and matplotlib and solves all the dependency issues regarding those packages.
Before we can start you have to download [Anaconda](https://www.anaconda.com/download/). Select your OS and your prefered
python version (at this point I would recommand python 3.6) and click on `Download`.

### Create the virtual environment

To create an Anaconda virtual environment you can either use the Anaconda GUI or do it using the terminal.
For me the terminal is the most straight forward way and it's pretty easy as well.
When in terminal you just have to type in

```sh
conda create -n EnvName                  # creates an virtual environment named EnvName
conda create -n EnvName python=3.7       # specifies python version to 3.7
conda create --clone EnvName -n Env2     # creates an exact clone of EnvName named Env2
```

to create your Anaconda environment. For this to work you have to make sure your Anaconda folder is linked to your PATH.
Normaly you will be asked during the installation process if you want to add Anaconda to your path. If that is not working for you for some 
reason you have to set it manually.  You can do this on Windows by opening the Command Prompt or Powershell and typing `PATH=%PATH%;C:\Anaconda3;C:\Anaconda3\Scripts\` depending 
where your Anaconda folder is located. On Linux and MaxOS open your `.bashrc` and add the line `export PATH="/<path to anaconda>/bin:$PATH"` to your `.bashrc` file.
For more information and help on the installation process see the [Anaconda FAQ](https://docs.anaconda.com/anaconda/faq/).

To view all your conda environments you can either type `conda info --envs` or `conda env list`. It is also possible to save your environment as a txt file
`conda list --explicit > EnvName.txt` and/or to built your environment using a txt file `conda env create --file EnvName.txt`.
If you want to see what packages are installed in your  environemnts you can type `conda list -n EnvName` or in case your environment is already 
activated (see next chapter) `conda list`. When using conda
and your environment is not yet activated you have to specify all your conda commands by adding the `-n EnvName` or `--name EnvName` flag.

To activate or deactivate your virtual environment on Linux and MacOS open your Terminal and type:

```sh
source activate EnvName # activates EnvName
source deactivate       # deactivates EnvName
```

On Windows open your Command Prompt or Powershell and type:

```sh
activate EnvName    # activates EnvName
deactivate          # deactivates EnvName
```

### Update packages in your enviornment

Anaconda offers an easy way to update packages using the `conda update` command. For example:

```sh
conda update conda                  # updates Anaconda to the most recent version
conda update SomePackage            # updates SomePackage in MyEnv (if already activated)
conda update -n MyEnv SomePackage   # updates SomePackage in MyEnv
conda update  --all                 # updates all packages in MyEnv (if already activated)
conda update -n MyEnv --all         # updates all packages in MyEnv
```

If you want to delete your conda environment type `conda remove -n EnvName`.

Anaconda offers a cheat sheet for the most useful tasks: [Conda CheatSheet](https://conda.io/docs/_downloads/conda-cheatsheet.pdf)

**Notice!** You can also use pip installs in your conda virtual environment! (see the pip install chapter)
{: .notice--info}

# Package Installation

## Pip Install

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

## Pipenv Install

## Conda Install

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

# Import Packages and Modules

## Import Packages

It pretty easy to import packages you have already installed via one of the package management tools listed above.
Just add the line `import SomePackage` to the top of your python file, where you want to use one or more of the utilities provided by the package. Instead you can also specifiy what you want to import.
Let say you want to import the function *printf* which is provided by the package *SomePackage* and located in the
*SomeFile* file. There are multiple ways to import this function. For example:

```python
import SomePackage
# call SomePackage.SomeFile.printf() in your file

from SomePackage.SomeFile import printf
# call printf() in your file

import SomePackage.SomeFile as sf
# call sf.printf() in your file

from SomePackage.SomeFile import *
# call printf() in your file
# import all functions, variables and classes SomeFile provides
# may lead to name conflicts so be careful with this sort of import
  
```

## Import Modules

But you can also import your own modules. For example you defined a useful function in one of your files but want to
use it also in different files. The file which contains the function you want to import is called *module*.
Say your project structure is as following:

```sh
MyProject                 # your project directory => project root
├── main.py               # a python file located at the root
├── subfolder             # regular folder
|  ├── __init__.py        # init file
|  ├── foo.py             # some python file
|  ├── foo2.py            # some python file
|  └── subsubfolder       # regular subfolder
|     ├── __init__.py     # init file
|     └── subfoo.py       # another python file
└── subfolder2            # second folder
   └── __init__.py        # another init file
   └── bar.py             # another python file
```

`__init__.py` just declares the folder where it is located to be a module. It can remain empty.In general there are two ways to import modules; by using relative or absolute imports.

**Notice!** Adding `__init__.py` to your project folders was important in Python 2. In Python 3 it is no longer required!
{: .notice--primary}

### Relative imports

When in `main.py` file:

```python
import subfolder.foo                    # import foo.py
import subfolder.subsubfolder.subfoo    # import subfoo.py
```

When in `foo.py`:

```python
import .subfoo                           # import foo2.py
import subsubfolder.subfoo               # import suboo.py
import ..main                            # import main
import ..subfolder2.bar                  # import bar.py
```

### Absolute Imports

When in `main.py` file:

```python
import MyProject.subfolder.foo                    # import foo.py
import MyProject.subfolder.subsubfolder.subfoo    # import subfoo.py
```

When in `foo.py`:

```python
import MyProject.subfolder.foo2                   # import foo2.py
import MyProject.subfolder.subsubfolder.subfoo    # import foo.py
import MyProject.main                             # import main
import MyProject.subfolder2.bar                   # import bar.py
```

## Importing Modules while using Jupyter Notebooks

There might be some issues with relative and absolute imports when using Jupyter Notebooks. The reason is
that the Jupyter Kernel might not use the same Path your Python interpreter is using.
To fix that problem you can add your project folder to the Jupyter path or you can do it by adding this two lines before
you import any own modules in your notebook:

```python
import sys
sys.path.add("path/to/project")
```

**Notice!** The *path/to/project* may also be relative or absolute!
{: .notice--primary}