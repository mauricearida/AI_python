import numpy as np
import cv2

img = cv2.imread("messi5.jpg")  # Read an image from a file. The '1' means the image is read in color.
img2 = cv2.imread("opencv-logo.png")  # Read an image from a file.

print(img.shape)  # Print the shape of the image. This returns a tuple containing number of rows, columns, and channels (if image is color)
print(img.size)  # Print the total number of pixels in the image
print(img.dtype)  # Print the data type of the image. This is usually 'uint8' for images.

b, g, r = cv2.split(img)

img = cv2.merge((b, g, r))

# Duplicate the ball's place in the messi picture
ball = img[280:340, 330:390]
img[273:333, 100:160] = ball

# Resize the images
img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))


# Stick images in top of each other after resizng them , and specify the opacity
dst = cv2.addWeighted(img, 0.9, img2, 0.1, 0)


# img = np.zeros([512, 512, 3], np.uint8)


"""
||||||||||||||||||||||||||||||||||||||||||
||||||||| beneath is for drawing |||||||||
||||||||||||||||||||||||||||||||||||||||||
"""

# img = cv2.line(img, (0, 0), (255, 255), (147, 96, 44), 5)
# img = cv2.arrowedLine(img, (0, 255), (255, 255), (255, 0, 0), 10)
# img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)
# img = cv2.circle(img, (447, 63), 63, (0, 255, 0), 10)
# font = cv2.FONT_HERSHEY_SIMPLEX
# img = cv2.putText(img, "OpenCV", (10, 500), font, 4, (255, 255, 255), 10, cv2.LINE_AA)

cv2.imshow("image", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
