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

Each time you want to use the environment, re-activate it from your shell.

## Install Own Python3

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

## Create Virtual Environment based on the Python

This is done so that all the additional package installs (which will
change over time) will not affect the above Python installation.

The virtual environment will be installed in `$HOME/p3`

```
$ python3 -m venv "${HOME}/p3"
```

## Activate (Use) the Virtual Environment

This causes the current shell to use the virtual environment as the
python3 directory.

```
$ source ${HOME}/p3/bin/activate
```

The shell prompt should change to have a `p3` prefix.

Verify that the path to `python` and `pip` are now under `${HOME}/p3`.

```
$ which python
$ which pip
```
