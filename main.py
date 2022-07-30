
import cv2
import numpy as np


def color_histogram_of_test_image(test_src_image):
    image = test_src_image
    chans = cv2.split(image)
    colors = ('b', 'g', 'r')
    features = []
    feature_data = ''
    counter = 0
    for (chan, color) in zip(chans, colors):
        counter = counter + 1
        hist = cv2.calcHist([chan], [0], None, [256], [0, 256])
        features.extend(hist)
        # find the peak pixel values for R, G, and B
        elem = np.argmax(hist)
        if counter == 1:
            blue = str(elem)
        elif counter == 2:
            green = str(elem)
        elif counter == 3:
            red = str(elem)
            feature_data = red + ',' + green + ',' + blue
            print(feature_data)


def presolving(save_src_image):
    image = save_src_image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred, 20, 40)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(canny, kernel, iterations=2)
    # 闭运算，先膨胀再腐蚀，可以填充孔洞（√）should be corrected
    dilated = cv2.morphologyEx(dilated, cv2.MORPH_OPEN, kernel, iterations=2)
    cv2.imshow("open", dilated)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    results = []
    candidate = []
    '''
    for k in range(0, len(contours)):
        x1, y1, w1, h1 = cv2.boundingRect(contours[k])
        cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (153, 153, 0), 5)
    '''
    for i in range(0, len(contours)):  # classify by the area and w/h   ** the parameters modify may need
        area = cv2.contourArea(contours[i])
        if 5000 < area < 100000:
            candidate.append(contours[i])
    for j in range(0, len(candidate)):
        x, y, w, h = cv2.boundingRect(candidate[j])
        if (w/h > 0.7) & (w/h < 1.3):
            results.append(candidate[j])
    cv2.drawContours(image, candidate, -1, (0, 0, 255), 3)
    cv2.imwrite("./pre_solving.jpg", image)
    cv2.namedWindow("pre_solving", 0)
    cv2.resizeWindow("pre_solving", 640, 640)
    cv2.imshow("pre_solving", image)

    cv2.waitKey(0)

'''
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # weight
cap.set(4, 480)  # height
cap.set(10, 0)  # light
if not cap.isOpened():
    print("Fail to open the camera0")
    exit()
while True:
    rate, frame = cap.read()
    cv2.imshow('camera0', frame)
    
        if cv2.waitKey(1) & 0xFF == ord('0'):
            print("camera0 has been quited")
            break
    
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("./save.jpg", frame)
        presolving(frame)
        break

cap.release()
cv2.destroyAllWindows()

'''
test = cv2.imread("save.jpg")
presolving(test)
