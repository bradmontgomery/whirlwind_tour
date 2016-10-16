Django: A whirlwind tour
========================


This repo contains sample code for an introductory talk on Django. This
talk was last given at DevSpace, Oct 2016. You can get the slides from speakerdeck:

https://speakerdeck.com/bkmontgomery/django-a-whirlwind-tour-2016


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


Notes
-----

Please keep a couple of things in mind when reviewing this repo:

1. This contains an entire project, and you wouldn't typically distribute that
   to the world (check out [Django Packages](https://djangopackages.org/) to
   see how apps are often distributed).
2. `foo/settings.py` contains sensitive information. Namely, the `SECRET_KEY`
   is something you *never ever want someone else to see*!
3. There are no tests. This is NOT OK for something that real people would use.
4. This whole project is for illustrative purposes only, and I tried to make
   the simplest possible (but still valuable) app that I could.
5. Please feel free to fork this repo, change it, use it for your own. It's
   MIT-licensed, so you can do whatever you want. Just keep your own project
   private (see #2 above).

