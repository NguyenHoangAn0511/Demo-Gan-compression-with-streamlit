import cv2

input_video_path = 'data/compress_resize.mp4'

cap = cv2.VideoCapture(input_video_path)
out = cv2.VideoWriter('output_2.mp4', -1, 20.0, (512,512))
while(cap.isOpened()):
    ret, frame = cap.read()
    print(frame, ret)
    if ret:
        
        frame = cv2.resize(frame, (512,512))
        # cv2.imshow("frame", frame)
        out.write(frame)
    else:
        break

cap.release()
cv2.destroyAllWindows()