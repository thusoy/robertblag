from __future__ import division

from robert import app

from flask.ext.frozen import Freezer
from PIL import Image

from os import listdir, path

freezer = Freezer(app)


def resize_images():
    src_dir = 'robert/static/raw_img'
    for raw_image_file in listdir(src_dir):
        image = Image.open(path.join(src_dir, raw_image_file))
        new_size = calculate_new_size(image.size)
        image = image.resize(new_size, Image.ANTIALIAS)
        dest_file =path.join('dist', 'static', 'img', raw_image_file)
        image.save(dest_file, quality=app.config['IMAGE_QUALITY'])
        print "{} resized to {!r}, new size: {}kB".format(
            raw_image_file, new_size, int(path.getsize(dest_file)/1024))


def calculate_new_size(old_size):
    old_width, old_heigth = old_size
    ratio = min(app.config['IMAGE_WIDTH'] / old_width, 1)
    new_size = (int(old_width*ratio), int(old_heigth*ratio))
    return new_size


if __name__ == '__main__':
    freezer.freeze()
    resize_images()
