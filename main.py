import os
from PIL import ImageFont
from utils.image_utils import create_new_image, save_image
from utils.text_utils import split_line, get_line_height
from config.config import dpi_factor, image_width, image_height, font_path, text_file, margin_top, margin_left, margin_right

# Check if the font exists
if os.path.exists(font_path):
    font = ImageFont.truetype(font_path, 10 * dpi_factor)
else:
    print("Font not found")
    exit()

# Read the text
with open(text_file, "r") as file:
    text = file.read()

# Split the text into lines
lines = text.splitlines()

# Calculate line height and spacing
line_height = get_line_height(font)
line_spacing = 10 * dpi_factor
total_line_height = line_height + line_spacing  # Calculate total line height here

# Initialize position and page number
y_position = margin_top
page_number = 1

# Create the first image
background, draw = create_new_image(page_number, total_line_height)

# Maximum width for the text
max_text_width = image_width - margin_left - margin_right

# Process the text and draw it onto the image
for line in lines:
    if line == "":
        y_position += total_line_height
        continue

    wrapped_lines = split_line(line, draw, font, max_text_width)

    for wrapped_line in wrapped_lines:
        if y_position + total_line_height > image_height:
            save_image(background, page_number)
            page_number += 1
            y_position = margin_top
            background, draw = create_new_image(page_number, total_line_height)

        draw.text((margin_left + 10, y_position), wrapped_line, font=font, fill=(0, 0, 0))
        y_position += total_line_height

# Save the last image
save_image(background, page_number)
