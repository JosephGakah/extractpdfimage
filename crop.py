import os
from PIL import Image, ImageChops

# Define the directory containing the images and the output directory
image_dir = "/home/gakah/Neurollect/Audread/Books/images/ssd"
output_dir = "/home/gakah/Neurollect/Audread/Books/images/ssd/cropped"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to crop white margins from an image
def crop_white_margins(image):
    # Convert image to RGB if not already in that mode
    if image.mode != 'RGB':
        image = image.convert('RGB')

    # Find the bounding box of the non-white areas
    bg = Image.new(image.mode, image.size, (255, 255, 255))
    diff = ImageChops.difference(image, bg)
    bbox = diff.getbbox()

    if bbox:
        return image.crop(bbox)
    else:
        # In case there's no difference, return the original image
        return image

# Loop through all images in the directory
for img_file in os.listdir(image_dir):
    if img_file.endswith((".png", ".jpg", ".jpeg")):
        img_path = os.path.join(image_dir, img_file)

        # Open the image
        image = Image.open(img_path)

        # Crop the white margins
        cropped_image = crop_white_margins(image)

        # Save the cropped image
        output_image_path = os.path.join(output_dir, f"cropped_{img_file}")
        cropped_image.save(output_image_path)

        print(f"Cropped image saved: {output_image_path}")

print("All images have been processed.")
