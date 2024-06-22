import cv2

def crop_center(image, aspect_ratio):
    height, width, _ = image.shape

    desired_aspect_ratio = aspect_ratio[0] / aspect_ratio[1]
    current_aspect_ratio = width / height

    if current_aspect_ratio > desired_aspect_ratio:
        # Image is wider than the desired aspect ratio, crop the sides
        new_width = int(height * desired_aspect_ratio)
        start_x = (width - new_width) // 2
        cropped_image = image[:, start_x:start_x + new_width]
    else:
        # Image is taller than the desired aspect ratio, crop the top and bottom
        new_height = int(width / desired_aspect_ratio)
        start_y = (height - new_height) // 2
        cropped_image = image[start_y:start_y + new_height, :]

    return cropped_image

# Load the image
image = cv2.imread('input_crop_wide.jpeg')

# Define the desired aspect ratio (e.g., 4:3)
aspect_ratio = (4, 3)

# Crop the image
cropped_image = crop_center(image, aspect_ratio)

# Display the original and cropped images
cv2.imwrite('result_crop.jpg', cropped_image)

