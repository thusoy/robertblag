"""
    Some tools for fetching articles and their metadata from the repo.
"""

from flask import Markup
from os import path, listdir
from datetime import datetime
import markdown
import re
import subprocess

REPO_ROOT = path.join(path.dirname(__file__), '..')
ARTICLE_FILE_PATTERN = re.compile(r'.*\.md$')

def get_articles():
    """ Fetch a list of article dicts with the following properties:

        - content
        - author
        - date_added

    Articles are sorted by the time added to the repo.
    """
    articles = []
    article_dir = path.join(path.dirname(__file__), '..', 'articles')
    for article_file in listdir(article_dir):
        if not ARTICLE_FILE_PATTERN.match(article_file):
            continue
        article_path = path.relpath(path.join(article_dir, article_file))
        article = {}
        article['title'] = article_file.rstrip('.md')
        article['date_added'] = _get_datetime_added(article_path)
        article['author'] = _get_author(article_path)
        with open(article_path) as article_fp:
            article_md = article_fp.read()
        article['content'] = Markup(markdown.markdown(article_md))
        articles.append(article)
    return sorted(articles, key=lambda a: a['date_added'], reverse=True)


def _get_first_commit(article_path):
    cmd = 'git rev-list HEAD "%s"' % article_path
    raw_output = subprocess.check_output(cmd, shell=True, cwd=REPO_ROOT)
    all_commits = raw_output.strip().split('\n')
    first_commit = all_commits[-1]
    return first_commit


def _get_datetime_added(article_path):
    first_commit = _get_first_commit(article_path)
    cmd = 'git show -s --pretty="format:%%ct" %s --' % first_commit
    timestamp_added = subprocess.check_output(cmd, shell=True, cwd=REPO_ROOT)
    datetime_added = datetime.fromtimestamp(float(timestamp_added))
    return datetime_added


def _get_author(article_path):
    first_commit = _get_first_commit(article_path)
    cmd = 'git show -s --pretty="format:%%aN" "%s" --' % first_commit
    raw_output = subprocess.check_output(cmd, shell=True, cwd=REPO_ROOT)
    just_author = raw_output.strip()
    author_encoded = unicode(just_author, encoding='utf-8')
    return author_encoded
