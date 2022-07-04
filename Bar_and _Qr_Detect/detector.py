import cv2
from pyzbar import pyzbar

video = cv2.VideoCapture(0)
while True:
    ret,frame = video.read()

    for i in pyzbar.decode(frame):
        (x,y,w,h) = i.rect
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        data = i.data.decode("utf-8")
        cv2.putText(frame,data,(x,y-60),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2,cv2.LINE_AA)

    if cv2.waitKey(1) == ord("q"):
        break
    cv2.imshow("window",frame)
    cv2.waitKey(1)

video.release()
cv2.destroyAllWindows()