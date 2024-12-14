# sml00

Shared space for ML hello-worlds.

* [Setting up your tools](https://github.com/ghst659/sml00/blob/main/py_setup.md)
  in `${HOME}/p3`.
* [Setting up SSH access on github](https://github.com/ghst659/sml00/blob/main/ssh_setup.md)
* Using SSH to work on this repository:

  1. Activate the python virtual envronment.

     ```
     $ source ${HOME}/p3/bin/activate
     ```

  2. Clone to your computer, and change to that working dir.

     ```
     (p3) $ git clone git@github.com:ghst659/sml00.git`
     (p3) $ cd sml00
     ```

  3. Running the quickstart Jupyter notebook

     1. Start the notebook server, typically at `http://localhost:8888`.
        ```
        (p3) $ jupyter notebook
        ```

     2. Inside the opened webpage, use File > Open... to open the
        `torch_quickstart.ipynb` notebook.

     3. When done, in the notebook, File > Close and Shut Down Notebook

     4. In the Jupyter home page (`http://localhost:8888`),
        shut down the server with File > Shut Down

  3. Work normally with edits, `git add`, `git commit` etc.

  4. Push to the `origin/main` branch.

     ```
     (p3) $ git push
     ```
