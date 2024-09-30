7# Import essential libraries
import requests
import cv2
import numpy as np
import imutils
import os
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import time


def cam_cap() :
    url = "http://192.168.37.253:8080/shot.jpg"


    key = cv2. waitKey(0)
    webcam = cv2.VideoCapture(0)
    cv2.namedWindow("test")
    while True:
        try :
            #img_resp = requests.get(url)
            #img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
            #img = cv2.imdecode(img_arr, -1)
            #img = imutils.resize(img, width=1000, height=1800)
            #print(img)
            #print(img_arr)
            #cv2.imshow("Android_cam", img)

            #key = cv2.waitKey(1)

            ret, frame = webcam.read()
            if not ret:
                print("failed to grab frame")
                break
            img_arr = np.array(bytearray(frame), dtype=np.uint8)
            img = cv2.imdecode(img_arr, -1)
            cv2.imshow("test", frame)
            key = cv2.waitKey(1)


            #if key == ord('s'):
            cv2.imwrite(filename='saved_img.jpg', img=frame)
            webcam.release()
            img_new = cv2.imread('saved_img.jpg', cv2.IMREAD_GRAYSCALE)
            img_new = cv2.imshow("Captured Image", img_new)
            cv2.waitKey(1650)
            cv2.destroyAllWindows()
            print("Processing image...")
            img_ = cv2.imread('saved_img.jpg', cv2.IMREAD_ANYCOLOR)
            print("Converting RGB image to grayscale...")
            gray = cv2.cvtColor(img_, cv2.COLOR_BGR2GRAY)
            print("Converted RGB image to grayscale...")
            print("Resizing image to 28x28 scale...")
            img_ = cv2.resize(gray,(28,28))
            print("Resized...")
            img_resized = cv2.imwrite(filename='saved_img-final.jpg', img=img_)
            print("Image saved!")

            break

            if key == ord('q'):
                print("Turning off camera.")
                webcam.release()
                print("Camera off.")
                print("Program ended.")
                cv2.destroyAllWindows()
                break

        except(KeyboardInterrupt):
            print("Turning off camera.")
            webcam.release()
            print("Camera off.")
            print("Program ended.")
            cv2.destroyAllWindows()
            break

def analyse() :
    print("In analyse")
    im = cv2.imread('saved_img.jpg')
    #im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    bbox, label, conf = cv.detect_common_objects(im)
    output_image = draw_bbox(im, bbox, label, conf)
    #plt.imshow(output_image)
    #plt.show()
    #print('Number of cars in the image is '+ str(label.count('car')))

    car = label.count('car')
    bus = label.count('bus')
    truck = label.count('truck')
    motorcycle = label.count('motorcycle')
    vechile = car + bus + truck + motorcycle
    print('Number of vechile in the image is :',vechile )
    return vechile

def dealay(ans):
    for i in reversed(range(ans[0]+1)):
        print(i)
        time.sleep(1)


# Signal code
class SmartTraffic_DEMO :
    S1 = 0
    S2 = 0
    S3 = 0
    S4 = 0
    R1 = 90
    R2 = 90
    R3 = 90
    R4 = 90
    G1 = 30
    G2 = 30
    G3 = 30
    G4 = 30
    @staticmethod
    def  compare( S2,  S3) :
        ans = [0] * (4)
        diff = 0
        Ga = 30
        Gb = 30
        Ra = 90
        Rb = 90
        diff = S2 - S3
        if (diff < -10) :
            Gb += 10
            Rb -= 10
            Ga -= 10
            Ra += 10
        if (diff > 10) :
            Ga += 10
            Ra -= 10
            Gb -= 10
            Rb += 10
        ans[0] = Ga
        ans[1] = Ra
        ans[2] = Gb
        ans[3] = Rb
        return ans
    def SetGreen(self) :
        @staticmethod
        def main(args) :
            ans = [0] * (4)
        sc =  "Python-inputs"
        #print("Enter value of Vehicle count at S2 & S3: ")
        #SmartTraffic_DEMO.S2 = int(input())
        #SmartTraffic_DEMO.S3 = int(input())

        # SIGNAL 2 -3
        cam_cap()
        SmartTraffic_DEMO.S2 = analyse()
        cam_cap()
        SmartTraffic_DEMO.S3 = analyse()


        ans = SmartTraffic_DEMO.compare(SmartTraffic_DEMO.S2, SmartTraffic_DEMO.S3)
        print(str(ans[0]) + " " + str(ans[2]))
        dealay(ans)
        SmartTraffic_DEMO.G2 = 30
        SmartTraffic_DEMO.R2 = 90
        #print("Enter value of Vehicle count at S3 & S4: ")
        #SmartTraffic_DEMO.S3 = int(input())
        #SmartTraffic_DEMO.S4 = int(input())

        # SIGNAL 3-4
        cam_cap()
        SmartTraffic_DEMO.S3 = analyse()
        cam_cap()
        SmartTraffic_DEMO.S4 = analyse()

        ans = SmartTraffic_DEMO.compare(SmartTraffic_DEMO.S3, SmartTraffic_DEMO.S4)
        print(str(ans[0]) + " " + str(ans[2]))
        dealay(ans)
        SmartTraffic_DEMO.G3 = 30
        SmartTraffic_DEMO.R3 = 90

        # SIGNAL 4-1
        cam_cap()
        SmartTraffic_DEMO.S4 = analyse()
        cam_cap()
        SmartTraffic_DEMO.S1 = analyse()


        ans = SmartTraffic_DEMO.compare(SmartTraffic_DEMO.S2, SmartTraffic_DEMO.S3)
        print(str(ans[0]) + " " + str(ans[2]))
        dealay(ans)
        SmartTraffic_DEMO.G4 = 30
        SmartTraffic_DEMO.R4 = 90

        # SIGNAL 1-2
        cam_cap()
        SmartTraffic_DEMO.S1 = analyse()
        cam_cap()
        SmartTraffic_DEMO.S2 = analyse()


        ans = SmartTraffic_DEMO.compare(SmartTraffic_DEMO.S2, SmartTraffic_DEMO.S3)
        print(str(ans[0]) + " " + str(ans[2]))
        dealay(ans)
        SmartTraffic_DEMO.G1 = 30
        SmartTraffic_DEMO.R1 = 90


if _name=="main_":
    std = SmartTraffic_DEMO()
    std.SetGreen()


#cam_cap()
#x = analyse()
