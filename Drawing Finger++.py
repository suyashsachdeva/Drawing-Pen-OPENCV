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
"""
# Creating the trackbars needed for adjusting the marker colour
cv2.namedWindow("Color detectors")
cv2.createTrackbar("Upper Hue", "Color detectors", 153, 180,setValues)
cv2.createTrackbar("Upper Saturation", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Upper Value", "Color detectors", 255, 255,setValues)
cv2.createTrackbar("Lower Hue", "Color detectors", 64, 180,setValues)
cv2.createTrackbar("Lower Saturation", "Color detectors", 72, 255,setValues)
cv2.createTrackbar("Lower Value", "Color detectors", 49, 255,setValues)
"""

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

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (0, 255, 255),(255,255,0), (255,0,255), (255,255,255), (0,0,0)]
colorIndex = 0

# Here is code for Canvas setup
paintWindow = np.zeros((471,636,3)) + 255
paintWindow = cv2.rectangle(paintWindow, (40,1), (150,65), (0,0,0), 2)
paintWindow = cv2.rectangle(paintWindow, (150,1), (265,65), colors[0], -1)
paintWindow = cv2.rectangle(paintWindow, (265,1), (380,65), colors[1], -1)
paintWindow = cv2.rectangle(paintWindow, (380,1), (495,65), colors[2], -1)
paintWindow = cv2.rectangle(paintWindow, (495,1), (600,65), colors[3], -1)

