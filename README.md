# Instagram Square Border

A Python tool that converts all images in the `input` folder into square photos with a **white 1:1 border**, optimized for Instagram sharing.

## Motivation

When posting photos to Instagram, I like to add a white square border so my profile looks cleaner and more consistent.

Existing mobile apps can do this, but the process was inefficient:

- Manual adjustment for each photo
- Permission requests to access the photo library
- Forced ads before saving the image

Processing a single photo often took several minutes.

By running it once, all photos in a folder are converted to Instagram-ready square images **within seconds**, with no ads, no permissions, and no manual adjustments.

## Example

Below is an example of the result after applying a square white border:

![Square Border Example](screenshots/github_showcase.png)

## Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/)

## Setup

### 1) Create and activate a virtual environment

```bash
python -m venv venv
```

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### 2) Install dependencies

```bash
pip install pillow
```

## Usage

1. Create a folder named `input` in the project root.
2. Place your photos (`.jpg`, `.jpeg`, `.png`) inside the `input` folder.
3. Run the script.
4. Processed images will be saved to the `output` folder.

The script will automatically create the `output` folder if it does not exist.

## Run

```bash
python square_border.py
```
