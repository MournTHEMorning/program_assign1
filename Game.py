"""GAME LOGIC. This connects to all files (Rouge.py and Scout.py, App.py uses the file) 
This uses all variables, methods, and classes related """

import random, Rouge,Scout

rMod=Rouge.rouge()
sMod=Scout.scout()

#7+ to win: Condition

class game:
    def __init__(self):
        self.score=0
        
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
    def winLoss(self,diceNBonus):
        if(diceNBonus<=3):
            winOrLoss=0
        elif(3<diceNBonus<=6):
            winOrLoss=1
        elif(6<diceNBonus<=11):
            winOrLoss=2
        elif(diceNBonus>=12):
            winOrLoss=3
        self.score+=winOrLoss
        return winOrLoss
    
    #looking at score to see if player won or lost the whole game
    def assessScore(self):
        return self.score

    def RougeAccess(self):
        return rMod

    def ScoutAccess(self):
      return sMod

    def resetScore(self):
        self.score=0