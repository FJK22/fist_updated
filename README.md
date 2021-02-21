# Fist_updates

## Project requirements
* [Python >= 3.0](https://docs.python.org/3)
* [Django >= 3.0](https://docs.djangoproject.com/en/3.0/)
* [Bootstrap documentation - more features](https://getbootstrap.com/docs/4.1/getting-started/introduction)

## Setup
* On project initialisation, clone the repository using

```sh
git clone https://github.com/JbFiras/Dating-Platform-Prod.git
```
> *Note:* This needs to be done only once

## Running the projecrt with Docker on local machine

```sh
Docker compose build
```
```sh
Docker compose up -d
```
## Create and activate virtual environment
```sh
python -m venv env
```

For windows, activate it this way

```sh
env/Scripts/activate
```

For other operating system like Linux and MacOS, use

```sh
source env/bin/activate

## Installing project dependencies

To install the project dependencies, use

```sh
pip install -r requirements.txt
```

## Migrating changes

Make sure you run the following code after creating either a new django app, model or migration. This will ensure that the database is in sync and prevent unnecessary issues.

```sh
python manage.py makemigrations
python manage.py migrate
```