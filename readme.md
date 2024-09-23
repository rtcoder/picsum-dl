# Picsum Image Downloader

This Python script allows you to download random images from [Picsum.photos](https://picsum.photos/) with specified dimensions.

## Requirements

- Python 3.x
- `requests` library (Install using: `pip install requests`)

## Usage

The script accepts the following command-line arguments:

- `--count` or `-c` (required): The number of images to download.
- `--width` or `-w` (required): The width of the images.
- `--height` or `-ht` (optional): The height of the images. If not provided, the images will be square.

### Example Commands

1. **Download 5 square images with width 300px**:
   ```bash
   python picsum-dl.py --count 5 --width 300

2. **Download 5 images with width 300px and height 200px:**
3. ```bash
   python picsum-dl.py --count 5 --width 300 --height 200
