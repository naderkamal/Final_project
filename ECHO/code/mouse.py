import cv2
import mediapipe
import numpy
import autopy
import time
import pyautogui

cap = cv2.VideoCapture(0)

initHand = mediapipe.solutions.hands
mainHand = initHand.Hands()
draw = mediapipe.solutions.drawing_utils
wScr , hScr = autopy.screen.size()
pX,pY = 0,0
cX,cY = 0,0

def handLandmarks(colorImg):
    landmarkList = []
    landmarkPositions = mainHand.process(colorImg)
    landmarkCheck = landmarkPositions.multi_hand_landmarks
    if landmarkCheck:
        for hand in landmarkCheck:
            for index,landmark in enumerate(hand.landmark):
                draw.draw_landmarks(img,hand,initHand.HAND_CONNECTIONS)
                h,w,c = img.shape
                centerX,centerY = int(landmark.x * w),int(landmark.y * h)
                landmarkList.append([index,centerX,centerY])
    return landmarkList
def fingers(landmarks):
    fingerTips = []
    tipIds = [4,8,12,16,20]
    if landmarks[tipIds[0]][1] > landmarks[tipIds[0] - 1][1]:
        fingerTips.append(1)
    else:
        fingerTips.append(0)
    for id in range(1,5):
        if landmarks[tipIds[id]][2] < landmarks[tipIds[id] - 2][2]:
            fingerTips.append(1)
        else:
            fingerTips.append(0)
    return fingerTips
while True:
    check,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    lmList = handLandmarks(imgRGB)
    if len(lmList) != 0:
        x,y = lmList[12][1:]
        finger = fingers(lmList)
        
        if finger[1] == 1 and finger[2] == 1:
            if finger[4] == 0:
                x3 = numpy.interp(x,(100,640-100),(0,wScr))
                y3 = numpy.interp(y,(100,480-100),(0,hScr))

                cX = pX + (x3-pX) / 7.8
                cY = pY + (y3-pY) / 7.8
                autopy.mouse.move(wScr-cX,cY)
                cv2.circle(img, (x, y), 7, (255, 0, 255), cv2.FILLED)
                pX,pY=cX,cY
        if finger[1] == 1 and finger[2] == 0:
            autopy.mouse.click(autopy.mouse.Button.RIGHT)
            time.sleep(0.25)
        if finger[1] == 0 and finger[2] == 1:
            autopy.mouse.click(autopy.mouse.Button.LEFT)
            time.sleep(0.25)
        if finger[1] == 1 and finger[2] == 1:
            if finger[3] == 1:
                if y>260:
                    pyautogui.scroll(-25)
                if y<220:
                    pyautogui.scroll(25)
                
    new_cam=cv2.resize(img,(1000,400))

    cv2.imshow("webcam", new_cam )

    if cv2.waitKey(20) & 0xFF==ord('d' ):
        break 
cv2.destroyAllWindows()