# I am having a lot of problem in the save section of the program as i failed in the integration of the sddweight function
# Then I also faced a lot of problem while making a confirmation block at the centre of the screen  

import numpy as np
import cv2
from collections import deque
import os

#default called trackbar function 
def setValues(x):
   print("")
global simg

# Creating the trackbars needed for adjusting the marker colour
cv2.namedWindow("Color detectors")
cv2.resizeWindow("Color detectors",400, 280)
cv2.createTrackbar("hue h", "Color detectors", 100, 180,setValues)
cv2.createTrackbar("sat h", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("val h", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("hue l", "Color detectors", 40, 180,setValues)
cv2.createTrackbar("sat l", "Color detectors", 100, 255,setValues)
cv2.createTrackbar("val l", "Color detectors", 100, 255,setValues)

# Giving different arrays to handle colour points of different colour
bpoints = [deque(maxlen=1024)]
gpoints = [deque(maxlen=1024)]
rpoints = [deque(maxlen=1024)]
ypoints = [deque(maxlen=1024)]
spoints = [deque(maxlen=1024)]
ppoints = [deque(maxlen=1024)]
wpoints = [deque(maxlen=1024)]
npoints = [deque(maxlen=1024)]

# These indexes will be used to mark the points in particular arrays of specific colour
blue_index = 0
green_index = 0
red_index = 0
yellow_index = 0
sky_index = 0
pink_index = 0
white_index = 0
black_index = 0


#The kernel to be used for dilation purpose 
kernel = np.ones((5,5),np.uint8)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255),(255,255,0), (255,0,255), (255,255,255), (0, 0, 0)]
colorIndex = 0

    
def colorlist(frame, cen):
    global COLIST
    global colorIndex
    global colors
    STRING = ["Blue","Green","Red","Yellow","Sky","Pink","White","Black"]
    if COLIST is True and SAVE is False:
        frame = cv2.rectangle(frame, (160,65), (255,305), (0,0,0),2)

        for c in range(len(STRING)):
            frame = cv2.line(frame, (160,95+(c*30)), (255,95 + (c*30)), (0,0,0), 2)
            frame = cv2.rectangle(frame, (162,67 + (c*30)), (253,93 + (c*30)), colors[c], -1)
            cv2.putText(frame,STRING[c] , (190, 80+c*30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        cv2.putText(frame,"White" , (190,260), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        
        if colorIndex == 0:
            frame =cv2.circle(frame, (245, 80), 4, (255,255,255), -1 )
        elif colorIndex == 1:
            frame =cv2.circle(frame, (245, 110), 4, (255,255,255), -1 )
        elif colorIndex == 2:
            frame =cv2.circle(frame, (245, 140), 4, (255,255,255), -1 )
        elif colorIndex == 3:
            frame =cv2.circle(frame, (245, 170), 4, (255,255,255), -1 )
        elif colorIndex == 4:
            frame =cv2.circle(frame, (245, 200), 4, (255,255,255), -1 )
        elif colorIndex == 5:
            frame =cv2.circle(frame, (245, 230), 4, (255,255,255), -1 )
        elif colorIndex == 6:
            frame =cv2.circle(frame, (245, 260), 4, (0,0,0), -1 )
        elif colorIndex == 7:
            frame =cv2.circle(frame, (245, 290), 4, (255,255,255), -1 )

        if not(cen is None):
            if 160<cen[0]<255 and 65<cen[1]<95:
                colorIndex = 0
            elif 160<cen[0]<255 and 96<cen[1]<125:
                colorIndex = 1
            elif 160<cen[0]<255 and 126<cen[1]<155:
                colorIndex = 2
            elif 160<cen[0]<255 and 156<cen[1]<185:
                colorIndex = 3
            elif 160<cen[0]<255 and 186<cen[1]<215:
                colorIndex = 4 
            elif 160<cen[0]<255 and 216<cen[1]<245:
                colorIndex = 5
            elif 160<cen[0]<255 and 246<cen[1]<275:
                colorIndex = 6 
            elif 160<cen[0]<255 and 276<cen[1]<305:
                colorIndex = 7
            if not(160<cen[0]<255 and 0<cen[1]<305):
                COLIST = False

def colorsize(frame, cen):
    global COSIZE
    global colsize
    if COSIZE is True and SAVE is False:
        frame = cv2.rectangle(frame, (275,65), (370,215), (0,0,0),2)
        for i in range(5):
            if i%2 == 0:
                p = 255
            else : p = 0
            
            frame = cv2.line(frame, (275,95 + (i*30)), (370,95 + (i*30)), (0,0,0), 2)
            frame = cv2.rectangle(frame, (277,67 + (i*30)), (368,93 + (i*30)), (abs(p -255), abs(p -255), abs(p -255)), -1)
            cv2.putText(frame, str(1+i) +  "px", (310, 85 + (i*30)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (p,p,p), 2, cv2.LINE_AA)
        
        if colsize == 1 :
            frame =cv2.circle(frame, (360, 80), 4, (255,255,255), -1 )
        elif colsize == 2 :
            frame =cv2.circle(frame, (360, 110), 4, (0,0,0), -1 )
        elif colsize == 3 :
            frame =cv2.circle(frame, (360, 140), 4, (255,255,255), -1 )
        elif colsize == 5 :
            frame =cv2.circle(frame, (360, 170), 4, (0,0,0), -1 )
        elif colsize == 7 :
            frame =cv2.circle(frame, (360, 200), 4, (255,255,255), -1 )

        if not(cen is None):
            if 275<cen[0]<370 and 65<cen[1]<95:
                colsize = 1
            elif 275<cen[0]<370 and 96<cen[1]<125:
                colsize = 2 
            elif 275<cen[0]<370 and 126<cen[1]<155:
                colsize = 3
            elif 275<cen[0]<370 and 156<cen[1]<185:
                colsize = 5
            elif 275<cen[0]<370 and 186<cen[1]<215:
                colsize = 7
            if not(275<cen[0]<370 and 0<cen[1]<215):
                COSIZE = False

def save(frame,cen):
    global SAVE
    
    if SAVE == True:
        frame = cv2.rectangle(frame, (200,160), (440, 320), (255,255,255), -1 )
        frame = cv2.rectangle(frame, (200,160), (440, 320), (0,0,0), 3 )
        cv2.putText(frame,"Do you want to save this image ?" ,(210,180), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0,0,0), 2)
        
        frame = cv2.rectangle(frame, (220,260), (280, 300), (0,255,0), -1)
        frame = cv2.rectangle(frame, (220,260), (280, 300), (0,0,0), 2)
        cv2.putText(frame, "YES", (235,285), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

        frame = cv2.rectangle(frame, (360,260), (420, 300), (0,0,255), -1)
        frame = cv2.rectangle(frame, (360,260), (420, 300), (0,0,0), 2)
        cv2.putText(frame, "NO", (380,285), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2)

        if not(cen is None):
            if 220 <= cen[0] <= 280 and 260 <= cen[1] <= 300:
                cv2.imwrite("opencv finger.png", simg)
                OLD = r"C:\Users\suyash\Desktop\KACHRA\laohub\opencv finger.png"
                NEW = r"C:\Users\suyash\Desktop\Delete Me\opencv finger.png"
                OLD = OLD.replace("\\","/")
                NEW = NEW.replace("\\","/")
                os.rename(OLD, NEW)
                SAVE = False
            
            elif 360 <= cen[0] <= 420 and 260 <= cen[1] <= 300:
                SAVE = False

def smart(frame, cen):
    global xrect
    global yrect
    global RECT
    global SMART
    global PSEL
    SHAPE = ["Rectangle", "Circle"]
    if SMART == True:
        global STOP
        cv2.rectangle(frame, (505,450), (600, 390), (0,0,0), 2)

        for c in range(len(SHAPE)):
            frame = cv2.line(frame, (505,450-(c*30)), (600,450 - (c*30)), (0,0,0), 2)
            frame = cv2.rectangle(frame, (503,448 - (c*30)), (600,422 - (c*30)), colors[c], -1)
            cv2.putText(frame,SHAPE[c] , (515, 435 - (c*30)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)

        #if cen[0]
        if cen != None:
            c=0
            if not(505 <= cen[0] <= 600 and 390 <= cen[1] <= 480) and PSEL == False :
                SMART = False
                STOP = False
            elif (505 <= cen[0] <= 600 and 390 <= cen[1] <= 420):
                PSEL = False
            elif (505 <= cen[0] <= 600 and 450 <= cen[1] <= 480):  
                PSEL = False 
            elif (505 <= cen[0] <= 600 and 420 <= cen[1] <= 450) or PSEL == True:
                if c==0:
                    xrect = cen[0]
                    yrect = cen[1]
                    c=1
                    PSEL = True
            
        else:
            if c== 1:
                if c == 1:
                    SMART = False
                    RECT = True
                else:
                    SMART =True
        
                
def rect(frame,cen):
    global RECT 
    global xmax
    global ymax
    global DRAW

    f = frame.copy()
    if cen != None:
        ymax = cen[1]
        xmax = cen[0]
        f = cv2.rectangle(f,(xrect,yrect), (xmax, ymax), (255,255,255),2)
        

    if cen == None and (xmax!=None and ymax != None):
        RECT = False
        DRAW = True
    cv2.imshow("Tracking", f)


def draw():
    global DRAW
    global xrect
    global yrect
    global xmax
    global ymax
    global STOP
    if DRAW is True:
        DRAW = False
        xrect = None
        yrect = None
        xmax = None
        ymax =None
        STOP = False
        

RECT = False
DRAW = False
ymax = None
xmax = None
COLIST = False
COSIZE = False
SAVE = False
SMART = False
PSEL = False
STOP = False
rectangle = []
colsize = 2
blank = np.zeros((480,640,3))

# Loading the default webcam of PC.
cap = cv2.VideoCapture(0)

# Keep looping
while True:
    # Reading the frame from the camera
    ret, frame = cap.read()
    #Flipping the frame to see same side of yours
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    hueh = cv2.getTrackbarPos("hue h", "Color detectors")
    sath = cv2.getTrackbarPos("sat h", "Color detectors")
    valh = cv2.getTrackbarPos("val h", "Color detectors")
    huel = cv2.getTrackbarPos("hue l", "Color detectors")
    satl = cv2.getTrackbarPos("sat l", "Color detectors")
    vall = cv2.getTrackbarPos("val l", "Color detectors")
    Upper_hsv = np.array([hueh,sath,valh])
    Lower_hsv = np.array([huel,satl,vall])
    
    # Adding the colour buttons to the live frame for colour access
    frame = cv2.rectangle(frame, (40,1), (140,65), (122,122,122), -1)
    frame = cv2.rectangle(frame, (160,1), (255,65), colors[0], -1)
    frame = cv2.rectangle(frame, (275,1), (370,65), colors[1], -1)
    frame = cv2.rectangle(frame, (390,1), (485,65), colors[2], -1)
    frame = cv2.rectangle(frame, (505,1), (600,65), colors[3], -1)
    frame = cv2.rectangle(frame, (505,450),(600,480), colors[5], -1 )
  
    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Colour", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Size", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Exit", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Save", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
    cv2.putText(frame, "SMART", (520,468), cv2.FONT_HERSHEY_COMPLEX, 0.4, colors[4], 1, cv2.LINE_AA)

    # Identifying the pointer by making its mask
    Mask = cv2.inRange(hsv, Lower_hsv, Upper_hsv)
    Mask = cv2.erode(Mask, kernel, iterations=1)
    Mask = cv2.morphologyEx(Mask, cv2.MORPH_OPEN, kernel)
    Mask = cv2.dilate(Mask, kernel, iterations=1)
    
    # Find contours for the pointer after idetifying it
    cnts,_ = cv2.findContours(Mask.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    #cv2.imshow("frame", cnts)
    center = None

    # Ifthe contours are formed
    if len(cnts) > 0:
    	# sorting the contours to find biggest 
        cnt = sorted(cnts, key = cv2.contourArea, reverse = True)[0]
        # Get the radius of the enclosing circle around the found contour
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        
        # Calculating the center of the detected contour
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']),colsize)

        
        # Now checking if the user wants to click on any button above the screen 
        if center[1] <= 65:
            if 40 <= center[0] <= 140 and SAVE is False: # Clear Button
                bpoints = [deque(maxlen=1024)]
                gpoints = [deque(maxlen=1024)]
                rpoints = [deque(maxlen=1024)]
                ypoints = [deque(maxlen=1024)]
                spoints = [deque(maxlen=1024)]
                ppoints = [deque(maxlen=1024)]
                wpoints = [deque(maxlen=1024)]
                npoints = [deque(maxlen=1024)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                sky_index = 0
                pink_index = 0
                white_index = 0
                black_index = 0

                blank[:,:,:] = 0
            elif 160 <= center[0] <= 255:
                    #colorIndex = 0 # Blue
                    COLIST = True
            elif 275 <= center[0] <= 370:
                    #colorIndex = 1 # Green
                    COSIZE = True
            elif 390 <= center[0] <= 485:
                    if SAVE is False:
                        break
                    #colorIndex = 2 # Red
            elif 505 <= center[0] <= 600:
                    #colorIndex = 3 # Yellow
                    SAVE = True
        elif center[1]>449:
            if 505<=center[0]<=600:
                SMART = True  
                STOP = True

        elif (COLIST == False and COSIZE == False) and (SAVE == False and STOP == False):
            if colorIndex == 0:
                bpoints[blue_index].appendleft(center)
            elif colorIndex == 1:
                gpoints[green_index].appendleft(center)
            elif colorIndex == 2:
                rpoints[red_index].appendleft(center)
            elif colorIndex == 3:
                ypoints[yellow_index].appendleft(center)
            elif colorIndex == 4:
                spoints[sky_index].appendleft(center)
            elif colorIndex == 5:
                ppoints[pink_index].appendleft(center)
            elif colorIndex == 6:
                wpoints[white_index].appendleft(center)
            elif colorIndex == 7:
                npoints[black_index].appendleft(center)
                 
    # Append the next deques when nothing is detected to avois messing up
    else:
        bpoints.append(deque(maxlen=1024))
        #blue_index += 1
        gpoints.append(deque(maxlen=1024))
        #green_index += 1
        rpoints.append(deque(maxlen=1024))
        #red_index += 1
        ypoints.append(deque(maxlen=1024))
        #yellow_index += 1
        spoints.append(deque(maxlen=1024))
        #blue_index += 1
        ppoints.append(deque(maxlen=1024))
        #green_index += 1
        wpoints.append(deque(maxlen=1024))
        #red_index += 1
        npoints.append(deque(maxlen=1024))
        #yellow_index += 1

    # Draw lines of all the colors on the canvas and frame 
    points = [bpoints, gpoints, rpoints, ypoints, spoints, ppoints, wpoints, npoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1][:2], points[i][j][k][:2], colors[i], points[i][j][k][-1])
                cv2.line(blank, points[i][j][k - 1][:2], points[i][j][k][:2], colors[i], points[i][j][k][-1])
                col = colors[i]
    for x in rectangle:
        cv2.rectangle(frame, (x[0],x[1]),(x[2],x[3]), x[4], 2)
    if SAVE is False:
        simg = frame.copy()
    colorlist(frame, center)
    colorsize(frame, center)
    save(frame, center)
    smart(frame, center)
    if center != None:
        cv2.circle(frame, (center[0], center[1]), 3, (120, 255, 255), 2)
    # Show all the windows
    if RECT is False:
        cv2.imshow("Tracking", frame)
    else:
        rect(frame, center)
        if DRAW is True:
            rectangle.append([xrect, yrect, xmax, ymax, col]) 
        draw()
    cv2.imshow("blank", blank)
    cv2.imshow("mask",Mask)
    
    # If the 'q' key is pressed then stop the application 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and all resources
cap.release()
cv2.destroyAllWindows()