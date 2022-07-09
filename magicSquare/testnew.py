import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # weight
cap.set(4, 480)  # height
cap.set(10, 0)  # light
if not cap.isOpened():
    print("Fail to open the camera0")
    exit()
while True:
    rate, frame = cap.read()
    rec_w = 300    # modified
    rec_h = 300
    rec_ws = 60
    rec_hs = 60
    gap = 10
    rec_y = int((frame.shape[0] - rec_h) / 2)
    rec_x = int((frame.shape[1] - rec_w) / 2)
    top_x = rec_x + int(rec_w/2)
    lef_y = rec_y + int(rec_h/2)
    cv2.circle(frame, (top_x, rec_y), 1, (255, 255, 255), 20)
    cv2.circle(frame, (rec_x, lef_y), 1, (255, 255, 255), 20)
    # big
    cv2.rectangle(frame, (rec_x, rec_y), (rec_x + rec_w, rec_y + rec_h), (0, 255, 0), 2)
    # p1
    cv2.rectangle(frame, (rec_x + gap, rec_y + gap), (rec_x + gap + rec_ws, rec_y + gap + rec_hs), (0, 255, 255))
    # p2
    cv2.rectangle(frame, (top_x - int(rec_ws/2), rec_y + gap), (top_x - int(rec_ws/2) + rec_ws, rec_y + gap + rec_hs), (0, 255, 255))
    # p3
    cv2.rectangle(frame, (rec_x + rec_w - gap - rec_ws, rec_y + gap), (rec_x + rec_w - gap, rec_y + gap + rec_hs), (0, 255, 255))
    # p4
    cv2.rectangle(frame, (rec_x + gap, lef_y - int(rec_hs/2)), (rec_x + gap + rec_ws, lef_y - int(rec_hs/2) + rec_hs), (0, 255, 255))
    # p5
    cv2.rectangle(frame, (top_x - int(rec_ws/2), lef_y - int(rec_hs/2)), (top_x - int(rec_ws/2) + rec_ws, lef_y - int(rec_hs/2) + rec_hs), (0, 255, 255))
    # p6
    cv2.rectangle(frame, (rec_x + rec_w - gap - rec_ws, lef_y - int(rec_hs/2)), (rec_x + rec_w - gap, lef_y - int(rec_hs/2) + rec_hs), (0, 255, 255))
    # p7
    cv2.rectangle(frame, (rec_x + gap, rec_y + rec_h - rec_hs - gap), (rec_x + gap + rec_ws, rec_y + rec_h - gap), (0, 255, 255))
    # p8
    cv2.rectangle(frame, (top_x - int(rec_ws/2),  rec_y + rec_h - rec_hs - gap), (top_x - int(rec_ws/2) + rec_ws, rec_y + rec_h - gap), (0, 255, 255))
    # p9
    cv2.rectangle(frame, (rec_x + rec_w - gap - rec_ws,  rec_y + rec_h - rec_hs - gap), (rec_x + rec_w - gap, rec_y + rec_h - gap), (0, 255, 255))

    cv2.imshow('camera0', frame)
    # select roi
    xmin, ymin, w, h = rec_x + gap, rec_y+gap, rec_ws, rec_hs
    p1 = frame[ymin:ymin + h, xmin:xmin + w].copy()
    cv2.imshow('p1', p1)
    if cv2.waitKey(1) & 0xFF == ord('a'):
        print("camera0 has been quited")
        break

cap.release()
cv2.destroyAllWindows()

