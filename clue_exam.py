from adafruit_clue import clue
from adafruit_clue import time

clue_display = clue.simple_text_display(title="", title_scale=2,text_scale=1,title_color=(255,0,0))

msg1="This is a message ."

while True:
    
    clue_display[4].text = msg1
    clue_display[4].color= clue.CYAN
    clue_display[4].scale=2
    clue_display.show()
    
    time.sleep(1)
    clue_display[4].color=clue.BLACK  
    clue_display.show()
    
    removedFirstLetter= msg1[0:1]
    msg1= msg1[1: ] + removedFirstLetter
      

  

    

