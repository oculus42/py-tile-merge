# py-tile-merge
## Python 3 Tile Download and Merge Script
Basic Tiled Image Download and Stitching

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
