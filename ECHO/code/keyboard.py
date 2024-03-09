import cv2 as cv
import mediapipe as mp
import pyautogui as pg

cam = cv.VideoCapture(0)

mphands = mp.solutions.hands
hands = mphands.Hands()


clk = 1
keys = [['Q','W','E','R','T','Y','U','I','O','P','1','2','3'], 
        ['A','S','D','F','G','H','J','K','L',':','4','5','6'],
        ['Z','X','C','V','B','N','M',',','.','?','7','8','9'],
        ]

size = 100/100
buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        x = int((j*45*size)+ 25)
        y = int((i*70*size) + 60)
        h = int(x + 40*size)
        w = int(y + 40*size)
        buttonList.append([x,y,h,w, key])

def S_keys():
    xs = lambda i : int((i*45*size) + 25)
    ys = lambda y : int((y*75*size) + 60)
    hws = lambda hw : int(hw + 50*size)
    buttonList.append([xs(0), ys(len(keys)), hws(xs(2.8)), hws(ys(len(keys))), 'backspace'])
    buttonList.append([xs(4), ys(len(keys)), hws(xs(5.8)), hws(ys(len(keys))), 'capslock'])
    buttonList.append([xs(7), ys(len(keys)), hws(xs(8.8)), hws(ys(len(keys))), 'enter'])
    buttonList.append([xs(10), ys(len(keys)), hws(xs(12)), hws(ys(len(keys))), '0'])
    buttonList.append([xs(1), ys(len(keys)+1), hws(xs(9)), hws(ys(len(keys)+1)), ' '])

S_keys()

def drawKey(img, buttonList):
    for x,y,h,w,key in buttonList:
        cv.rectangle(img, (x,y), (h,w), (158,158,158), cv.FILLED,1)
        cv.putText(img, key, (x+12, y+29), cv.FONT_HERSHEY_PLAIN, 1.6, (255,255,255 ),2)


while True:
    succes, img = cam.read()
    img = cv.flip(img, 1)

    h,w,c = img.shape

    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = hands.process(imgRGB)
    if (result.multi_hand_landmarks):
        lmlist = []
        for handsLms in result.multi_hand_landmarks:
            for id, landmarks in enumerate(handsLms.landmark):
                x, y = int(landmarks.x * w), int(landmarks.y * h)
                lmlist.append([id,x,y])
               
        X = lmlist[12][1]
        Y = lmlist[12][2]
        cv.circle(img, (X,Y), 9, (0,255,255), cv.FILLED)
        if (lmlist[8][2] > lmlist[7][2]) and ((clk > 0)):
            cv.circle(img, (X,Y), 9, (0,255,0), cv.FILLED)
            for x,y,h,w,keys in buttonList:
                if x < X < h and y < Y < w:
                    pg.press(keys)
            clk = -1

        elif (lmlist[4][2] < lmlist[3][2]):
            clk = 1
                                  
    drawKey(img, buttonList)

    new_cam=cv.resize(img,(1000,400))
    cv.imshow("webcam", new_cam )

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
    
cv.destroyAllWindows()