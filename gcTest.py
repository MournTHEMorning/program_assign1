"""Game Condition Test: gcTest. This is to test out, specifically, scoring system in game. Will delete later. Most is copied from Game.py"""

import random

#so short: don't do list. make a variable in rouge and scout to count for points..
#Way 1: Variable in each Rouge or Scout role [recommended]
#Way 2: have game logic carry the score. [sounds easier, but was not recommended]

#Testing way 2
#7+ to win: Condition

global score
score=0

class game:
        #dice
    def dice(self,rollInput):
        if(rollInput=="R"):
            player_roll=random.randint(1,12)
            return player_roll
        else:
            return None

#partner bonus method
    def traitBonus(self,diceValue,traitValue):
        result=diceValue+traitValue
        return result
      
#point system for win/loss, from above
    def winLoss(self, diceNBonus):
        if(diceNBonus<=3):
            winOrLoss=0
        elif(4<=diceNBonus<=6):
            winOrLoss=1
        elif(7<=diceNBonus<=11):
            winOrLoss=2
        elif(diceNBonus>=12):
            winOrLoss=3
            score+=winOrLoss
            return winOrLoss
    
    #looking at score to see if player won or lost the whole game
    def assessScore():
        print(score)