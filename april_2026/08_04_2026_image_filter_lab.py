# 08/04/2026
# Image Filter Lab

import cv2
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
image_path = os.path.join(BASE_DIR, 'temp_plot.png')

# Load the image
image = cv2.imread(image_path)

if image is not None:
    print("Processing image...")
    # Convert BGR to RGB for matplotlib
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # 1. Grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # 2. Blur
    blurred_image = cv2.GaussianBlur(image_rgb, (15, 15), 0)
    
    # 3. Edge Detection
    edges = cv2.Canny(gray_image, 100, 200)
    
    # Show before and after
    plt.figure(figsize=(12, 8))
    
    plt.subplot(2, 2, 1)
    plt.imshow(image_rgb)
    plt.title('Original Image')
    plt.axis('off')
    
    plt.subplot(2, 2, 2)
    plt.imshow(gray_image, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')
    
    plt.subplot(2, 2, 3)
    plt.imshow(blurred_image)
    plt.title('Blurred Image')
    plt.axis('off')
    
    plt.subplot(2, 2, 4)
    plt.imshow(edges, cmap='gray')
    plt.title('Edge Detection (Canny)')
    plt.axis('off')
    
    plt.tight_layout()
    
    # Save the result
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'filter_results.png')
    plt.savefig(output_path)
    print(f"Image processing complete. Results saved to:\n{output_path}")
    
    # Uncomment the following line to display the plot interactively if running locally
    # plt.show() 
else:
    print(f"Failed to load image at '{image_path}'.")
