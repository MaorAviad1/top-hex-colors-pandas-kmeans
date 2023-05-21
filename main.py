import cv2
import pandas as pd
from PIL import Image
from sklearn.cluster import KMeans
import numpy as np


def get_top_3_colors(image_path, n_colors=3):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    image = image.reshape(-1, 3)

    kmeans = KMeans(n_clusters=n_colors)
    kmeans.fit(image)

    colors = kmeans.cluster_centers_

    # Convert colors to hex and return
    return [f'#{int(color[0]):02x}{int(color[1]):02x}{int(color[2]):02x}' for color in colors]


# Read CSV file
df = pd.read_csv('image_data.csv')

# Create a new column with the top 3 colors of each image
df['top_3_colors'] = df['image_path'].apply(get_top_3_colors)

# Write back to CSV
df.to_csv('image_data_with_colors.csv', index=False)
