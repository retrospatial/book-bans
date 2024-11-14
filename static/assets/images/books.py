import os
import requests
import pandas as pd

# Path to your CSV file
csv_file_path = "books.csv"

# Create a folder to save images (optional)
folder = "covers"
os.makedirs(folder, exist_ok=True)

# Read the CSV file using pandas
df = pd.read_csv(csv_file_path)

# Ensure the CSV has 'title' and 'url' columns
if 'url' not in df.columns:
    print("The CSV file must have a column named 'url'.")
    exit()

# Function to download images
def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Image successfully downloaded: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}. Error: {e}")

# Loop through each URL in the DataFrame and download the images
for i, row in df.iterrows():
    url = row['url']  # Get the image URL from the 'url' column
    # Name the image as 'book_1.jpg', 'book_2.jpg', etc.
    image_name = f"book_{i+1}.jpg"  
    save_path = os.path.join(folder, image_name)
    download_image(url, save_path)
