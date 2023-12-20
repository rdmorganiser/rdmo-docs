# Databases

RDMO can use any type of database that is supported by the Django web framework. The particular database connection is defined with the setting `DATABASES` in your `local.py`.  
An overview of the Django database settings can be found in the [Django docs](https://docs.djangoproject.com/en/4.2/ref/settings/#databases). For the most typical types of databases, [PostgreSQL](#postgresql), [MySQL](#mysql) and [SQLite](#sqlite), we show here the configuration and [initialization](#initializing-the-database) with the `manage.py migrate` command.

### PostgreSQL

PostgreSQL can be installed using:


```{eval-rst}
.. tabs::

   .. code-tab:: bash Debian/Ubuntu

      sudo apt install postgresql

   .. code-tab:: bash RHEL/CentOS

      sudo yum install postgresql-server postgresql-contrib
      sudo postgresql-setup initdb
      sudo systemctl start postgresql
      sudo systemctl enable postgresql
```

To use PostgreSQL as your database backend install `psycopg2`, via the `rdmo` dependencies, in your virtual environment:

```bash
pip install rdmo[postgres]
```

Then, add the following to your `config/settings/local.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'rdmo',
        'USER': 'rdmo',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```

where `NAME` is the name of the database, `USER` the PostgreSQL user, `PASSWORD` her password, `HOST` the database host, and `PORT` the port PostgreSQL is listening on. Note that, depending on your setup, not all settings are needed. If you are using the peer authentication methods, you only need the `NAME` and `ENGINE` settings. The user and the database can be created using:

```bash
sudo su - postgres
createuser rdmo
createdb rdmo -O rdmo
```

This assumes peer authentication for the rdmo user.
Now you can [initialize your database](#initializing-the-database).

### MySQL


MySQL (or community-developed fork MariaDB) can be installed using:


```{eval-rst}
.. tabs::

   .. code-tab:: bash Debian/Ubuntu

      sudo apt install mysql-client mysql-server libmysqlclient-dev        # for MySQL
      sudo apt install mariadb-client mariadb-server libmariadbclient-dev  # for MariaDB

   .. code-tab:: bash RHEL/CentOS

      sudo yum install -y mysql mysql-server mysql-devel                   # for MySQL
      sudo yum install -y mariadb mariadb-server mariadb-devel             # for MariaDB
      sudo systemctl enable mariadb
      sudo systemctl start mariadb
      sudo mysql_secure_installation
```

To use MySQL as your database backend install `mysqlclient`, via the `rdmo` dependencies, in your virtual environment:

```bash
pip install rdmo[mysql]
```

Then, add the following to your `config/settings/local.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'rdmo',
        'USER': 'rdmo',
        'PASSWORD': 'not a good password',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
            # only if you want to connect over a non-default socket
            'unix_socket': '',
            # only for MySQL 5.7
            'init_command': "SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));"
        }
    }
}
```

to your `config/settings/local.py`. Here, `NAME` is the name of the database, `USER` the MySQL user, `PASSWORD` her password, `HOST` the database host, and `PORT` the port MySQL is listening on. If you don't use `/tmp/mysql.sock`, you can use `unix_socket` to specify its path. The user and the database can be created using:

```mysql
CREATE USER 'rdmo'@'localhost' identified by 'not a good password';
GRANT ALL ON `rdmo`.* to 'rdmo'@'localhost';
CREATE DATABASE `rdmo` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

on the MySQL-shell.
 Now you can [initialize your database](#initializing-the-database).


### SQLite

SQLite is the default option in RDMO, but we recommend it only for a development/testing setup on your local machine. It can be configured in `config/settings/local.py` by adding:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
    }
}
```

where `NAME` is the name of database file. Now you can [initialize your database](#initializing-the-database).

### Initializing the database

When you have configured your database, then you can initialize the database tables with a Django command [`migrate`](https://docs.djangoproject.com/en/4.2/ref/django-admin/#migrate).

To check if your settings are correct, please first run:
```bash
python manage.py check
```
this should return `System check identified no issues (0 silenced).` If there are any errors, please check your settings or dependencies. When the problem cannot be solved, please contact the RDMO community for support.

The command

```bash
python manage.py migrate
```
should now create RDMO database tables in the specified database.
