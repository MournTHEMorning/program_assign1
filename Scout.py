"""ROLE 2 module: SCOUT- THE HACKER. This file contains variables and related methods."""
class scout():
    #variables/attributes
    def __init__(self):
        self.isScout=False
        self.INTEL = 1
        self.PHY=0
        self.SOC=-2
        self.PRI=1
        self.HACK=2

    #Getter methods
    def getRoleStatus(self):
        return self.isScout
    
    def getINT(self):
        return self.INTEL
    
    def getPHY(self):
        return self.PHY

    def getSOC(self):
        return self.SOC
    
    def getPRI(self):
        return self.PRI
    
    def getSpecial(self):
        return self.HACK

    #Setter method, makes variable True for App.py to establish role is activated
    def selectScout(self, choice):
        if(choice=="Y"):
            self.isScout=True
        #When the player replays the game    
        else:
            self.isScout=False