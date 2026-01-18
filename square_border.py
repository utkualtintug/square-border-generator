from PIL import Image
from tqdm import tqdm
import argparse
import os

# (Support for 200MP images)
Image.MAX_IMAGE_PIXELS = 200000000  # ~200 MP

# Base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Input and output folders
input_dir = os.path.join(BASE_DIR, "input")
output_dir = os.path.join(BASE_DIR, "output")

# Create output folder if needed
os.makedirs(output_dir, exist_ok=True)

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Square border generator")
parser.add_argument("--size", type=int, default=1440, help="Output image size (e.g. 1080, 1440)")
parser.add_argument("--color", type=str, default="white", help="Output border color (e.g. white, black or gray)")

args = parser.parse_args()

# Read CLI options
TARGET_SIZE = args.size
color = args.color.lower()

# Map color argument to RGB value
if color == "white":
    BORDER_COLOR = (255, 255, 255)
elif color == "black":
    BORDER_COLOR = (0, 0, 0)
elif color == "gray":
    BORDER_COLOR = (128, 128, 128)
else:
    raise ValueError("Unsupported color. Use 'white', 'black', or 'gray'.")

files = os.listdir(input_dir)

Image_files = [f for f in files if f.lower().endswith((".jpg", ".jpeg", ".png"))]

if not Image_files:
    print("There are no pictures in the input folder.")
else:
    for file_name in tqdm(Image_files, desc="Processing", unit="img"):
        
        input_path = os.path.join(input_dir, file_name)

        # Output filename
        name, ext = os.path.splitext(file_name)
        new_name = f"{name}_square{ext}"
        output_path = os.path.join(output_dir, new_name)
        try:
            img = Image.open(input_path)
            width, height = img.size

            # Scale image proportionally
            scale = TARGET_SIZE / max(width, height)
            new_width = round(width * scale)
            new_height = round(height * scale)

            img_resized = img.resize((new_width, new_height), Image.LANCZOS)

            # Create square canvas and center image
            canvas = Image.new("RGB", (TARGET_SIZE, TARGET_SIZE), BORDER_COLOR)
            x_offset = (TARGET_SIZE - new_width) // 2
            y_offset = (TARGET_SIZE - new_height) // 2
            canvas.paste(img_resized, (x_offset, y_offset))

            # Save optimized JPEG
            canvas.save(
                output_path,
                format="JPEG",
                quality=85,
                subsampling=2,
                optimize=True
            )
        except Exception as e:
            tqdm.write(f"Error ({file_name}): {e}")