import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

def add_watermark(img, watermark_path, save_folder):
    # Open the image
    im = Image.open(img)
    # Open the watermark image
    watermark = Image.open(watermark_path)
    # Resize the watermark image
    watermark = watermark.resize((773,322))
    # Get the width and height of the image
    width, height = im.size
    # Check if the image is vertical or horizontal
    if width > height:
        # Paste the watermark image on the bottom right corner of the horizontal image
        im.paste(watermark, (width-watermark.width, height-watermark.height), watermark)
    else:
        # Paste the watermark image on the bottom right corner of the vertical image
        im.paste(watermark, (width-watermark.width, height-watermark.height-30), watermark)
    # Save the watermarked image in the specified folder
    im.save(save_folder + '/' + 'watermarked_' + img.split('/')[-1])

# Create a Tkinter root
root = tk.Tk()
root.withdraw()

# Ask the user to select the source folder
source_folder = filedialog.askdirectory(title = "Select the source folder")

# Ask the user to select the watermark image
watermark_path = filedialog.askopenfilename(title = "Select watermark image", filetypes = (("png files", "*.png"), ("all files", "*.*")))

# Ask the user to select the destination folder
destination_folder = filedialog.askdirectory(title = "Select the destination folder")

# Iterate over the files in the source folder and add the watermark
for file in os.listdir(source_folder):
    # Check if the file is an image
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        # Create the full path of the image
        img = source_folder + '/' + file
        add_watermark(img, watermark_path, destination_folder)

# Show a message to indicate that the process is complete
print("Watermark added to the images in the source folder and saved in the destination folder")
