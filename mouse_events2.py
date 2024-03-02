import numpy as np
import cv2


# events = [i for i in dir(cv2) if "EVENT" in i]
# print(events)


def click_event(event, x, y, flags, param):  # Function to handle mouse events
    if event == cv2.EVENT_LBUTTONDOWN:  # If left mouse button clicked
        points.append((x, y))  # Add the point to the list of points
        if len(points) >= 2:  # If there are at least two points
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)  # Draw a line between the last two points
        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # Draw a circle at the clicked point
        cv2.imshow("image", img)  # Show the updated image


# img = np.zeros((512, 512, 3), np.uint8)  # Create a black image (commented out)
img = cv2.imread("lena.jpg")  # Read an image from a file

cv2.imshow("image", img)  # Show the image in a window
points = []  # Initialize an empty list of points

cv2.setMouseCallback("image", click_event)  # Set the click_event function to handle mouse events

cv2.waitKey(0)  # Wait for a keyboard event
cv2.destroyAllWindows()  # Destroy all windows
