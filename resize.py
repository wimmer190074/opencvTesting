import cv2

# load and display image
image = cv2.imread('image5.jpg')

# set new dimensions for image
new_dim = (500, 500)

# resize image according to set dimensions
resized_img = cv2.resize(image, new_dim, interpolation= cv2.INTER_AREA)

# display resized image
cv2.imshow("Square image", resized_img)
cv2.waitKey(0)
cv2.imwrite('result_resize.jpg', resized_img)

