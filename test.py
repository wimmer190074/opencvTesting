from __future__ import print_function
import numpy as np
import argparse
import cv2

def automatic_gamma_adjust(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculate histogram
    hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

    # Find the cumulative distribution function
    cdf = hist.cumsum()
    cdf_normalized = cdf / cdf[-1]

    # Calculate the gamma value based on the cumulative distribution function
    gamma = 1 / (np.argmax(cdf_normalized > 0.99) / 255 + 0.01)

    # Adjust gamma based on image brightness
    if gamma > 1.0:
        gamma = min(gamma, 2.0)  # Cap the gamma value at 2.0 for overexposed images
    else:
        gamma = max(gamma, 0.5)  # Set a minimum gamma value of 0.5 for underexposed images
    
    print("Automatic Gamma Adjustment: Gamma =", gamma)

    # Apply gamma correction
    adjusted_image = adjust_gamma(image, gamma)

    return adjusted_image

def adjust_gamma(image, gamma=1.0):
    # build a lookup table mapping the pixel values [0, 255] to
    # their adjusted gamma values
    invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** invGamma) * 255
        for i in np.arange(0, 256)]).astype("uint8")
    return cv2.LUT(image, table)

img_src = cv2.imread('image6.jpg', 1)
img = automatic_gamma_adjust(img_src)

cv2.imwrite('image_adjusted.jpg', img)  # Save the adjusted image as 'image_adjusted.jpg'
