# Decameal

A food management system that would enable Decadevs and Decagon employees to subscribe and unsubscribe from Decagon Meal.

![Decameal CI](https://github.com/decadevs/decameal/actions/workflows/ci.yml/badge.svg)
[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

## Technologies

- [Python 3.9](https://python.org) : Base programming language for development
- [Bash Scripting](https://www.codecademy.com/learn/learn-the-command-line/modules/bash-scripting) : Create convenient script for easy development experience
- [PostgreSQL](https://www.postgresql.org/) : Application relational databases for development, staging and production environments
- [Django Framework](https://www.djangoproject.com/) : Development framework used for the application
- [Django Rest Framework](https://www.django-rest-framework.org/) : Provides API development tools for easy API development
- [Github Actions](https://docs.github.com/en/free-pro-team@latest/actions) : Continuous Integration and Deployment
- [Docker Engine and Docker Compose](https://www.docker.com/) : Containerization of the application and services orchestration

## Getting up and Running with Docker

Getting started with this project is very simple, all you need is to have Git and Docker Engine installed on your machine. Then open up your terminal and run this command `git clone https://github.com/decadevs/decameal.git` to clone the project repository.

Change directory into the project folder `cd decameal`.

Spin up container needed for the project that are specified in **_local.yml_** file by running the command `docker-compose -f local.yml up`.

In summary, these are the lists of commands to run in listed order, to start up the project.

```docker
1. git clone https://github.com/decadevs/decameal.git
2. cd decameal
3. docker-compose -f local.yml build
4. docker-compose -f local.yml up

```

## Setting up git pre-commit

Before doing any git commit, pre-commit should be installed globally on your local machine, and then

    $ git init
    $ pre-commit install

**NB: Failing to do so will result with a bunch of CI and Linter errors that can be avoided with pre-commit.**

## Setting Up Your Users

- To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

- To create an **superuser account**, use this command:

      $ docker-compose -f local.yml run django python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

### Type checks

Running type checks with mypy:

    $ docker-compose -f local.yml run django mypy decameal

### Test coverage

To run the tests, check your test coverage, and generate an HTML coverage report:

    $ docker-compose -f local.yml run --rm django coverage run -m pytest
    $ docker-compose -f local.yml run --rm django coverage report

### Running tests with pytest

    $ docker-compose -f local.yml run --rm django pytest

## License

The MIT License - Copyright (c) 2022 - Present, Decagon Institute. https://decagonhq.com/

## Contributors

<table>
    <tr>
        <td align="center">
            <div>
                <img src="https://avatars.githubusercontent.com/u/80605206?v=4" width="100px;">
                <br /><sub><b>Ayodele Oluwatosin - Lead</b></sub>
            </div>
        </td>
        <td align="center">
            <div>
                <img src="https://avatars1.githubusercontent.com/u/49355114?s=460&u=17218f01b571cbad08912982baab6c31cc8cf004&v=4" width="100px;">
                <br /><sub><b>Olatunde Sodiq - Lead</b></sub>
            </div>
        </td>
      </tr>
</table>
