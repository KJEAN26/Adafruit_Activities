from microbit import *
from time import sleep

counter=0

while True:
    for counter in range(0,5): # accessing the y-axis
        for num in range (0,5):  #accessing the x-axis
            display.set_pixel(num,counter,9) 
            sleep(0.5)
            display.set_pixel(num,counter,0)
    counter+=1  #iteration
    