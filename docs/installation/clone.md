# Obtaining the app directory

The next step is to create the `rdmo-app` directory by cloning the corresponding repository into the home directory of your `rdmo` user:

```bash
git clone https://github.com/rdmorganiser/rdmo-app
```

Note that this is not the main `rdmo` repository, only the configuration files. Inside this directory, you will find:

* a `config` directory, containing the main settings of your RDMO installation, and
* a `manage.py` script, which is the main way to interact with your RDMO installation on the command line. Most of the following steps will use this script.

The idea is, that all your (future) configurations and extensions reside in the `rdmo-app` directory. It is therefore recommended to use Git versioning on your side for this repo (i.e. to fork the `rdmo-app` repository) and to store it either on GitHub or a similar suited repository system.

The `rdmo-app` directory corresponds to a [project](https://docs.djangoproject.com/en/stable/intro/tutorial01) in Django terms.
