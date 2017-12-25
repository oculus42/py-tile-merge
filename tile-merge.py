## README
# Tile Download and Stitcher
# Python 3 Download Script
# https://github.com/oculus42/py-tile-merge
#
# Image Merge uses the Pillow Library
# On windows, install Pillow with the following command
#
# py -m pip install Pillow

################################################
# Change these variables
start_x = 0
end_x = 10
start_y = 0
end_y = 10
z_level = 13

# Optional delay between successive requests (in seconds)
request_delay = 0.5

# Swaps out the x, y, and z values with %s, which allows the script to fill them in
# This script doesn't support reordering those parameters at this time.
base_url = "http://www.example.com/tileService?x=%s&y=%s&z=%s"

source_type = "jpg"

################################################
# Everything below this should stay the same

import os
import os.path
import urllib
import urllib.request
import time

# Make an output folder
if not os.path.exists("out"):
    os.makedirs("out")

# Python range is exclusive of the end, so we add one
for x in range(start_x, end_x + 1):
    for y in range(start_y, end_y + 1):

        dl_url = base_url % (x, y, z_level)
        file_name = "out/%s-%s-%s.%s" % (x, y, z_level, source_type)

        #Don't re-download images we have
        if not os.path.isfile(file_name):

            print(file_name)
        
            urllib.request.urlretrieve(dl_url,file_name)
        
            # Don't overload the server with requests
            time.sleep(request_delay)

# Image Merge section
import sys
from PIL import Image

start_image_path = "out/%s-%s-%s.%s" % (start_x, start_y, z_level, source_type)

# Figure out the final image size
# Assumes all tiles are the same size
start_tile = Image.open(start_image_path)
tile_width = start_tile.size[0]
tile_height = start_tile.size[1]
start_tile.close()

total_width =  tile_width * (end_x - start_x + 1)
total_height = tile_height * (end_y - start_y + 1)

print("Final image is %s x %s" % (total_width, total_height))

final_image = Image.new('RGB', (total_width, total_height))

# Same range logic as above
# This time we cycle over the saved images
# Pasting them into the final as we go
for x in range(start_x, end_x + 1):
    for y in range(start_y, end_y + 1):

        file_name = "out/%s-%s-%s.%s" % (x, y, z_level, source_type)
        tile = Image.open(file_name)
        
        x_offset = (x) * tile_width
        y_offset = (y) * tile_height
        
        final_image.paste(tile, (x_offset, y_offset))
        tile.close()

# Full quality on the output image
final_image.save("complete.jpg", quality=100)
