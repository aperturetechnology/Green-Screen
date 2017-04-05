# ## Problem 3:  green-screening!
# 
# This code will take in two images, and will create a overlap between the two images, creating a green screen effect
#


import numpy as np
from matplotlib import pyplot as plt
import cv2


# Here is a signature for the green-screening...
# remember - you will want helper functions!
def get_green(orig_image):
    """
    Tovisualize what we should set 
    """
    raw_image = cv2.imread(orig_image,cv2.IMREAD_COLOR)
    image = raw_image.copy()
    num_rows, num_cols, num_chans = image.shape
    list_string = []
    
    for row in range(num_rows):
        for col in range(num_cols):
            r, g, b = image[row,col]
            list_string.append([r, g, b])
    d = {}
    for i in range(len(list_string)):
        if list_string[i] in list_string[i:]:
            d[str(list_string[i][0])] += 1
        else:
            d[str(list_string[i][0])] = 1
            
    
    
    max_num = max(d.values())

    for x in d:
        if d[x] == max_num:
            return x
        

def isGreen( r, g, b ):
    """
    Tests if a color is green based on the rgb values
    """
    if g > 100 and r < 150 and b < 150:
        return True
    else:
        return False 
        

def green_screen( orig_image_name, new_bg_image_name, corner=(0,0) ):
    """ 
    orig_image = the green screen image
    new_big_image = the background image
    this will take the green screen image, and put the green screen image person/item in the background
    """

    #if not green, should add it on top of the function
    green = [67,150,4]

    # read in other image
    raw1_image = cv2.imread(orig_image_name,cv2.IMREAD_COLOR)
    raw1_image = cv2.cvtColor(raw1_image,cv2.COLOR_BGR2RGB)
    orig_image = raw1_image.copy()


    raw_image = cv2.imread(new_bg_image_name,cv2.IMREAD_COLOR)
    raw_image = cv2.cvtColor(raw_image,cv2.COLOR_BGR2RGB)
    new_image = raw_image.copy()

    num1_rows, num1_cols, num1_chans = orig_image.shape
    num2_rows, num2_cols, num2_chans = new_image.shape

    min_num_rows = min(num1_rows, num2_rows)
    min_num_cols = min(num1_cols, num2_cols)

    for row in range(num2_rows):
        for col in range(num2_cols):
            orig_row = row - corner[0]
            orig_col = col - corner[1]

            if 0 <= orig_row < num1_rows and 0 <= orig_col < num1_cols:
                r1, g1, b1 = orig_image[orig_row,orig_col]

                if isGreen( r1, g1, b1 ) == True:
                    new_image[row][col]  = new_image[row][col]
                else:
                    new_image[row, col] = [r1, g1, b1]
    
    return new_image
                
i2 = green_screen('green.png', 'rushmore.jpg')
plt.imshow( i2 )
plt.show()

