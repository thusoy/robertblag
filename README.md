Robert
======

The blog for Robert, our volleyball playing mindstorms robot.

To write a new blogpost, add a markdown file to the 'articles' directory. Upload any images
to go with the post into 'robert/static/img' or similar. Examples will come.

How does it work?
-----------------

A simple webserver is running, that scans the 'articles' folder for files to render as markdown,
and renders them all using the 'robert/templates/base.html' template. Look at the code to see how
it's done, it's real simple. When you add a new article, Travis will pull down the repo and run the
grunt build task, which is only a thin wrapper around Frozen-Flask. Frozen-Flask simulates a request
to the webserver, and stores the result as a static website into the 'dist' folder. Travis will
then push the resulting 'dist' folder into the production branch, which is what my server
will pull down and serve, at [bob.thusoy.com](http://bob.thusoy.com).

For now, the server doesn't pull automatically on changes, but I can add that if desireable.

Running locally
---------------

Assuming you have virtualenv and node/npm installed already, this is what you need to do to run the code locally.

Set up a new virtualenv:

    $ virtualenv venv
    $ # unix:
    $ . venv/bin/activate
    # windows:
    $ venv\Scripts\activate.bat

Install the python packages:

    $ pip install -r requirements.txt

Install grunt and the grunt packages:

    $ npm install -g grunt-cli
    $ npm install

Run the server:

    $ grunt

This will start a webserver at `localhost:5000`, open up your web browser to see it. The browser listens to changes in
any of the project files, and will automatically refresh itself on any changes. This is most useful if you're working
on styles or similar, but if you want to see how your article will look before you publish this might also come in 
handy.

Note that to transpile the SASS to CSS, you also need to have compass installed, since there's no good js libraries for
compass/sass. If you have rubygems installed (which it usually is on most *nix systems), this is fairly easy:

    $ gem update --system
    $ gem install compass

All set, have fun!
