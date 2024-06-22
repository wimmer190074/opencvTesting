import numpy as np
import cv2

def denoise_image(input_image_path, output_image_path, filter_size=3, high_freq_weight=0.1):
    # Read the original color image
    img_color = cv2.imread(input_image_path)

    # Convert the color image to grayscale
    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)

    # Apply Fourier Transform to grayscale image
    f_gray = np.fft.fft2(img_gray)
    fshift_gray = np.fft.fftshift(f_gray)

    # Define a mask (e.g., a high pass filter) to remove noise from high frequencies
    mask = np.zeros_like(fshift_gray)
    mask_center = (fshift_gray.shape[0]//2, fshift_gray.shape[1]//2)
    mask_width = 30
    mask[mask_center[0]-mask_width:mask_center[0]+mask_width,
         mask_center[1]-mask_width:mask_center[1]+mask_width] = 1

    # Apply the mask to the Fourier transformed grayscale image
    fshift_masked_gray = fshift_gray * mask

    # Perform inverse Fourier transform for grayscale image
    inv_fshift_gray = np.fft.ifftshift(fshift_masked_gray)
    filtered_gray_image = np.fft.ifft2(inv_fshift_gray)
    filtered_gray_image = np.abs(filtered_gray_image)

    # Combine the filtered grayscale image with color channels to form the recolored image
    filtered_rgb_image = np.zeros_like(img_color)
    for i in range(3):
        filtered_rgb_image[:,:,i] = filtered_gray_image * high_freq_weight + (1 - high_freq_weight) * img_color[:,:,i]

    # Apply Median Filtering to remove any remaining noise
    filtered_rgb_image = cv2.medianBlur(np.uint8(filtered_rgb_image), filter_size)

    # Export the denoised and recolored image
    cv2.imwrite(output_image_path, filtered_rgb_image)
    print("Denoised and recolored image saved successfully!")

# Example usage
input_image_path = "image11.jpg"
output_image_path = "denoised_recolored_image1111.jpg"
denoise_image(input_image_path, output_image_path, filter_size=3, high_freq_weight=0.15)
