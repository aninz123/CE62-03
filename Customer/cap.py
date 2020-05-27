import cv2


videoCaptureObject = cv2.VideoCapture('nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1280, height=1280, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink' , cv2.CAP_GSTREAMER)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    #cv2.imwrite("Data/"+"cap.jpg",frame)
    cv2.imwrite("darknet-master/"+"cap.jpg",frame)	
    result = False
videoCaptureObject.release()
cv2.destroyAllWindows()
print('CAP Suc')
