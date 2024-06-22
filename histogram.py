import numpy as np
from skimage.io import imread, imsave
from skimage.color import rgb2hsv, hsv2rgb
from skimage.exposure import cumulative_distribution
from skimage import img_as_ubyte

def histogram_equalization(image):
    """
    Perform histogram equalization on each color channel independently.

    Parameters:
    image (ndarray): Input image.

    Returns:
    equalized_image (ndarray): Histogram equalized image.
    """
    # Convert the image to HSV color space
    hsv_image = rgb2hsv(image)

    # Equalize the intensity component (Value channel)
    v_channel = hsv_image[:, :, 2]
    intensity = np.round(v_channel * 255).astype(np.uint8)
    freq, bins = cumulative_distribution(intensity)
    target_bins = np.arange(256)
    target_freq = np.linspace(0, 1, len(target_bins))
    new_vals = np.interp(freq, target_freq, target_bins)

    # Ensure indices are within bounds
    v_channel_indices = img_as_ubyte(v_channel)
    v_channel_indices[v_channel_indices >= len(new_vals)] = len(new_vals) - 1
    v_channel_eq = new_vals[v_channel_indices].astype(float) / 255

    # Combine the equalized intensity channel with the original hue and saturation channels
    equalized_hsv_image = np.dstack((hsv_image[:, :, 0], hsv_image[:, :, 1], v_channel_eq))

    # Convert the equalized HSV image back to RGB color space
    equalized_image = hsv2rgb(equalized_hsv_image)

    return equalized_image

# Load the image
image = imread('P4670764.jpeg')

# Perform histogram equalization while retaining color information
equalized_image = histogram_equalization(image)

# Save the corrected image
imsave('result22_histogram.jpg', img_as_ubyte(equalized_image))
