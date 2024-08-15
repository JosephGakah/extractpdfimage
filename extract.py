import os
from pdf2image import convert_from_path
from PIL import Image

# Define the directory containing the PDF files and the output directory
pdf_dir = "/path/to/your/pdf/folder"
output_dir = "/path/to/output/directory"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through all PDF files in the directory
for pdf_file in os.listdir(pdf_dir):
    if pdf_file.endswith(".pdf"):
        pdf_path = os.path.join(pdf_dir, pdf_file)

        # Extract the first page of the PDF and convert it to an image
        images = convert_from_path(pdf_path, first_page=1, last_page=1)

        # Save the image with the same name as the PDF, but with a .png extension
        output_image_path = os.path.join(output_dir, f"{os.path.splitext(pdf_file)[0]}_page1.png")
        images[0].save(output_image_path, 'PNG')

        print(f"First page of {pdf_file} has been saved as an image: {output_image_path}")

print("All PDFs have been processed.")
