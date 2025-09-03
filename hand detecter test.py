import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import numpy as np

# Webcam setup
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Screen Size
screen_width, screen_height = pyautogui.size()

# Smoothing variables
plocX, plocY = 0, 0
clocX, clocY = 0, 0
smoothening = 3

# Drag flag
dragging = False

cv2.namedWindow("Virtual Mouse (Smooth)", cv2.WINDOW_NORMAL)
cv2.setWindowProperty("Virtual Mouse (Smooth)", cv2.WND_PROP_TOPMOST, 1)

while True:
    success, img = cap.read()
    if not success:
        print("❌ Camera not working!")
        break

    img = cv2.flip(img, 1)
    hands, img = detector.findHands(img, flipType=False)

    if hands:
        lmList = hands[0]["lmList"]
        fingers = detector.fingersUp(hands[0])

        # 👇 Debugging ke liye print
        print("Fingers:", fingers)

        x1, y1 = lmList[8][0], lmList[8][1]  # Index finger

        # Mapping to screen
        x3 = np.interp(x1, (100, 540), (0, screen_width))
        y3 = np.interp(y1, (100, 380), (0, screen_height))

        # Smooth cursor movement
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        pyautogui.moveTo(int(clocX), int(clocY))
        plocX, plocY = clocX, clocY

        # -------- Left Click (Index + Middle finger close)
        if fingers[1] == 1 and fingers[2] == 1:
            length, _, _ = detector.findDistance(lmList[8][:2], lmList[12][:2])
            if length < 35:
                pyautogui.click()

        # -------- Right Click (Thumb + Pinky up)
        if fingers == [0, 0, 0, 0, 1]:
            pyautogui.rightClick()

        # -------- Scroll Up (Index + Middle + Ring UP, Pinky DOWN)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 0:
            pyautogui.scroll(200)

        # -------- Scroll Down (Index + Middle + Ring + Pinky UP)
        if fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
            pyautogui.scroll(-200)

        # -------- Drag & Drop (Only Index finger up)
        if fingers == [0, 1, 0, 0, 0]:
            if not dragging:
                pyautogui.mouseDown()
                dragging = True
        else:
            if dragging:
                pyautogui.mouseUp()
                dragging = False

    # Show Window
    cv2.imshow("Virtual Mouse (Smooth)", img)

    # Exit Key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
