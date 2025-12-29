from PIL import Image
import os

# Base directory of the script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Input and output folders
input_dir = os.path.join(BASE_DIR, "input")
output_dir = os.path.join(BASE_DIR, "output")

# Create output folder if needed
os.makedirs(output_dir, exist_ok=True)

TARGET_SIZE = 1440
WHITE = (255, 255, 255)

files = os.listdir(input_dir)

for file_name in files:
    # Process only image files
    if file_name.lower().endswith((".jpg", ".jpeg", ".png")):
        print("Photo:", file_name)

        input_path = os.path.join(input_dir, file_name)

        # Output filename
        name, ext = os.path.splitext(file_name)
        new_name = f"{name}_square{ext}"
        output_path = os.path.join(output_dir, new_name)

        img = Image.open(input_path)
        width, height = img.size

        # Scale image proportionally
        scale = TARGET_SIZE / max(width, height)
        new_width = round(width * scale)
        new_height = round(height * scale)

        img_resized = img.resize((new_width, new_height), Image.LANCZOS)

        # Create square canvas and center image
        canvas = Image.new("RGB", (TARGET_SIZE, TARGET_SIZE), WHITE)
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

    else:
        print("Skip:", file_name)
