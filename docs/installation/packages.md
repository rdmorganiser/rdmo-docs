# Install Python packages


After you have obtained the `rdmo-app`, you need to install the `rdmo` package and the other python dependencies.

Change to the `rdmo-app` directory and create a [Virtual Environment](https://docs.python.org/3/tutorial/venv.html) (this is done as your user or the created `rdmo` user, not as `root`):


```{eval-rst}
.. tabs::

   .. code-tab:: bash/zsh Linux/MacOS

      cd rdmo-app
      python3 -m venv env 
      source env/bin/activate
      pip install --upgrade pip setuptools        

   .. code-tab:: bash Windows

      cd rdmo-app
      python3 -m venv env 
      source env/Scripts/activate
      pip install --upgrade pip setuptools

   .. code-tab:: cmd/pwsh Windows

      cd rdmo-app
      python3 -m venv env 
      call env\Scripts\activate.bat
      pip install --upgrade pip setuptools
```

After the virtual environment is activated and `pip` was upgraded, the `rdmo` package can be installed using `pip`:

```bash
pip install rdmo
```

The virtual environment encapsulates your RDMO installation from the rest of the system. This makes it possible to run several applications with different python dependencies on one machine and to install the dependencies without root permissions.

**Important:** The virtual environment needs to be activated, using `source env/bin/activate` or `call env\Scripts\activate.bat`, every time a new terminal is used.
