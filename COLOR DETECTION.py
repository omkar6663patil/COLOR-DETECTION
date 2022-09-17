#!/usr/bin/env python
# coding: utf-8

# # TSF #GRIPTASK
# #COLOR DETECTION
# #Author: Omkar Patil

# In[17]:


import cv2          #install using pip install opencv-python 
import pandas as pd      #install using pip install pandas
import matplotlib.pyplot as plt


# # image path

# In[27]:


img_path='COLOR IMAGE.jpg'     #array format
img=cv2.imread(img_path)
img=cv2.resize(img,(800,600))    #Resize image
plt.imshow(img)


# # Values of color in open-cv(BGR)

# In[33]:


click = False
r = g = b = x_pos = y_pos = 0
index = ['Color','color_name', 'hex', 'R', 'G', 'B']
df=pd.read_csv('colors.csv',names = index,header = None)
print(df.head(3))
print(len(df))    #total number of row


# # Defining functions to detect color from csv file

# In[35]:


def get_color_name(r,g,b):
    minimum = 10000
    for i in range(len(df)):
        d = abs(r - int(df.loc[i, 'R'])) + abs(g - int(df.loc[i, 'G'])) + abs(b - int(df.loc[i, 'B']))
        if d<= minimum:
            minimum = d
            cname = df.loc[i, 'color_name']
    return cname


# In[34]:


def draw_function(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:                      #in double click on left button it will show cordinates
        global b, g, r, x_pos, y_pos, click
        click = True
        x_pos = x
        y_pos = y
        b, g, r = img [y,x]
        b = int(b)
        g = int(g)
        r = int(r)


# # For execution of image

# In[ ]:


cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)
#cv2.imshow('image',img)
#cv2.waitKey(0)
while True:
    cv2.imshow('image', img)
    if click:
        cv2.rectangle(img, (20,20),(450,60),(b, g, r), -1 )
        character = get_color_name(r, g, b) #+ 'R= ' + str(r) + 'G = ' + str(g) + 'B = ' + str(b)
        cv2.putText(img, character, (50,50), 2, 0.8, (255,255,255), 2 ,cv2.LINE_AA)
        
        if r+g+b >= 600:
            cv2.putText(img, character, (50,50), 2, 0.8, (0,0,0), 2 ,cv2.LINE_AA)
            
        click = False
        
    if cv2.waitKey(2) & 0XFF == 27:
        break
cv2.destroyAllWindows()


# In[ ]:




