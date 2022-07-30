#!/usr/bin/python
# -*- coding: utf-8 -*-


import cv2
import numpy as np

flag = 0
small_h = 10
small_w = 10

cap0 = cv2.VideoCapture(0)
cap0.set(3, 640)  # weight
cap0.set(4, 480)  # height
cap0.set(10, 0)  # light
if not cap0.isOpened():
    print("Fail to open the camera0")
    exit()

cap1 = cv2.VideoCapture(2)
cap1.set(3, 640)  # weight
cap1.set(4, 480)  # height
cap1.set(10, 0)  # light
if not cap1.isOpened():
    print("Fail to open the camera1")
    exit()

cap2 = cv2.VideoCapture(4)
cap2.set(3, 640)  # weight
cap2.set(4, 480)  # height
cap2.set(10, 0)  # light
if not cap2.isOpened():
    print("Fail to open the camera2")
    exit()

cap3 = cv2.VideoCapture(6)
cap3.set(3, 640)  # weight
cap3.set(4, 480)  # height
cap3.set(10, 0)  # light
if not cap3.isOpened():
    print("Fail to open the camera3")
    exit()
while True:
    if flag == 0:
        #  ************************************
        #  ***             camera0          ***
        #  ***          on the right(0)     ***
        #  ************************************
        rate0, frame0 = cap0.read()

        # save the scope
        xmin01, ymin01, w01, h01 = 325, 40, small_w, small_h
        p01 = frame0[ymin01:ymin01 + h01, xmin01:xmin01 + w01].copy()
        cv2.imwrite("./select/p01.jpg", p01)

        xmin02, ymin02, w01, h01 = 400, 110, small_w, small_h
        p02 = frame0[ymin02:ymin02 + h01, xmin02:xmin02 + w01].copy()
        cv2.imwrite("./select/p02.jpg", p02)

        xmin03, ymin03, w01, h01 = 480, 190, small_w, small_h
        p03 = frame0[ymin03:ymin03 + h01, xmin03:xmin03 + w01].copy()
        cv2.imwrite("./select/p03.jpg", p03)

        xmin04, ymin04, w01, h01 = 260, 110, small_w, small_h
        p04 = frame0[ymin04:ymin04 + h01, xmin04:xmin04 + w01].copy()
        cv2.imwrite("./select/p04.jpg", p04)

        xmin05, ymin05, w01, h01 = 340, 190, small_w, small_h
        p05 = frame0[ymin05:ymin05 + h01, xmin05:xmin05 + w01].copy()
        cv2.imwrite("./select/p05.jpg", p05)

        xmin06, ymin06, w01, h01 = 390, 230, small_w, small_h
        p06 = frame0[ymin06:ymin06 + h01, xmin06:xmin06 + w01].copy()
        cv2.imwrite("./select/p06.jpg", p06)

        xmin07, ymin07, w01, h01 = 185, 190, small_w, small_h
        p07 = frame0[ymin07:ymin07 + h01, xmin07:xmin07 + w01].copy()
        cv2.imwrite("./select/p07.jpg", p07)

        xmin08, ymin08, w02, h02 = 285, 250, small_w, small_h
        p08 = frame0[ymin08:ymin08 + h02, xmin08:xmin08 + w02].copy()
        cv2.imwrite("./select/p08.jpg", p08)

        xmin09, ymin09, w02, h02 = 340, 345, small_w, small_h
        p09 = frame0[ymin09:ymin09 + h02, xmin09:xmin09 + w02].copy()
        cv2.imwrite("./select/p09.jpg", p09)
        flag = 1
        cap0.release()
    if flag == 1:
        #  ************************************
        #  ***             camera1          ***
        #  ***          on the left(1)      ***
        #  ************************************
        rate1, frame1 = cap1.read()
        # save the scope
        xmin11, ymin11, w11, h11 = 150, 200, small_w, small_h
        p11 = frame1[ymin11:ymin11 + h11, xmin11:xmin11 + w11].copy()
        cv2.imwrite("./select/p11.jpg", p11)

        xmin12, ymin12, w11, h11 = 220, 140, small_w, small_h
        p12 = frame1[ymin12:ymin12 + h11, xmin12:xmin12 + w11].copy()
        cv2.imwrite("./select/p12.jpg", p12)

        xmin13, ymin13, w11, h11 = 300, 70, small_w, small_h
        p13 = frame1[ymin13:ymin13 + h11, xmin13:xmin13 + w11].copy()
        cv2.imwrite("./select/p13.jpg", p13)

        xmin14, ymin14, w11, h11 = 240, 240, small_w, small_h
        p14 = frame1[ymin14:ymin14 + h11, xmin14:xmin14 + w11].copy()
        cv2.imwrite("./select/p14.jpg", p14)

        xmin15, ymin15, w11, h11 = 290, 210, small_w, small_h
        p15 = frame1[ymin15:ymin15 + h11, xmin15:xmin15 + w11].copy()
        cv2.imwrite("./select/p15.jpg", p15)

        xmin16, ymin16, w11, h11 = 360, 150, small_w, small_h
        p16 = frame1[ymin16:ymin16 + h11, xmin16:xmin16 + w11].copy()
        cv2.imwrite("./select/p16.jpg", p16)

        xmin17, ymin17, w11, h11 = 290, 350, small_w, small_h
        p17 = frame1[ymin17:ymin17 + h11, xmin17:xmin17 + w11].copy()
        cv2.imwrite("./select/p17.jpg", p17)

        xmin18, ymin18, w12, h12 = 355, 255, small_w, small_h
        p18 = frame1[ymin18:ymin18 + h12, xmin18:xmin18 + w12].copy()
        cv2.imwrite("./select/p18.jpg", p18)

        xmin19, ymin19, w12, h12 = 435, 220, small_w, small_h
        p19 = frame1[ymin19:ymin19 + h12, xmin19:xmin19 + w12].copy()
        cv2.imwrite("./select/p19.jpg", p19)
        flag = 2
        cap1.release()
    if flag == 2:
        #  ************************************
        #  ***             camera2          ***
        #  ***          on the front(2)     ***
        #  ***          on the top(3)      ***
        #  ************************************
        rate2, frame2 = cap2.read()
        # save the scope
        xmin21, ymin21, w21, h21 = 330, 210, small_w, small_h
        p21 = frame2[ymin21:ymin21 + h21, xmin21:xmin21 + w21].copy()
        cv2.imwrite("./select/p21.jpg", p21)

        xmin22, ymin22, w21, h21 = 230, 210, small_w, small_h
        p22 = frame2[ymin22:ymin22 + h21, xmin22:xmin22 + w21].copy()
        cv2.imwrite("./select/p22.jpg", p22)

        xmin23, ymin23, w21, h21 = 110, 205, small_w, small_h
        p23 = frame2[ymin23:ymin23 + h21, xmin23:xmin23 + w21].copy()
        cv2.imwrite("./select/p23.jpg", p23)

        xmin24, ymin24, w21, h21 = 325, 145, small_w, small_h
        p24 = frame2[ymin24:ymin24 + h21, xmin24:xmin24 + w21].copy()
        cv2.imwrite("./select/p24.jpg", p24)

        xmin25, ymin25, w21, h21 = 220, 145, small_w, small_h
        p25 = frame2[ymin25:ymin25 + h21, xmin25:xmin25 + w21].copy()
        cv2.imwrite("./select/p25.jpg", p25)

        xmin26, ymin26, w21, h21 = 120, 135, small_w, small_h
        p26 = frame2[ymin26:ymin26 + h21, xmin26:xmin26 + w21].copy()
        cv2.imwrite("./select/p26.jpg", p26)

        xmin27, ymin27, w21, h21 = 325, 80, small_w, small_h
        p27 = frame2[ymin27:ymin27 + h21, xmin27:xmin27 + w21].copy()
        cv2.imwrite("./select/p27.jpg", p27)

        xmin28, ymin28, w21, h21 = 230, 80, small_w, small_h
        p28 = frame2[ymin28:ymin28 + h21, xmin28:xmin28 + w21].copy()
        cv2.imwrite("./select/p28.jpg", p28)

        xmin29, ymin29, w21, h21 = 140, 80, small_w, small_h
        p29 = frame2[ymin29:ymin29 + h21, xmin29:xmin29 + w21].copy()
        cv2.imwrite("./select/p29.jpg", p29)
        # ***********************************************************************
        xmin31, ymin31, w31, h31 = 320, 405, small_w, small_h
        p31 = frame2[ymin31:ymin31 + h31, xmin31:xmin31 + w31].copy()
        cv2.imwrite("./select/p31.jpg", p31)

        xmin32, ymin32, w31, h31 = 220, 405, small_w, small_h
        p32 = frame2[ymin32:ymin32 + h31, xmin32:xmin32 + w31].copy()
        cv2.imwrite("./select/p32.jpg", p32)

        xmin33, ymin33, w31, h31 = 130, 410, small_w, small_h
        p33 = frame2[ymin33:ymin33 + h31, xmin33:xmin33 + w31].copy()
        cv2.imwrite("./select/p33.jpg", p33)

        xmin34, ymin34, w31, h31 = 320, 360, small_w, small_h
        p34 = frame2[ymin34:ymin34 + h31, xmin34:xmin34 + w31].copy()
        cv2.imwrite("./select/p34.jpg", p34)

        xmin35, ymin35, w31, h31 = 220, 360, small_w, small_h
        p35 = frame2[ymin35:ymin35 + h31, xmin35:xmin35 + w31].copy()
        cv2.imwrite("./select/p35.jpg", p35)

        xmin36, ymin36, w31, h31 = 115, 360, small_w, small_h
        p36 = frame2[ymin36:ymin36 + h31, xmin36:xmin36 + w31].copy()
        cv2.imwrite("./select/p36.jpg", p36)

        xmin37, ymin37, w31, h31 = 330, 290, small_w, small_h
        p37 = frame2[ymin37:ymin37 + h31, xmin37:xmin37 + w31].copy()
        cv2.imwrite("./select/p37.jpg", p37)

        xmin38, ymin38, w31, h31 = 220, 295, small_w, small_h
        p38 = frame2[ymin38:ymin38 + h31, xmin38:xmin38 + w31].copy()
        cv2.imwrite("./select/p38.jpg", p38)

        xmin39, ymin39, w31, h31 = 110, 290, small_w, small_h
        p39 = frame2[ymin39:ymin39 + h31, xmin39:xmin39 + w31].copy()
        cv2.imwrite("./select/p39.jpg", p39)
        flag = 3
        cap2.release()
    if flag == 3:
        #  ************************************
        #  ***             camera3          ***
        #  ***          on the button(4)     ***
        #  ***          on the back(5)      ***
        #  ************************************
        rate3, frame3 = cap3.read()
        # save the scope
        xmin41, ymin41, w41, h41 = 240, 40, small_w, small_h
        p41 = frame3[ymin41:ymin41 + h41, xmin41:xmin41 + w41].copy()
        cv2.imwrite("./select/p41.jpg", p41)

        xmin42, ymin42, w41, h41 = 330, 40, small_w, small_h
        p42 = frame3[ymin42:ymin42 + h41, xmin42:xmin42 + w41].copy()
        cv2.imwrite("./select/p42.jpg", p42)

        xmin43, ymin43, w41, h41 = 435, 35, small_w, small_h
        p43 = frame3[ymin43:ymin43 + h41, xmin43:xmin43 + w41].copy()
        cv2.imwrite("./select/p43.jpg", p43)

        xmin44, ymin44, w41, h41 = 240, 110, small_w, small_h
        p44 = frame3[ymin44:ymin44 + h41, xmin44:xmin44 + w41].copy()
        cv2.imwrite("./select/p44.jpg", p44)

        xmin45, ymin45, w41, h41 = 340, 110, small_w, small_h
        p45 = frame3[ymin45:ymin45 + h41, xmin45:xmin45 + w41].copy()
        cv2.imwrite("./select/p45.jpg", p45)

        xmin46, ymin46, w41, h41 = 440, 100, small_w, small_h
        p46 = frame3[ymin46:ymin46 + h41, xmin46:xmin46 + w41].copy()
        cv2.imwrite("./select/p46.jpg", p46)

        xmin47, ymin47, w41, h41 = 220, 180, small_w, small_h
        p47 = frame3[ymin47:ymin47 + h41, xmin47:xmin47 + w41].copy()
        cv2.imwrite("./select/p47.jpg", p47)

        xmin48, ymin48, w41, h41 = 350, 180, small_w, small_h
        p48 = frame3[ymin48:ymin48 + h41, xmin48:xmin48 + w41].copy()
        cv2.imwrite("./select/p48.jpg", p48)

        xmin49, ymin49, w41, h41 = 440, 180, small_w, small_h
        p49 = frame3[ymin49:ymin49 + h41, xmin49:xmin49 + w41].copy()
        cv2.imwrite("./select/p49.jpg", p49)
        # ***********************************************************************
        xmin51, ymin51, w51, h51 = 470, 410, small_w, small_h
        p51 = frame3[ymin51:ymin51 + h51, xmin51:xmin51 + w51].copy()
        cv2.imwrite("./select/p51.jpg", p51)

        xmin52, ymin52, w51, h51 = 360, 420, small_w, small_h
        p52 = frame3[ymin52:ymin52 + h51, xmin52:xmin52 + w51].copy()
        cv2.imwrite("./select/p52.jpg", p52)

        xmin53, ymin53, w51, h51 = 260, 420, small_w, small_h
        p53 = frame3[ymin53:ymin53 + h51, xmin53:xmin53 + w51].copy()
        cv2.imwrite("./select/p53.jpg", p53)

        xmin54, ymin54, w51, h51 = 450, 350, small_w, small_h
        p54 = frame3[ymin54:ymin54 + h51, xmin54:xmin54 + w51].copy()
        cv2.imwrite("./select/p54.jpg", p54)

        xmin55, ymin55, w51, h51 = 350, 350, small_w, small_h
        p55 = frame3[ymin55:ymin55 + h51, xmin55:xmin55 + w51].copy()
        cv2.imwrite("./select/p55.jpg", p55)

        xmin56, ymin56, w51, h51 = 240, 360, small_w, small_h
        p56 = frame3[ymin56:ymin56 + h51, xmin56:xmin56 + w51].copy()
        cv2.imwrite("./select/p56.jpg", p56)

        xmin57, ymin57, w51, h51 = 450, 270, small_w, small_h
        p57 = frame3[ymin57:ymin57 + h51, xmin57:xmin57 + w51].copy()
        cv2.imwrite("./select/p57.jpg", p57)

        xmin58, ymin58, w51, h51 = 340, 270, small_w, small_h
        p58 = frame3[ymin58:ymin58 + h51, xmin58:xmin58 + w51].copy()
        cv2.imwrite("./select/p58.jpg", p58)

        xmin59, ymin59, w51, h51 = 240, 280, small_w, small_h
        p59 = frame3[ymin59:ymin59 + h51, xmin59:xmin59 + w51].copy()
        cv2.imwrite("./select/p59.jpg", p59)

        flag = 4
        cap3.release()
    if flag == 4:
        print("finished")
        break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("camera2 has been quited")
        break

