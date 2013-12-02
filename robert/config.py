from os import path

FREEZER_DESTINATION = path.abspath(path.join(path.dirname(__file__), '../dist'))

# The size the raw images will be resized to
IMAGE_WIDTH = 1000

# The JPEG quality used to save the new images
IMAGE_QUALITY = 70
