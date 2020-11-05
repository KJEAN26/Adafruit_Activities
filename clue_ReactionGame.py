import random
from adafruit_clue import clue
from adafruit_clue import time
from time import sleep

counter=4
clue_display = clue.simple_text_display(title="REACTION GAME", title_scale=2,text_scale=1,title_color=(255,255,0))
player1=0
player2=0
score=5

while True:
   clue_display[2].text = "Instructions:"
   clue_display[2].color= clue.GREEN
   clue_display[2].scale=2
   clue_display[4].text = "PLayer A presses A"
   clue_display[4].color= clue.WHITE
   clue_display[4].scale=2
   clue_display[6].text = "PLayer B presses B"
   clue_display[6].color= clue.WHITE
   clue_display[6].scale=2
   clue_display[8].text = "Press is the number "
   clue_display[8].color= clue.SKY
   clue_display[8].scale=2
   clue_display[10].text = "is divisible by 2"
   clue_display[10].color= clue.SKY
   clue_display[10].scale=2
   clue_display[12].text = "Maximum Score of 5"
   clue_display[12].color= clue.YELLOW
   clue_display[12].scale=2

   counter=counter-1
   time.sleep(1)
   clue_display[14].text = "Starts in " + str (counter)
   time.sleep(0.5)
   clue_display[14].color= clue.RED
   clue_display[14].scale=2
   clue_display.show()

   if counter==1:
    while True:
        clue_display[2].text = ""
        clue_display[4].text = ""
        clue_display[6].text = ""
        clue_display[8].text = ""
        clue_display[10].text = ""
        clue_display[12].text = ""
        clue_display[14].text = ""
   
        
        clue_display[13].text = "Player A Score:" + str (player1)
        clue_display[13].color= clue.GREEN
        clue_display[13].scale=2
        
        clue_display[15].text = "Player B Score:"+ str (player2)
        clue_display[15].color= clue.SKY
        clue_display[15].scale=2
        
        
        clue_display[5].scale=2
        number=random.randint(0,100)
        clue_display[5].text= f'         {(number)}'
 
        
        counters=1
        measure1 = time.time()
        measure2 = time.time()
        while counters > 0:
            if measure2 - measure1 >= 1:
                counters = 0
                break
            else:
                measure2 = time.time()
                
            if clue.button_a:
                if number % 2==0:
                    player1+=1
                else:
                    player1-=1
                break
            
            if clue.button_b:
                if number % 2 ==0:
                    player2+=1
                else:
                    player2-=1
                break

            if player1 > score:
                clue_display[5].text = "PLAYER 1 WINS!" 
                
            if player2 > score:
                clue_display[5].text="PLAYER 2 WINS!"
            

        time.sleep(1)
        clue_display.show()



        


   

    
