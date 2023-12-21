
#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp

Nfing = 5
cap = cv2.VideoCapture(0)
myname = "Flook"  
#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                if id == 4:
                    id4 = int(id)
                    cx4 = cx
                if id == 3:
                    id3 = int(id)
                    cx3 = cx
                if id == 8:
                    id8 = int(id)
                    cy8 = cy
                if id == 6: 
                    id6 = int(id)
                    cy6 = cy
                if id == 12: 
                    id12 = int(id)
                    cy12 = cy
                if id == 10: 
                    id10 = int(id)
                    cy10 = cy  
                if id == 16: 
                    id16 = int(id)
                    cy16 = cy
                if id == 14: 
                    id14 = int(id)
                    cy14 = cy 
                if id == 20: 
                    id20 = int(id)
                    cy20 = cy
                if id == 18: 
                    id18 = int(id)
                    cy18 = cy 
            if cy8 > cy6:
                Nfing = 0           
            elif cy12 > cy10:
                Nfing = 1        
            elif cy16 > cy14:
                Nfing = 2
            elif cy20 > cy18:
                Nfing = 3
            elif cx4 > cx3:
                Nfing = 4
            else:
                Nfing = 5

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.putText(img, str(int(Nfing)), (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 255), 3) 

    cv2.putText(img, str(str(myname)), (500, 450), cv2.FONT_HERSHEY_PLAIN, 3,
                (200, 0, 0), 3)
    cv2.imshow("Image", img)
    cv2.waitKey(1)



#Closeing all open windows
#cv2.destroyAllWindows()