PasteTube
======================

This Appliaction makes it easy to sync your Copy&Paste Data from
diffrent Devices.

Go to the `App <http://paste-tube.herokuapp.com/>`_.


Act II: Try.
------------

Let's run the app locally::

    $ python app.py
    Bottle server starting up (using WSGIRefServer())...
    Listening on http://0.0.0.0:5000/
    Hit Ctrl-C to quit.

Now you can hit the app and play around with it::

    $ curl http://0.0.0.0:5000/hello/kitty
    <b>Hello kitty!</b>


Act III: Deploy.
----------------

In the project directory, create a new file named ``Procfile``.
This `specifies the processes that comprise your app <http://devcenter.heroku.com/articles/procfile>`_.

Our ``Procfile`` will look like this::

    web: python app.py

You can now test this out locally with the `foreman <http://ddollar.github.com/foreman/>`_ command (included in the toolbelt)::

    $ foreman start
    18:04:25 web.1     | started with pid 21350
    18:04:25 web.1     | Bottle server starting up (using WSGIRefServer())...
    18:04:25 web.1     | Listening on http://0.0.0.0:5000/
    18:04:25 web.1     | Hit Ctrl-C to quit.

It works! Let's push this app up to Heroku.

We also need to tell Heroku what our app needs to run.::

    $ pip freeze > requirements.txt

Your app needs to be in a `Git <http://git-scm.com/>`_ repo. If it isn't already,
you can do this easily::

    $ git init
    $ git add .
    $ git commit -m "Created app."

Now, we can create a new heroku app to push this to::

    $ heroku create --stack cedar
    Creating simple-warrior-3414... done, stack is cedar
    http://simple-warrior-3414.herokuapp.com/ | git@heroku.com:simple-warrior-3414.git
    Git remote heroku added

Let's push it up! ::

    $ git push heroku master
    ...
    $ curl http://simple-warrior-3414.herokuapp.com/hello/kitty
    <b>Hello kitty!</b>

\\o/

