from PIL import Image

# Open an RGB image
rgb_image = Image.open('image.jpg')

# Convert RGB image to CMYK
cmyk_image = rgb_image.convert('CMYK')

# Save or display CMYK image
cmyk_image.show()
# Or save the CMYK image
cmyk_image.save('cmyk_image.jpg')
