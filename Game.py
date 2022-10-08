"""GAME LOGIC. This connects to all files (Rouge.py and Scout.py, App.py uses the file) 
This uses all variables, methods, and classes related """
import random, Rouge, Scout, colorama
rMod=Rouge.rouge()
sMod=Scout.scout()
from colorama import Fore


class game():
    global score
    score=[]

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
      score=[].append(result)
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
      #you'll have to check this later :) when the game is done
      score.append(winOrLoss)
      return winOrLoss
    
    #looking at score to see if player won or lost the whole game
    def assessScore(self):
      for i in range(len(score)):
        print(score[i])
  
    def RougeAccess(self):
        return rMod

    def ScoutAccess(self):
      return sMod