import cv2

img = cv2.imread("lena.jpg", 0)
# "1"  Loads a color image. Any transparency of image will be neglected. It is the default flag.
# "0"  Loads image in grayscale mode
# "-1" Loads image as such including alpha channel.

print(img)

cv2.imshow("image", img)
key = cv2.waitKey(0)

if key == 27:  # if "Esc" is pressed
    cv2.destroyAllWindows()
elif key == ord("s"):  # if "s" is pressed
    cv2.imwrite("lena_copy.png", img)
    cv2.destroyAllWindows()

    # 1:23:00
