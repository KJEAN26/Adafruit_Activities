from microbit import *
from time import sleep


pixelPattern = [
                [0,0],[1,0],[2,0],[3,0],[4,0],
                [4,1],[4,2],[4,3],[4,4],[3,4],
                [2,4],[1,4],[0,4],[0,3],[0,2],
                [0,1],[1,1],[2,1],[3,1],[3,2],
                [3,3],[2,3],[1,3],[1,2],[2,2]
                ]
while True:
    for i in range(0,len(pixelPattern)):
        display.set_pixel(pixelPattern[i][0],pixelPattern[i][1],9)
        sleep(0.5)
        display.set_pixel(pixelPattern[i][0],pixelPattern[i][1],0)
    