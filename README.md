![printf](https://i.imgur.com/lpnL8nd.png)

## SCHEMATIC
![SCHEMA](https://i.imgur.com/4Y1HRWC.png)

Stages of the challenge are covered in detail at:
[Geru_Challenge](https://gist.github.com/flaviogeru/53a739e35e1523a39bf3e7a95d177918)

![Alt Text](https://media.giphy.com/media/cIsRhzdUL6DYUBWho3/giphy.gif)

## SYNOPSIS
I enjoyed this challenge and learned a lot by using a framework and technologies I haven't used before. I started off pouring through the documentation on the Pylongs Project Pyramid website. To get familiar with the Pyramid framework, I first read the [Quick Tour of Pyramid](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tour.html) and then worked through the [Quick Tutorial for Pydamid](https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html).

This is the first time where I used a virtual environment. I saw the value of using an isolated Python environment that allows packages to be installed for use by a partifular application versus system wide. Interestingly, I found that setting the virtual environment in one window within `iterm` did not apply to the same directory in another window.

I decided to check out the `cookiecutter` templates - and went with the `starter` template to kick off my project and build upon it as I went along. More information can be found [here](https://github.com/Pylons/pyramid-cookiecutter-starter)

There were a number of challenges to overcome during this project - such as how to generate a session id or deal with deserializing the datetime format to be inserted into the database. 
These challenges were overcome with more reading, tutorials and simple trial and error.

Some of the things I learned from this project:
- How to effectively query the [provided API](https://1c22eh3aj8.execute-api.us-east-1.amazonaws.com/challenge/quotes)
- Create a web application utilizing the [Pyramid Web Framework](https://docs.pylonsproject.org/projects/pyramid/en/latest/index.html#)
- Editing the application driver file `.ini`
- Better working knowledge of using modules & packages
- Using the cookiecutter template
- Using `jinja2`/`chameleon` templating languages alongside CSS
- Working with virtual environments
- Dealing with complexity (dependent installations and increasing number of functions/files)
- How to deserialize the datetime format
- How to save and query data into the database using `SQLAlchemy`
- Organizing views via the `views.py` and `jinja2` templates
- How to create and serve JSON data via an API endpoint

## ENVIRONMENT

This project was written in `ZSH` on `Ubuntu 14.04 LTS` using `python3` (`version 3.4.3`).

Tools used:
* [] - `pyramid 1.9.1` (framework)
* [] - `jinja2` (markdown template)
* [] - `sqlAlchemy` (database)
* [] - `SQLite` (database)
* [] - `pip` for package management
* [] - `pyramid-cookiecutter` (project template) 

Testing executed in VirtualBox on [Ubuntu](https://atlas.hashicorp.com/ubuntu/boxes/trusty64) via [Vagrant](https://www.vagrantup.com/)(1.9.1)


## USAGE OF PYRAMID WEB APP
- First, clone the repoository into your directory.
```
$ git clone https://github.com/spencerhcheng/Geru_Challenge
```

- I used `Python 3.4` to build out this app; however, `Pyramid` supports `Python 3.4+` and `Python 2.7+`. Please make sure you have a compatible version of `python` installed.

- Set an environmental variable to save typing:
```
export VENV=~/env/myproject/env
```

- Change directory to `myproject`

- Create a new virtual environment:
```
python3 -m venv $VENV
```

- Update the the latest version of packaging tools:
```
$VENV/bin/pip install --upgrade pip setuptools
```

- Install Pyramid:
```
$VENV/bin/pip install "pyramid==1.9.1" waitress
```
Waitress is Pyramid's WSGI server. We now have Pyramid and the `waitress` package.

- Install sqlalchemy, jinja2, zope.sqlalchemy, chameleon, and pytest
```
$VENV/bin/pip install webtest pytest pytest-cov deform sqlalchemy \
  pyramid_chameleon pyramid_debugtoolbar pyramid_jinja2 waitress \
  pyramid_tm zope.sqlalchemy
```

- Install our project:
```
$VENV/bin/pip install -e .
```
 (Note: anytime setup.py is changed, we need to re-install the app)

Produce database and table(s):
```
$VENV/bin/initialize_myproject_db development.ini
```

- Run the WSGI application:
```
$VENV/bin/pserve development.ini --reload
```

- Proceed to a web browser using a computer connected to the local network (specified by route 0.0.0.0:8080) and point browser to localhost:8080.

## ROUTES:
- / (`localhost:8080`):

Displays `Web Challenge 1.0`

![Alt Text](https://media.giphy.com/media/8OYSzlFu6E9wJw4UWX/giphy.gif)

- /quotes (`localhost:8080/quotes`):

Displays page containing all quotes returned by API

![Alt Text](https://media.giphy.com/media/14SAwXrAXgNwZDthAg/giphy.gif)

- `/quotes/<quote_number>` (`localhost:8080/<quote_number>`):

![Alt Text](https://media.giphy.com/media/XHUxy4pO0nKI0iXlN9/giphy.gif)

Displays page containing <quote_number> followed by the quote
- `/quotes/random` (`localhost:8080/quotes/random`):

Presents a page containing a random quote with the quote number.

![Alt Text](https://media.giphy.com/media/2tOsgFEQCAONDpMmpg/giphy.gif)

- `/api_query` (`localhost:8080/api_query`):

Presents a page containing stored information in the `sqlalchemy` database, including the session_identifier (unique UUID for each session user), date + time, and page requested.

![Alt Text](https://media.giphy.com/media/y7YOI5UWSwz3m4PHJL/giphy.gif)

## TO DO

- [ ] | - Write unit tests
- [ ] | - Further streamline CSS + jinja templates
- [ ] | - Fix CSS bug with resizing of web page
- [ ] | - Create custom 404 page
- [ ] | - Incorporate navigation bar
- [ ] | - Deploy app on web server


## AUTHOR
Spencer Cheng - https://github.com/spencerhcheng || [Twitter](https://twitter.com/spencerhcheng)

