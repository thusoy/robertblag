from robert import app
from flask.ext.frozen import Freezer

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
