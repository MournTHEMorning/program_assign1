"""ROLE 1 module: ROUGE- THE ARISTOCRAT. This file contains variables and related methods."""
class rouge():
    #variables/attributes
    def __init__(self):
        self.isRouge=False
        self.INTEL = 0
        self.SOC=1
        self.PRI=-2
        self.DAN=2

    #Getter methods
    def getRoleStatus(self):
        return self.isRouge
    
    def getINT(self):
        return self.INTEL

    def getSOC(self):
        return self.SOC
    
    def getPRI(self):
        return self.PRI
    
    def getSpecial(self):
        return self.DAN

    #Setter method, makes variable True for App.py to establish role is activated
    def selectRouge(self,choice):
        if(choice=="Y"):
            self.isRouge=True
        #When the player replays the game    
        else:
            self.isRouge=False