cv2.putText(paintWindow, "CLEAR", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "BLUE", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "GREEN", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "RED", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
cv2.putText(paintWindow, "YELLOW", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)
cv2.namedWindow('Paint', cv2.WINDOW_AUTOSIZE)
    
def colorlist(frame, cen):
    global COLIST
    global colorIndex
    global colors
    STRING = ["Blue","Green","Red","Yellow","Sky","Pink","White","Black"]
    if COLIST is True and SAVE is False:
        frame = cv2.rectangle(frame, (160,65), (255,305), (0,0,0),2)
        
        
        # frame = cv2.rectangle(frame, (160,97), (255, 123), (0,0,255), -1)
        # frame = cv2.rectangle(frame, (160,127), (255, 153), (0,255,0), -1)
        # frame = cv2.rectangle(frame, (162,157), (253,183), (0,255,255), -1)
        # frame = cv2.rectangle(frame, (160,187), (255, 213), (255,255,0), -1)
        # frame = cv2.rectangle(frame, (160,217), (255, 243), (255,0,255), -1)
        # frame = cv2.rectangle(frame, (160,247), (255, 273), (255,255,255), -1)
        # frame = cv2.rectangle(frame, (160,277), (255, 303), (0,0,0), -1)

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
            
        # else : 
        #     COLIST = False

def colorsize(frame, cen):
    global COSIZE
    global colsize
    if COSIZE is True and SAVE is False:
        frame = cv2.rectangle(frame, (275,65), (370,215), (0,0,0),2)
        frame = cv2.line(frame, (275,95), (370,95), (0,0,0), 2)
        frame = cv2.line(frame, (275,125), (370,125), (0,0,0), 2)
        frame = cv2.line(frame, (275,155), (370,155), (0,0,0), 2)
        frame = cv2.line(frame, (275,185), (370,185), (0,0,0), 2)

        frame = cv2.rectangle(frame, (277,67), (368,93), (0,0,0), -1)
        frame = cv2.rectangle(frame, (277,97), (368, 123), (255,255,255), -1)
        frame = cv2.rectangle(frame, (277,127), (368,153), (0,0,0), -1)
        frame = cv2.rectangle(frame, (277,157), (368, 183), (255,255,255), -1)
        frame = cv2.rectangle(frame, (277,187), (368, 213), (0,0,0), -1)

        cv2.putText(frame, "1 px", (310, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "2 px", (310,110), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "3 px", (310, 140), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, "4 px", (310,170), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, "5 px", (310,200), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        
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
    if not(cen is None) and SAVE is True:
        if 220 <= cen[0] <= 280 and 260 <= cen[1] <= 300:
            cv2.imwrite("opencv finger.png", simg)
            OLD = r"C:\Users\suyash\Desktop\KACHRA\laohub\opencv finger.png"
            NEW = r"C:\Users\suyash\Desktop\Delete Me\opencv finger.png"
            OLD = OLD.replace("\\","/")
            NEW = NEW.replace("\\","/")
            os.rename(OLD, NEW)
            SAVE = False
            
        if 360 <= cen[0] <= 420 and 260 <= cen[1] <= 300:
            SAVE = False


# Loading the default webcam of PC.
cap = cv2.VideoCapture(0)

COLIST = False
COSIZE = False
SAVE = False
colsize = 2

# Keep looping
while True:
    # Reading the frame from the camera
    ret, frame = cap.read()
    #Flipping the frame to see same side of yours
    frame = cv2.flip(frame, 1)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    u_hue = cv2.getTrackbarPos("Upper Hue", "Color detectors")
    u_saturation = cv2.getTrackbarPos("Upper Saturation", "Color detectors")
    u_value = cv2.getTrackbarPos("Upper Value", "Color detectors")
    l_hue = cv2.getTrackbarPos("Lower Hue", "Color detectors")
    l_saturation = cv2.getTrackbarPos("Lower Saturation", "Color detectors")
    l_value = cv2.getTrackbarPos("Lower Value", "Color detectors")
    Upper_hsv = np.array([u_hue,u_saturation,u_value])
    Lower_hsv = np.array([l_hue,l_saturation,l_value])
    

    # Adding the colour buttons to the live frame for colour access
    frame = cv2.rectangle(frame, (40,1), (140,65), (122,122,122), -1)
    frame = cv2.rectangle(frame, (160,1), (255,65), colors[0], -1)
    frame = cv2.rectangle(frame, (275,1), (370,65), colors[1], -1)
    frame = cv2.rectangle(frame, (390,1), (485,65), colors[2], -1)
    frame = cv2.rectangle(frame, (505,1), (600,65), colors[3], -1)
  
    cv2.putText(frame, "CLEAR ALL", (49, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Colour", (185, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Size", (298, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Exit", (420, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.putText(frame, "Save", (520, 33), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (150,150,150), 2, cv2.LINE_AA)


    # Identifying the pointer by making its mask
    Mask = cv2.inRange(hsv, (100,100,100), (150,255,255))
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
        # Draw the circle around the contour
        cv2.circle(frame, (int(x), int(y)), 3, (120, 255, 255), 2)
        # Calculating the center of the detected contour
        M = cv2.moments(cnt)
        center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00']),colsize)

        # Now checking if the user wants to click on any button above the screen 
        if center[1] <= 65:
            if 40 <= center[0] <= 140 and SAVE is False: # Clear Button
                bpoints = [deque(maxlen=512)]
                gpoints = [deque(maxlen=512)]
                rpoints = [deque(maxlen=512)]
                ypoints = [deque(maxlen=512)]
                spoints = [deque(maxlen=512)]
                ppoints = [deque(maxlen=512)]
                wpoints = [deque(maxlen=512)]
                npoints = [deque(maxlen=512)]

                blue_index = 0
                green_index = 0
                red_index = 0
                yellow_index = 0
                sky_index = 0
                pink_index = 0
                white_index = 0
                black_index = 0


                paintWindow[:,:,:] = 255
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
                
        elif (COLIST == False and COSIZE == False) and SAVE == False:
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
        bpoints.append(deque(maxlen=512))
        #blue_index += 1
        gpoints.append(deque(maxlen=512))
        #green_index += 1
        rpoints.append(deque(maxlen=512))
        #red_index += 1
        ypoints.append(deque(maxlen=512))
        #yellow_index += 1
        spoints.append(deque(maxlen=512))
        #blue_index += 1
        ppoints.append(deque(maxlen=512))
        #green_index += 1
        wpoints.append(deque(maxlen=512))
        #red_index += 1
        npoints.append(deque(maxlen=512))
        #yellow_index += 1

    # Draw lines of all the colors on the canvas and frame 
    points = [bpoints, gpoints, rpoints, ypoints, spoints, ppoints, wpoints, npoints]
    for i in range(len(points)):
        for j in range(len(points[i])):
            for k in range(1, len(points[i][j])):
                if points[i][j][k - 1] is None or points[i][j][k] is None:
                    continue
                cv2.line(frame, points[i][j][k - 1][:2], points[i][j][k][:2], colors[i], points[i][j][k][-1])
                cv2.line(paintWindow, points[i][j][k - 1][:2], points[i][j][k][:2], colors[i], points[i][j][k][-1])
    if SAVE is False:
        simg = frame.copy()
    colorlist(frame, center)
    colorsize(frame, center)
    save(frame, center)
    # Show all the windows
    cv2.imshow("Tracking", frame)
    cv2.imshow("Paint", paintWindow)
    cv2.imshow("mask",Mask)

	# If the 'q' key is pressed then stop the application 
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and all resources
cap.release()
cv2.destroyAllWindows()