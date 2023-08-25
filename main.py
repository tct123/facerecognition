import cv2

capture = cv2.VideoCapture(0)
cascade = cv2.CascadeClassifier(filename="haarcascade_frontalface_default.xml")
while True:
    _, im = capture.read()
    im_grey = cv2.cvtColor(im, code=cv2.COLOR_BGR2GRAY)
    faces = cascade.detectMultiScale(image=im_grey)
    for x, y, width, height in faces:
        cv2.rectangle(
            im, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=5
        )
    cv2.imshow("Camera", im)
    if cv2.waitKey(1) == ord("q"):
        break
capture.release()
cv2.destroyAllWindows()
