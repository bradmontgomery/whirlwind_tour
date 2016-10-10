Django: A whirlwind tour
========================


This repo contains sample code for an introductory talk on Django. This
talk was last given at DevSpace, Oct 2016.


Usage
-----

Before you can use this code, you'll need to install Python and Django. (There's
a `requirements.txt` file in this repo that'll get the same version of django
with which the code was built).

Once you've got python + django, check out this repo, cd into the `foo` directory,
and run the following commands

- `python manage.py migrate` to create your database (an sqlite file)
- `python manage.py createsuperuser` to create a user account
- `python manage.py runserver` to run the development server.

Then open up [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/),
log in with the user credentials you just created and start playing around.

Enjoy!
