import cv2
import numpy as np


cap = cv2.VideoCapture(0)


fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = None
recording = False
is_flipped = False  
brightness = 0     

print("Space: 녹화 시작/중지, F: 좌우반전, U: 밝게, D: 어둡게, ESC: 종료")

while True:
    ret, frame = cap.read()
    if not ret: break

    
    if is_flipped:
        frame = cv2.flip(frame, 1)

 
    frame = cv2.convertScaleAbs(frame, alpha=1, beta=brightness)

    display_frame = frame.copy()

  
    if recording:
        cv2.circle(display_frame, (30, 30), 15, (0, 0, 255), -1)
        cv2.putText(display_frame, "REC", (50, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        if out is not None:
            out.write(frame)

    cv2.imshow('Smart Video Recorder', display_frame)

    key = cv2.waitKey(1)
    
   
    if key == ord(' '): 
        recording = not recording
        if recording:
            out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
        else:
            out.release()
    elif key == ord('f'): 
        is_flipped = not is_flipped
    elif key == ord('u'): 
        brightness += 10
    elif key == ord('d'): 
        brightness -= 10
    elif key == 27: 
        break

cap.release()
if out is not None: out.release()
cv2.destroyAllWindows()