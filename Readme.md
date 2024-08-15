# Batch PDF-to-Image Conversion Script

This Python script processes multiple PDF files in a specified directory, extracts the first page of each PDF, and converts it to an image (PNG format). The resulting images are saved in a designated output directory.

## Features

- **Batch Processing:** Automatically processes all PDF files in a given folder.
- **First Page Extraction:** Extracts and converts only the first page of each PDF to an image.
- **Customizable Paths:** Easily specify input and output directories.

## Prerequisites

### Python Packages

Ensure you have the following Python packages installed:

- `pdf2image`
- `Pillow`

You can install them using pip:

```bash
pip install pdf2image pillow
```

### Poppler

The `pdf2image` library requires `poppler` to be installed on your system.

- **Ubuntu/Debian:**
  ```bash
  sudo apt-get install poppler-utils
  ```
- **MacOS (using Homebrew):**
  ```bash
  brew install poppler
  ```

## Usage

1. **Clone or Download the Script:**

   Save the script as `batch_pdf_to_image.py`.

2. **Edit the Script:**

   Open the script in a text editor and update the following paths:

   - `pdf_dir`: Path to the folder containing your PDF files.
   - `output_dir`: Path to the folder where you want to save the images.

   Example:
   ```python
   pdf_dir = "/path/to/your/pdf/folder"
   output_dir = "/path/to/output/directory"
   ```

3. **Run the Script:**

   Execute the script using Python:

   ```bash
   python extract.py
   ```

   The script will process each PDF in the specified directory, extract the first page, and save it as an image in the output directory.

## Output

- The images will be saved with the same name as the PDF files, with the addition of `_page1.png` at the end. For example, if the PDF is named `example.pdf`, the image will be saved as `example_page1.png`.
- The script will print the path to each saved image once it has been processed.

## Troubleshooting

- **Missing PDF Files:** Ensure that the `pdf_dir` path is correctly set and contains valid PDF files.
- **Poppler Not Found:** If you encounter issues related to `poppler`, ensure it is installed and accessible in your system's PATH.

## License

This script is provided under the MIT License. Feel free to use, modify, and distribute it as needed.

---

**Author:** Joseph Gakah  
**Date:** 15 August 2024
