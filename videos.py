import cv2


cap = cv2.VideoCapture(0)  # connects to the camera, the parameter is the index for camera
# you can pass it a string which has to be a video .mp4 path

while cap.isOpened():  # checks if the camera is opened
    ret, frame = cap.read()  # "ret" is the boolean on if the "frame" variable has a value or not so in JS (let ret = !!frame)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts colors
    cv2.imshow("frame", gray)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
