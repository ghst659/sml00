# Python Setup

## Overview

1. Install your own Python3 separate from the computer's system
   python installation.
2. Use the new Python3 installation to start a **virtual Python
   environment** in your homedir.
3. Activate the virtual environment; this will cause all Python
   commands to use the virtual environment.
4. Install the additional Python packages into the virtual
   environment.
5. Using the Environment

   + Each time you want to use the environment,
     re-activate it from your shell.
   + Running Jupyter Notebook.

## 1. Install Own Python3

### macOS

1. Check original system python location.
   ```
   $ which python3
   ```
2. Install Python3
   ```
   $ brew install python
   ```
3. Confirm the new python path is different from the original
   system path.
   ```
   $ which python3
   ```

### Linux

1. Download Python source `.tar.xz` file from https://www.python.org/
2. Uncompress and untar
3. Configure
   ```
   $ CC=$(which clang) ./configure --prefix=/opt/python-3.12.6 --with-ensurepip=upgrade
   ```
4. Build
   ```
   $ make -j 4
   ```
5. Install
   ```
   $ make -j 4 install
   ```

## 2. Create Virtual Environment based on the Python

This is done so that all the additional package installs (which will
change over time) will not affect the above Python installation.

The virtual environment will be installed in `$HOME/p3`

```
$ python3 -m venv "${HOME}/p3"
```

## 3. Activate (Use) the Virtual Environment

This causes the current shell to use the virtual environment as the
python3 directory.  The shell prompt will get a `(p3)` prefix.

```
$ source ${HOME}/p3/bin/activate
(p3) $
```

The shell prompt should change to have a `p3` prefix.

Verify that the path to `python` and `pip` are now under `${HOME}/p3`.

```
(p3) $ which python
(p3) $ which pip
```

Install/update the Python modules needed to install packages.

```
(p3) $ pip install -U pip setuptools wheel
```


## 4. Install Packages from PyPI

This installs the additional PyPI packages into the virtual
environment so that the new python stays clean.

```
(p3) $ pip install -U numpy matplotlib pandas pandas-datareader notebook torch tensorflow-cpu
```

## 5. Using the Virtual Environment

### Activate and Deactivate

To start using the virtual environment, activate it, the shell prompt
will get a `(p3)` prefix

```
$ source ${HOME}/p3/bin/activate
(p3) $
```

To stop using the virtual environment, deactivate it; the `(p3)`
prompt prefix will disappear.

```
(p3) $ deactivate
$ 
```

### Running Jupyter

To start the Jupyter notebook server run `${HOME}/p3/bin/jupyter`
after activating the virtual environment.

```
(p3) $ jupyter notebook
```

which will start the server in the terminal session, then open a
browser window pointing to the server at `localhost:8888`.

The working directory is the location where you invoked `jupyter`.
