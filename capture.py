from fileinput import close
import cv2    

capture = cv2.VideoCapture(0)  

if capture.isOpened() == False:
    print("camera open failed")
    exit()

capNum = int (0)  
while True:  
    ret, frame = capture.read()  

    if not ret:
        print("Can't read camera")
        break;

    cv2.imshow("ex01", cv2.flip(frame, 1))

    if cv2.waitKey(1) == ord('c'): 
        img_captured = cv2.imwrite('./testimagefolder/image%03d.png' % capNum, frame);
        capNum += 1 
    if cv2.waitKey(1) == ord('q'): 
        break;
capture.release()