import cv2

# load and display image
image = cv2.imread('image5.jpg')

# get the dimensions of original image
OriginalHeight, OriginalWidth = image.shape[:2]

# get the ratio of *new* width to the *original* width
new_width = 500
ratio = new_width / OriginalWidth

# Then we multiply the ratio with height of the original image
# to get a new height that maintains the same aspect ratio
new_height = int(OriginalHeight * ratio) # must be integer

# This then gives a new dimension for the new image that
# sets the width to 400 pixels and maintains the the image aspect ratio

# define new dimension
new_dim = (new_width, new_height)

# resize image according to set dimensions
resized_img = cv2.resize(image, new_dim, interpolation= cv2.INTER_AREA)

# display resized image
cv2.imshow("Square image", resized_img)
cv2.waitKey(0)
cv2.imwrite('result_resize.jpg', resized_img)
