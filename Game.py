"""GAME LOGIC. This connects to all files (Rouge.py and Scout.py, App.py uses the file) 
This uses all variables, methods, and classes related """

#random returns random values and comes with Python. This is used for the dice function through method randint()
#Rouge and Scout are imported to allow App.py to access the roles' methods and variables through the one module
import random, Rouge,Scout

#reference variables for Rouge and Scout module for their respective classes
rMod=Rouge.rouge()
sMod=Scout.scout()

class game:
    """variable score: keeps track of "points"  gained through winLoss() class and determines if player won/loss entire game"""
    def __init__(self):
        #self.score is the counter for the player's points, determining if they win or lose the game
        self.score=0
        
    """dice() function: when given a valid input("R") from App.py, will roll and give a random value from 1-12 (inclusive)."""
    def dice(self,rollInput):
        if(rollInput=="R"):
            player_roll=random.randint(1,12)
            return player_roll
        else:
            return None

    """traitBonus() function: adds int variable diceValue-- which is the respective level's dice roll from dice() function--and
                int variable traitValue--which is the respective role attribute for the respective level-- to give App.py the total 'roll' """
    def traitBonus(self,diceValue,traitValue):
        result=diceValue+traitValue
        return result
      
    """winLoss() function: takes value from traitBonus() function from a specific level and 
                        adds the respective amount of points (points depend on what the total "roll" gave as a result(i.e. (crit)win/loss)) 
                        to the score variable"""
    def winLoss(self,diceNBonus):
        if(diceNBonus<=3):
            winOrLoss=0
        elif(3<diceNBonus<=6):
            winOrLoss=1
        elif(6<diceNBonus<=11):
            winOrLoss=2
        elif(diceNBonus>=12):
            winOrLoss=3
        
        #part of function that adds the respective amount of points
        self.score+=winOrLoss
        return winOrLoss
    
    """resetScore() function: resets the score to 0, in the case the player is playing again"""
    def resetScore(self):
        self.score=0

    """assessScore() function: returns the score value"""
    def assessScore(self):
        return self.score

    """RougeAccess() function: returns access to Rouge.py"""
    def RougeAccess(self):
        return rMod

    """ScoutAccess() function: returns access to Scout.py"""
    def ScoutAccess(self):
      return sMod