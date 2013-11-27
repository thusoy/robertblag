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
