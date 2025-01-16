# Development setup

If you only want to test RDMO you can use the regular [installation](../installation/index.md#installation) with the [development server](../deployment/development) to run RDMO on your laptop or workstation. In this case, the main `rdmo` Python package is installed from PyPI, just like in the production setup and cannot be edited.

This setup should also suffice when you want to work on [themes](../themes/index.md#themes) or [plugins](../plugins/index.md#plugins) (see also the bottom of this page). 

The deveopment setup described here, can be used to work on all parts of RDMO, in particular the source code of the `rdmo` package and the front-end components written in JavaScript.

## Install prerequisites

Install the prerequisites for your system as described [for the regular setup](../installation/prerequisites.md#install-prerequisites).

## Obtain repositories

First create a directory called `rdmorganiser` somewhere where you usually put your coding projects.

```bash
mkdir path/to/rdmorganiser
cd path/to/rdmorganiser
```

Next clone the `rdmo-app` and the `rdmo` repositories from GitHub. If you have an account there, and [added your public SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) you can use:

```bash
git clone git@github.com:rdmorganiser/rdmo-app
git clone git@github.com:rdmorganiser/rdmo
```

Otherwise you can clone the repos using:

```bash
git clone https://github.com/rdmorganiser/rdmo-app
git clone https://github.com/rdmorganiser/rdmo
```

You should now have two directories in `rdmorganiser`:

```
📂 path/to/rdmorganiser
 ┣ 📂 rdmo
 ┃ ┣ ...
 ┣ 📂 rdmo-app
 ┃ ┣ ...
```

## Setup rdmo-app

Change into `rdmo-app` and create a Python virtual environment:

```{eval-rst}
.. tabs::

   .. code-tab:: bash Linux/MacOS

      cd rdmo-app
      python3 -m venv env 
      source env/bin/activate
      pip install --upgrade pip setuptools        

   .. code-tab:: bash Windows

      cd rdmo-app
      python3 -m venv env 
      source env/Scripts/activate
      pip install --upgrade pip setuptools

   .. code-tab:: powershell Windows

      cd rdmo-app
      python3 -m venv env 
      call env\Scripts\activate.bat
      pip install --upgrade pip setuptools
```

Install `rdmo` in _editable_ mode incl. dev-dependencies:

```
pip install -e ../rdmo
pip install -e ../"rdmo[dev]"
```

This links the cloned `rdmo` repo in a way that changes to the code will be available to the development server instantly.

Create a copy of `sample.local.py` with the name `local.py`:

```bash
cp config/settings/sample.local.py config/settings/local.py
```

In the new file, set `DEBUG = True` and configure the `DATABASE` entry. The simplest way is to use Sqlite3:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}
```

If you want to use PostgreSQL or MySQL for the development you need to install the Python dependencies for this as well.

```
pip install -e ../"rdmo[postgres]"
pip install -e ../"rdmo[mysql]"
```

Since the testing data that comes with RDMO use a simpler password hashing algorithm, you need to add the following to
the settings as well:

```python
PASSWORD_HASHERS = ("django.contrib.auth.hashers.MD5PasswordHasher",)
``` 

If you want to use the browsable API, that comes with the Django Rest Framework add:

```python
from rdmo.core.settings import REST_FRAMEWORK

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)
```

Then, initialize the application, using:

```bash
python manage.py download_vendor_files  # download front-end vendor files
python manage.py migrate                # initializes the database
python manage.py setup_groups           # optional: create groups with different permissions
```

The testing data can be imported using:

```{eval-rst}
.. tabs::

   .. code-tab:: bash Linux/MacOS/Windows

      python manage.py loaddata ../rdmo/testing/fixtures/*     

   .. code-tab:: powershell Windows

      python manage.py loaddata ..\rdmo\testing\fixtures\accounts.json ^
                              ..\rdmo\testing\fixtures\conditions.json ^
                              ..\rdmo\testing\fixtures\domain.json ^
                              ..\rdmo\testing\fixtures\groups.json ^
                              ..\rdmo\testing\fixtures\options.json ^
                              ..\rdmo\testing\fixtures\overlays.json ^
                              ..\rdmo\testing\fixtures\projects.json ^
                              ..\rdmo\testing\fixtures\questions.json ^
                              ..\rdmo\testing\fixtures\sites.json ^
                              ..\rdmo\testing\fixtures\tasks.json ^
                              ..\rdmo\testing\fixtures\users.json ^
                              ..\rdmo\testing\fixtures\views.json

```

The test upload files are initialized using:

```{eval-rst}
.. tabs::

   .. code-tab:: bash Linux/MacOS/Windows

      cp -r ../rdmo/testing/media media_root

   .. code-tab:: powershell Windows

      xcopy ..\rdmo\testing\media media_root /e/s
```

Starting from RDMO `2.0.0` we use [webpack](https://webpack.js.org/) to bundle the new React based front-end. For this [nodejs](https://nodejs.org) needs to be available. The preferred way is to use [nvm.sh](https://github.com/nvm-sh/nvm). On (regular) Windows, Node JS needs to be installed like the other [prerequisites](../installation/prerequisites) and the `nvm` part can be skipped here.

`nvm.sh` can be installed for the current user with:

```
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
```

After the installation add:

```
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
```

to your `.bashrc`. Then, inside of your `rdmo` repository, run:

```
cd ../rdmo
nvm install    # only once, to install the node version given in .nvmrc
nvm use        # to activate the node version
```

Then `npm` can be used to download and install the javascript dependencies and build the front-end:

```
npm install    # to install the many, many javascript dependencies
npm run watch  # to build the front-end and rebuild it when changing the source
```

Now the development server can be started (in a different terminal) using:

```
python manage.py runserver
```

You can access the application at http://localhost:8000 in your browser and can log in using different users:

```
admin    -> superuser
site     -> site manager

editor   -> member of the editor group
reviewer -> member of the reviewer group
api      -> member of the api group

owner    -> owner of the test projects
manager  -> manager of the test projects
author   -> author of the test projects
guest    -> guest of the test projects

user     -> user without project
other    -> another user without project
```

The password for these users is the same as the username, e.g. `admin`: `admin`. You might have guessed yourself, but make sure to **never use these users in a production environment**.

A local email server for development can be started by setting:

```python
# in local.py
EMAIL_PORT = 8025
```

and using:

```bash
# for python versions >= 3.7
pip install aiosmtpd

python -m aiosmtpd -n -l localhost:8025
```

## Setup rdmo

In order to run the test suite, the `rdmo` repo itself can be setup in a similar way in its own virtual environment:


```{eval-rst}
.. tabs::

   .. code-tab:: bash Linux/MacOS

      deactivate                                  # if you are already in an env
      cd path/to/rdmorganiser/rdmo
      python3 -m venv env 
      source env/bin/activate
      pip install --upgrade pip setuptools        

   .. code-tab:: bash Windows

      deactivate                                  # if you are already in an env
      cd path/to/rdmorganiser/rdmo
      python3 -m venv env 
      source env/Scripts/activate
      pip install --upgrade pip setuptools

   .. code-tab:: powershell Windows

      deactivate                                  # if you are already in an env
      cd path\to\rdmorganiser\rdmo
      python3 -m venv env 
      call env\Scripts\activate.bat
      pip install --upgrade pip setuptools
```

Again install `rdmo` in editable mode and install the database prerequisites:

```
pip install -e .

pip install ".[postgres]"                   # for PostgreSQL
pip install ".[mysql]"                      # for MySQL
```

Create a `local.py` as before, but this time in `testing/config/settings/local.py`:

```bash
cp testing/config/settings/sample.local.py testing/config/settings/local.py
```

Create a log directory:

```bash
mkdir testing/log
```

Now you can run the test using:

```
pytest
```

More about testing can be found [here](testing.md).

## Setup plugins

In order to include plugins into the development setup simply clone the plugin repository next to `rdmo` and `rdmo-app`, e.g. for `rdmo-plugins`:


```{eval-rst}
.. tabs::

   .. code-tab:: bash HTTPS

      git clone https://github.com/rdmorganiser/rdmo-plugins

   .. code-tab:: bash SSH

      git clone git@github.com:rdmorganiser/rdmo-plugins
```

Then the plugin can be added to the `env` for `rdmo-app` or `rdmo` also in _editable_ mode using:

```bash
pip install -e ../rdmo-plugins
```

The plugin itself needs to be added to the `local.py` as described [in the documentation](../../plugins/index).
