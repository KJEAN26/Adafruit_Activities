#

from microbit import *
from time import sleep

# pixel = "00000:00000:00000:00000:00000"
# pixelList = list(pixel)
counter=0

while True:
    if counter < 5:
        for num in range (0,5):
            display.set_pixel(num,counter,9) 
            sleep(0.5)
            display.set_pixel(num,counter,0)

    counter+=1    
    # counter = 0 if counter > 28 else counter       
    # if pixel[counter] != ":":
    #     pixelList[counter] = "9"
    #     display.show(Image("".join(map(str,pixelList))))
    #     pixelList[counter] = "0"
    #     sleep(0.5)

    # counter+= 1 
            



