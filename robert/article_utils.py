"""
    Some tools for fetching articles and their metadata from the repo.
"""

from flask import Markup
from os import path, listdir
import markdown
import subprocess


def get_articles():
    """ Fetch a list of article dicts with the following properties:

        - content
        - author
        - date_added
    """
    articles = []
    article_dir = path.join(path.dirname(__file__), '..', 'articles')
    for article_file in listdir(article_dir):
        article_path = path.relpath(path.join(article_dir, article_file))
        article = {}
        article['title'] = article_file.rstrip('.md')
        article['date_added'] = _get_date_added(article_path)
        article['author'] = _get_author(article_path)
        with open(article_path) as article_fp:
            article_md = article_fp.read()
        article['content'] = Markup(markdown.markdown(article_md))
        articles.append(article)
    return articles


def _get_first_commit(article_path):
    cmd = 'git rev-list HEAD "%s"' % article_path
    raw_output = subprocess.check_output(cmd, shell=True)
    all_commits = raw_output.strip().split('\n')
    first_commit = all_commits[-1]
    return first_commit


def _get_date_added(article_path):
    first_commit = _get_first_commit(article_path)
    cmd = 'git show -s --format="%%ci" %s --' % first_commit
    date_added = subprocess.check_output(cmd, shell=True)
    nicely_formatted_date_added = ' '.join(date_added.split()[:2])
    return nicely_formatted_date_added


def _get_author(article_path):
    first_commit = _get_first_commit(article_path)
    cmd = 'git show -s --format="%%aN" "%s" --' % first_commit
    raw_output = subprocess.check_output(cmd, shell=True)
    just_author = raw_output.strip()
    author_encoded = unicode(just_author, encoding='utf-8')
    return author_encoded
