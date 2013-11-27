"""
    Entry point and the only view we have.
"""

from .article_utils import get_articles

from flask import Flask, render_template
from os import path

app = Flask(__name__)

config_path = path.abspath(path.join(path.dirname(__file__), 'config.py'))
app.config.from_pyfile(config_path)


@app.route('/')
def frontpage():
    articles = get_articles()
    context = {
        'articles': articles,
        'debug': app.config.get('DEBUG', False),
    }
    return render_template('base.html', **context)
