# 06/04/2026
# Image as Numbers

import cv2
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
image_path = os.path.join(BASE_DIR, 'temp_plot.png')

# Load the image
image = cv2.imread(image_path)

if image is not None:
    print("Image loaded successfully.")
    
    # Shape
    height, width, channels = image.shape
    print(f"\nShape: {image.shape}")
    print(f"Height: {height} pixels")
    print(f"Width: {width} pixels")
    print(f"Channels: {channels}")
    
    # Pixel values
    print("\nSample Pixel Values (Top-Left 3x3 region across all channels):")
    print(image[0:3, 0:3])
    
    # Explanation
    print("\nExplanation:")
    print("An image is represented as a multi-dimensional array (matrix) of numbers.")
    print("The shape (H, W, C) tells us the resolution (Height x Width) and the number of color channels.")
    print("For a standard color image, there are 3 channels (e.g., Blue, Green, Red in OpenCV).")
    print("Each pixel value is a number between 0 and 255 representing color intensity.")
else:
    print(f"Failed to load image at '{image_path}'. Ensure it exists.")
