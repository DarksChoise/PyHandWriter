import os
from PIL import Image, ImageDraw
from config.config import background_color, image_width, image_height, line_color, margin_color, margin_left, margin_right, margin_top, output_folder


def create_new_image(page_num, total_line_height):
    img = Image.new('RGB', (image_width, image_height), background_color)
    draw = ImageDraw.Draw(img)

    for y in range(margin_top, image_height, total_line_height):
        draw.line([(margin_left, y), (image_width - margin_right, y)], fill=line_color, width=2)

    margin_x = margin_left // 2
    draw.line([(margin_x, margin_top), (margin_x, image_height)], fill=margin_color, width=4)

    return img, draw


def save_image(image, page_number):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Save the image in the folder
    image.save(os.path.join(output_folder, f"text_#{page_number}.jpg"))
