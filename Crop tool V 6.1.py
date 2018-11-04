# VERSION 6.1
#
# AUTHOR: Suri Bhasker Sri Harsha, MS- Research Scholar, IIT Tirupati

# Description: Version 6.1
#


import cv2
import numpy as np

list1=[]
list2=[]

# MOUSE MOVEMENT TRACKING AND RESPONDING FUNCTION
#
def draw_circle(event,x,y,flags,param):
    global ix,iy
	
    # If left button of the mouse is pressed and mouse is moving, then
    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
	# Append the x cordinate of the mouse location into the first list
        list1.append(x)
	# Append the y cordinate of the mouse location into the second list
        list2.append(y)
	# we are drawing a small circle in the area so that the user can see his track.
        cv2.circle(img,(x,y), 1, (255,255,255), -1)
        
    # IF the user lets go off the left button
    elif event == cv2.EVENT_LBUTTONUP:
        global a,b
        print ("Max of x list is "+str(max(list1)))
        print ("Max of y list is "+str(max(list2)))
        print ("Min of x list is "+str(min(list1)))
        print ("Min of y list is "+str(min(list2)))
	# Find the minimum of the elements from list 1 and list 2
        ix=min(list1)
        iy=min(list2);
	# Find the maximum of the elements from list 1 and list 2
        x=max(list1);
        y=max(list2);
        a,b=x,y
        print(list1)
        print(list2)



#IMAGE CREATION FUNCTION
img = cv2.imread("/home/bhasker/Desktop/t.jpg",1)
cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_circle)



#KEYSTROKE RECOGNITION AND RESPONDING FUNCTION
#
# The following code is responsible for capturing the keystrokes of the user. If the user hits "ESC" the loop breaks, if the user hits "c"
# the selected image is cropped.
while(1):
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF

    # IF user hits "ESC" break out of the loop
    if k == 27:
        break

    # If user hits "c" , then 
    elif k == ord('c'):
        print("Values of ix, iy and a,b are:")
        print(ix,iy,a,b)
        img2 = cv2.imread("/home/bhasker/Desktop/t.jpg",1)
	#Crop the image using the coordinates that we captured in the draw_circle function
        crop_img = img2[iy:b,ix:a]
        crop_img = cv2.resize(crop_img,(50,50))
	# Ask the user for annotations (i.e. name of the character that he/she just cropped)
        annotate = raw_input("Enter the annotation: ")
	# Now save the cropped portion of image in a folder using the annotation as image's name.
        cv2.imwrite("/home/bhasker/Desktop/Database/"+str(annotate)+".jpg",crop_img) 
	# Display the cropped image in a saperate window.
        cv2.imshow('Cropped image',crop_img)
        list1=[]
        list2=[]

cv2.destroyAllWindows()
