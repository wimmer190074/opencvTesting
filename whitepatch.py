import cv2
import numpy as np
from skimage import img_as_ubyte

def white_patch(image, percentile=100):
    #Apply the White-Patch Algorithm
    white_patch_image = img_as_ubyte(
        (image * 1.0 / np.percentile(image, 
                                     percentile, 
                                     axis=(0, 1))).clip(0, 1))
    return white_patch_image

# Read the image using OpenCV
image = cv2.imread('image11.jpg')  # Replace 'path_to_your_image.jpg' with the path to your image file

# Convert the image from BGR to RGB (OpenCV reads images in BGR format by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Call the white_patch function with the image
result_image = white_patch(image_rgb, percentile=90)

# Display or save the resulting image
# (The result image will be in uint8 format, suitable for visualization or saving)
cv2.imshow('Result Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result_white.jpg', result_image)

