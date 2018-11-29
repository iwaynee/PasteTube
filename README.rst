Hello World for Bottle
======================

In this tutorial, we'll create a web app and deploy it to Heroku, using
`Bottle <http://bottlepy.org/docs/dev/>`_.


tl;dr
-----

Want to jump right in? You can quickly get a copy of this app in your
Heroku account at `python.heroku.com <http://python.heroku.com>`_.


Ready?
------

Before we start, you need a Heroku `account <https://api.heroku.com/signup>`_ and `toolbelt <http://toolbelt.herokuapp.com/>`_.


Act I: Build.
-------------

1. Make sure you're using a virtualenv::

    $ virtualenv --no-site-packages venv
    $ source venv/bin/activate

2. Install your dependencies::

    $ pip install bottle

3. Say Hello to the World in ``app.py``::

    import os
    from bottle import route, run

    @route('/hello/:name')
    def index(name='World'):
        return '<b>Hello %s!</b>' % name

Simple enough.

Now, we need to serve our app locally. On Heroku, your application's port is available
as an `environment variable <http://en.wikipedia.org/wiki/Environment_variable>`_.

So, we can grab the port we need to run it on Heroku, and default when that's not defined (locally)::

    # Get required port, default to 5000.
    port = os.environ.get('PORT', 5000)

And, we can bind to the port::

    # Run the app.
    run(host='0.0.0.0', port=port)


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

