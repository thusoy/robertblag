from flask import Flask, render_template, Markup
import markdown

from os import path

app = Flask(__name__)

config_path = path.join(path.dirname(__file__), 'config.py')
app.config.from_pyfile(config_path)

@app.route('/')
def frontpage():
    article_path = path.join(path.dirname(__file__), '../articles/His name is Robert Paulson.md')
    with open(article_path) as article_fp:
        article_md = article_fp.read()
    article = Markup(markdown.markdown(article_md))
    context = {
        'article': article,
        'title': 'His name is Robertsss Paulson',
    }
    return render_template('base.html', **context)


@app.context_processor
def context():
    return {
        'debug': True,
    }
