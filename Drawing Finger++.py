 # While going to rect if the mask goes off at the time of then it starts to show error that only two values passed

# The mistery bug that colors are changing not in a fixed pattern but are randomly change and not changing
# The pattern that is any color above 1 color selected is negating all the olors that are below

import numpy as np
import cv2
from collections import deque
import os
import math as m


#default called trackbar function 
def setValues(x):
   print("")


# Functional variables 
KEYBOARD = [["1","2","3","4","5","6","7","8","9","0"],["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"],
["a", "s", "d", "f", "g", "h", "j", "k", "l"," "], ["z", "x", "c", "v", "b", "n", "m", ".", "\b" ,".."]]
v = None
c = None
reader = None
loc1 = None

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
bpoints = [deque(maxlen=8192)]

# These indexes will be used to mark the points in particular arrays of specific colour
blue_index = 0

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
        global c

        for con in range(len(SHAPE)):
            frame = cv2.line(frame, (505,450-(con*30)), (600,450 - (con*30)), (0,0,0), 2)
            frame = cv2.rectangle(frame, (507,448 - (con*30)), (598,422 - (con*30)), colors[con], -1)
            cv2.putText(frame,SHAPE[con] , (518, 438 - (con*30)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        
        cv2.rectangle(frame, (505, 480), (600, 452), (0,0,255), -1)
        cv2.rectangle(frame, (505, 480), (600, 390), (0,0,0), 2)
        cv2.putText(frame,"Quit" , (518, 468), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)


        if cen != None:
            c=0
            if not(505 <= cen[0] <= 600 and 390 <= cen[1] <= 480) and PSEL == False :
                SMART = False
                STOP = False
            elif (505 <= cen[0] <= 600 and 450 <= cen[1] <= 480):  
                PSEL = False 
            elif ((505 <= cen[0] <= 600 and 390 <= cen[1] <= 450) or PSEL == True) and not(cen is None):
                if c==0:
                    xrect = cen[0]
                    yrect = cen[1]
                    c=1
                    PSEL = True
                    if 390 < cen[1] <= 420 and 505 <= cen[0] <= 600:
                        return ("circle",cen[2])
                    elif 420 < cen[1] <= 450 and 505 <= cen[0] <= 600:
                        return ("rectangle",cen[2])
            
        else:
            if c== 1 :
                SMART = False
                RECT = True
            else:
                SMART =True
        
                
def rect(frame, cen, v):
    global RECT 
    global xmax
    global ymax
    global DRAW

    f = frame.copy()
    if cen != None:
        ymax = cen[1]
        xmax = cen[0]
        if v == "rectangle":
            cv2.rectangle(f,(xrect,yrect), (xmax, ymax), (255,255,255),cen[2])
        elif v == "circle":
            radx = xmax - xrect
            rady = ymax - yrect
            rad = int(m.sqrt((radx*radx) + (rady*rady)))
            cv2.circle(f, (xrect, yrect),rad,(255,255,255), cen[2] )

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

def keyboard():
    global KEY
    global v 
    global c 
    global reader
    global LOC1

    if KEY is True:
        cv2.rectangle(frame, (98,148), (502,402), (0,0,0), 2)
        cv2.rectangle(frame, (100,150), (500, 200), (120,120,120), -1) 
        cv2.rectangle(frame, (100,200), (500, 400), (55,55,55), -1)
        cv2.line(frame, (98, 199), (502,199), (0,0,0), 2)
        for x in range(10):
            for y in range(4):
                cv2.rectangle(frame, (105 + (x*40),210 + (y*50)), (135 + (x*40), 240 + (y*50)),(0,0,0), 1)
                cv2.rectangle(frame, (105 + (x*40),210 + (y*50)), (135 + (x*40), 240 + (y*50)),(200,200,200), -1)
                cv2.putText(frame, KEYBOARD[y][x], (112 + (x*40),230 + (y*50)), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 1)
        
        
        if center is not(None):
            if 100<center[0]<500 and 200<center[1]<400:
                xtext = (center[0] - 105)/40
                ytext = (center[1] - 210)/50
                if int(xtext)+0.75 > xtext and int(ytext) + 0.6 > ytext:
                    c = KEYBOARD[int(ytext)][int(xtext)]
                else:
                    v = None
                    c = None

                if c == "\b" and c != v:
                    reader = reader[:-1]
                    f = open("ocv writer.txt", 'w')
                    f.write(reader)
                    f.close()
                
                f = open("ocv writer.txt", 'a')
                if c != v and c != "\b":  
                    f.write(c)
                elif c == "\b":
                    v = c
                
                f.close()
                if v != c and c != "\b":
                    f = open("ocv writer.txt", 'r')
                    reader = f.read()
                    f.close()
                    v = c
                    
                

            else:
                v = None
        else:
            v = None 
        cv2.putText(frame, reader, (110, 180), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0,0,0), 2) 

        if center is not(None):
            if 200<=center[0]<=400 and 450<=center[1]<=480:     
                KEY = False
                LOC1 =True

def locat1():
    global LOC1
    global LOC2
    global loc1
    if LOC1 is True:
        if center is not(None):
                loc1 = center[:2]
                
        elif loc1 is not(None) and center is None:
            LOC1 = False
            LOC2 = True
            return loc1 
    pass

def locat2():
    global LOC2
    global STOP
    global loc1
    global text
    global reader
    global a
    if LOC2 is True:
        f = frame.copy()
        cv2.circle(frame, loc1, 3, (255,255,255), -1)
        if center is  not(None):
            if loc1[1] >= center[1]:
                if loc1[0]<center[0]:
                    font = (loc1[1] - center[1])/13.7
                    cv2.putText(f, reader, loc1, cv2.FONT_HERSHEY_COMPLEX, font, (255,255,255), 1 )
                    a = [loc1,font, colors[center[3]], center[2]]
                else:
                    font = (loc1[0] - center[0])/(20*len(reader))
                    cv2.putText(f,reader, (center[0], loc1[1]), cv2.FONT_HERSHEY_COMPLEX, font, (255,255,255), 1 )
                    a = [(center[0], loc1[1]),font, colors[center[3]], center[2]]
            else:
                if loc1[0]<center[0]:
                    font = (loc1[0] - center[0])/(20*len(reader))
                    cv2.putText(f,reader[::-1], (center[0], loc1[1]), cv2.FONT_HERSHEY_COMPLEX, font, (255,255,255), 1 )
                    a = [(center[0], loc1[1]),font, colors[center[3]], center[2]]
                else:
                    font = (loc1[1] - center[1])/13.7
                    cv2.putText(f, reader, loc1, cv2.FONT_HERSHEY_COMPLEX, font, (255,255,255), 1 )
                    a = [loc1,font, colors[center[3]], center[2]]
        elif  a != [] and center is None: 
            print(a)
            cv2.putText(frame, reader,a[0] ,cv2.FONT_HERSHEY_COMPLEX,a[1], a[2], a[3])
            text.append([reader, a[0],a[1], a[2], a[3]])
            LOC2 = False
            STOP = False
            a = []
            loc1 = None
            reader = None
            os.remove("C:/Users/suyash/Desktop/KACHRA/laohub/ocv writer.txt")
            
        cv2.imshow("Tracking", f)



# ALL the variables useed in this program 
# If you are a friend and want to help me please remove useless variale
KEY = False
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
FONT = False
LOC1 = False
LOC2 = False
text = []
a = []
# R.I.P. 

c = 0
shape = []
colsize = 2
blank = np.zeros((480,640,3))
v = None


# def write(frame):
#     f = open("Text file.txt", 'a')
#     c = input()
#     if c != None:
#         f.write(c)
#         f.close()
#     f = open("Text file.txt", 'r')
#     reader = f.read()
#     f.close()
#     return reader

#     pass
"""
NOTE :-
Note from here all the commands are looped so please avoid unnecessary command as it will decrease the FPS

Use more effectent method like start replacing list with array and reduce variables

All the code above this are the functions used in the program and their are variables used in the program

Please dont get confused in the shape drawing function smart, rect and draw all these functions are linked with 
each other
"""

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
    frame = cv2.rectangle(frame, (40,450),(135,480), colors[5], -1 )
  
    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Colour", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Size", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Exit", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Save", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
    cv2.putText(frame, "Shape", (520,468), cv2.FONT_HERSHEY_COMPLEX, 0.4, colors[4], 1, cv2.LINE_AA)
    cv2.putText(frame, "FBoard", (55,468), cv2.FONT_HERSHEY_COMPLEX, 0.4, colors[4], 1, cv2.LINE_AA)

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
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']),colsize, colorIndex)

        
        # Now checking if the user wants to click on any button above the screen 
        if center[1] <= 65:
            if 40 <= center[0] <= 140 and SAVE is False: # Clear Button
                bpoints = [deque(maxlen=4096)]

                blue_index = 0
                shape = []
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

            elif 40 <= center[0] <= 135:
                KEY = True
                STOP = True

        elif (COLIST == False and COSIZE == False) and (SAVE == False and STOP == False):
            bpoints[blue_index].appendleft(center)
            # elif colorIndex == 1:
            #     gpoints[green_index].appendleft(center)
            # elif colorIndex == 2:
            #     rpoints[red_index].appendleft(center)
            # elif colorIndex == 3:
            #     ypoints[yellow_index].appendleft(center)
            # elif colorIndex == 4:
            #     spoints[sky_index].appendleft(center)
            # elif colorIndex == 5:
            #     ppoints[pink_index].appendleft(center)
            # elif colorIndex == 6:
            #     wpoints[white_index].appendleft(center)
            # elif colorIndex == 7:
            #     npoints[black_index].appendleft(center)
                 
    # Append the next deques when nothing is detected to avois messing up
    else:
        bpoints.append(deque(maxlen=4096))
        #blue_index += 1
        # gpoints.append(deque(maxlen=1024))
        # #green_index += 1
        # rpoints.append(deque(maxlen=1024))
        # #red_index += 1
        # ypoints.append(deque(maxlen=1024))
        # #yellow_index += 1
        # spoints.append(deque(maxlen=1024))
        # #blue_index += 1
        # ppoints.append(deque(maxlen=1024))
        # #green_index += 1
        # wpoints.append(deque(maxlen=1024))
        # #red_index += 1
        # npoints.append(deque(maxlen=1024))
        # #yellow_index += 1

    # Draw lines of all the colors on the canvas and frame 
    points = [bpoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                x1,y1 = points[i][j][k - 1][:2]
                x2,y2 = points[i][j][k][:2]
                xp = x2 - x1
                yp = y2 - y1
                dist = m.sqrt((xp*xp) + (yp*yp))
                if dist <= 75:
                    cv2.line(frame, points[i][j][k - 1][:2], points[i][j][k][:2], colors[points[i][j][k-1][-1]], points[i][j][k][-2])
                    cv2.line(blank, points[i][j][k - 1][:2], points[i][j][k][:2], colors[points[i][j][k-1][-1]], points[i][j][k][-2])
                else:
                    cv2.circle(frame, points[i][j][k - 1][:2], points[i][j][k][-2], colors[points[i][j][k-1][-1]], -1)
                    cv2.circle(blank, points[i][j][k - 1][:2], points[i][j][k][-2], colors[points[i][j][k-1][-1]], -1)
                col = colors[points[i][j][k][-1]]
                
    for x in shape:
        if x[-1] == "rectangle":
            cv2.rectangle(frame, (x[0],x[1]),(x[2],x[3]), x[5], x[4])
            
        elif x[-1] == "circle":
            radx = x[2] - x[0]
            rady = x[3] - x[1]
            rad = int(m.sqrt((radx*radx) + (rady*rady)))
            cv2.circle(frame, (x[0], x[1]),rad, x[5], x[4])

    for x in text:
        cv2.putText(frame, x[0], x[1], cv2.FONT_HERSHEY_COMPLEX, x[2], x[3], x[4])

    if SAVE is False:
        simg = frame.copy()

    colorlist(frame, center)
    colorsize(frame, center)
    save(frame, center)
    keyboard()
    locat1()
    locat2()

    var = smart(frame, center)
    if var != None:
        v = var[0]
        s = var[1]
    if center != None:
        cv2.circle(frame, (center[0], center[1]), 3, (120, 255, 255), 2)
    
    # Show all the windows
    if RECT is False and LOC2 is False:
        cv2.imshow("Tracking", frame)
    elif LOC2 is True and RECT is False:
        pass
    else:
        rect(frame, center, v)
        if DRAW is True and v != None:
            #print(center[2])
            shape.append([xrect, yrect, xmax, ymax,s, colors[colorIndex], v]) 
            col = colors[0]
        draw()
    
    cv2.imshow("blank", blank)
    cv2.imshow("mask",Mask)
    
    # If the 'q' key is pressed then stop the application 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
if os.path.isfile("C:/Users/suyash/Desktop/KACHRA/laohub/ocv writer.txt") is True:
    os.remove("C:/Users/suyash/Desktop/KACHRA/laohub/ocv writer.txt")
# Release the camera and all resources
cap.release()
cv2.destroyAllWindows()