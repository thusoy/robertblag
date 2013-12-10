"""
    Entry point and the only view we have.
"""

from .article_utils import get_articles

from flask import Flask, render_template, abort
from os import path

app = Flask(__name__)

config_path = path.abspath(path.join(path.dirname(__file__), 'config.py'))
app.config.from_pyfile(config_path)


@app.route('/')
def frontpage():
    articles = get_articles()
    context = {
        'articles': articles,
    }
    return render_template('home.html', **context)


@app.route('/about.html')
def about():
    return render_template('about.html', title="Robert :: About")


@app.route('/<title>.html')
def show_blogpost(title):
    all_articles = get_articles()
    titles = {slugify(article['title']): article for article in all_articles}
    article = titles.get(title)
    if article:
        return render_template('article.html', title=article['title'], article=article)
    else:
        abort(404)


def slugify(string):
    return '-'.join(string.lower().split())

@app.context_processor
def default_context():
    return {
        'slugify': slugify,
        'debug': app.config.get('DEBUG', False),
    }
