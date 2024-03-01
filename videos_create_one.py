import cv2


cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*"XVID")  # fourcc is the codec for the video
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))  # the parameters are the name of the file, the codec, the frames per second and the size of the frame

while cap.isOpened():
    ret, frame = cap.read()  # "ret" is the boolean on if the "frame" variable has a value or not so in JS (let ret = !!frame)

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # gets the width of the frame
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # gets the height of the frame

        out.write(frame)  # writes the frame to the file

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # converts colors
        cv2.imshow("frame", gray)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
