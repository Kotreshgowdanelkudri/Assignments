from PIL import Image, ImageDraw

# Create a new image with white background
img = Image.new('RGB', (400, 300), color = 'white')
draw = ImageDraw.Draw(img)

# Draw a simple line chart
draw.line((50, 250, 100, 200, 150, 150, 200, 100, 250, 50), fill='blue', width=2)
draw.text((150, 20), "Sales Dashboard", fill='black')
draw.text((10, 270), "Months", fill='black')
draw.text((10, 10), "Sales", fill='black')

# Save the image
img.save('sales_dashboard.png')
print("Image saved")