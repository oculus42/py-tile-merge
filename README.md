# py-tile-merge
## Python 3 Tile Download and Merge Script
Basic Tiled Image Download and Stitching

Some high-quality image viewers use a tile system like Open Street Maps or Google Maps, where image content is downloaded in a number of small pieces. Sometimes those images are public domain but have no option to download the original, high-quality source. That's why this script exists.

## Requirements
* Python 3
* Pillow

## How to use
* Download the ccript
* Install Python 3.x 
* Install Pillow
* Edit the variables in the script
  * Tile positions (x, y, z)
  * Base URL
  * Request delay
  * Input file format (only tested with JPG)
* Run the script

## Features
* Avoids downloading the same image twice.
* Optional delay to avoid flooding the tile service.
* Merges the images together when complete.
