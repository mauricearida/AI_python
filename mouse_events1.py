import numpy as np
import cv2


# events = [i for i in dir(cv2) if "EVENT" in i]
# print(events)


def click_event(event, x, y, flags, param):  # Function to handle mouse events
    if event == cv2.EVENT_LBUTTONDOWN:  # If left mouse button clicked
        print(x, ", ", y)  # Print the x and y coordinates of the click
        font = cv2.FONT_HERSHEY_SIMPLEX  # Set the font for the text
        strXY = str(x) + ", " + str(y)  # Create a string with the x and y coordinates
        cv2.putText(img, strXY, (x, y), font, 1, (255, 255, 0), 2)  # Put the coordinates on the image
        cv2.imshow("image", img)  # Show the updated image

    if event == cv2.EVENT_RBUTTONDOWN:  # If right mouse button clicked
        blue = img[y, x, 0]  # Get the blue value of the pixel
        green = img[y, x, 1]  # Get the green value of the pixel
        red = img[y, x, 2]  # Get the red value of the pixel
        font = cv2.FONT_HERSHEY_SIMPLEX  # Set the font for the text
        strBGR = str(blue) + ", " + str(green) + ", " + str(red)  # Create a string with the BGR values
        cv2.putText(img, strBGR, (x, y), font, 1, (0, 255, 255), 2)  # Put the BGR values on the image
        cv2.imshow("image", img)  # Show the updated image


# img = np.zeros((512, 512, 3), np.uint8)  # Create a black image
img = cv2.imread("lena.jpg")  # Load the image

cv2.imshow("image", img)  # Show the image in a window

cv2.setMouseCallback("image", click_event)  # Set the click_event function to handle mouse events

cv2.waitKey(0)  # Wait for a keyboard event
cv2.destroyAllWindows()  # Destroy all windows
