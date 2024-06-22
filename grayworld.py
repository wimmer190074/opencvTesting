import cv2
import numpy as np

def gray_world(image):
    # Apply the Gray World algorithm
    image_grayworld = ((image * (image.mean() / image.mean(axis=(0, 1)))).clip(0, 255).astype(np.uint8))

    # Exclude alpha or opacity channel (transparency)
    if image_grayworld.shape[2] == 4:
        image_grayworld[:, :, 3] = 255

    return image_grayworld

# Read the image using OpenCV
image = cv2.imread('image9.jpg') 

# Convert the image from BGR to RGB (OpenCV reads images in BGR format by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Call the function to apply the Gray World algorithm
result_image = gray_world(image_rgb)

# Display the resulting image
cv2.imshow('Gray World Corrected Image', result_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('result_gray.jpg', result_image)
