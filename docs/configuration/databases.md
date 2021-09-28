# Databases

RDMO can be used with all kind of databases supported by the Django framework. The particular database connection is defined using the setting `DATABASE`. An overview about the Django database settings is given [here](https://docs.djangoproject.com/en/1.10/ref/settings/#databases). In the following, we show the settings for PostgreSQL, MySQL, and SQLite.

## PostgreSQL

PostgreSQL can be installed using:

```bash
# Debian/Ubuntu
sudo apt install postgresql

# CentOS
sudo yum install postgresql-server postgresql-contrib
sudo postgresql-setup initdb
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

To use PostgreSQL as your database backend install `psycopg2` in your virtual environment:

```bash
pip install -r requirements/postgres.txt
```

Then, add the following to your `config/settings/local.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'rdmo',
        'USER': 'rdmo',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
```

where `Name` is the name of the database, `USER` the PostgreSQL user, `PASSWORD` her password, `HOST` the database host, and `PORT` the port PostgreSQL is listening on. Note that, depending on your setup, not all settings are needed. If you are using the peer authentication methods, you only need the `NAME` and `ENGINE` settings. The user and the database can be created using:

```bash
sudo su - postgres
createuser rdmo
createdb rdmo -O rdmo
```

This assumes peer authentication for the rdmo user.

The command

```bash
python manage.py migrate
```

should now create the RDMO database tables on PostgreSQL.


## MySQL


MySQL (or community-developed fork MariaDB) can be installed using:

```bash
# Debian/Ubuntu
sudo apt install mysql-client mysql-server libmysqlclient-dev        # for MySQL
sudo apt install mariadb-client mariadb-server libmariadbclient-dev  # for MariaDB

# CentOS
sudo yum install -y mysql mysql-server mysql-devel                   # for MySQL
sudo yum install -y mariadb mariadb-server mariadb-devel             # for MariaDB
sudo systemctl enable mariadb
sudo systemctl start mariadb
sudo mysql_secure_installation
```

To use MySQL as your database backend install `mysqlclient` in your virtual environment:

```bash
pip install -r requirements/mysql.txt
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

to your `config/settings/local.py`. Here, `Name` is the name of the database, `USER` the MySQL user, `PASSWORD` her password, `HOST` the database host, and `PORT` the port MySQL is listening on. If you don't use `/tmp/mysql.sock`, you can use `unix_socket` to specify its path. The user and the database can be created using:

```mysql
CREATE USER 'rdmo'@'localhost' identified by 'not a good password';
GRANT ALL ON `rdmo`.* to 'rdmo'@'localhost';
CREATE DATABASE `rdmo` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

on the MySQL-shell.

The command

```bash
python manage.py migrate
```

should now create the RDMO database tables on MySQL.


## SQLite


SQLite ist the default option in RDMO and configured in `config/settings/base.py`. We recommend it only for a development/testing setup. It can be configured in `config/settings/local.py` by adding:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '',
    }
}
```

where `Name` is the name of database file.

The command

```bash
python manage.py migrate
```

should now create RDMO database tables in the specified database file.
