# Image Color Extractor Script

This Python script extracts the top 3 dominant colors from images and adds them to a CSV file.

## Dependencies

To run this script, you need the following Python libraries:

-   pandas
-   Pillow
-   scikit-image
-   opencv-python
-   sklearn

You can install these libraries with pip:

bashCopy code

`pip install pandas Pillow scikit-image opencv-python sklearn` 

## Usage

The script expects a CSV file with a column named 'image_path' containing the path to each image. The script will create a new CSV file with an additional column 'top_3_colors' which lists the top 3 dominant colors (in hex format) for each image.

You can run the script as follows:

bashCopy code

`python script.py` 

Please replace `script.py` with the name of your Python script file.

----------

