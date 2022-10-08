"""ROLE 1: ROUGE- THE FREE SPIRIT. This file contains variables and related methods."""
class rouge():
    def __init__(self):
        self.isRouge=False
        self.name="ROUGE"
        self.INTEL = 0
        self.PHY=1
        self.SOC=1
        self.PRI=-2
        self.DAN=2

    #Getter methods
    def getName(self):
        return self.name
    
    def getRoleStatus(self):
        return self.isRouge
    
    def getINT(self):
        return self.INTEL
    
    def getPHY(self):
        return self.PHY

    def getSOC(self):
        return self.SOC
    
    def getPRI(self):
        return self.PRI
    
    def getSpecial(self):
        return self.DAN

    #Setter methods
    def selectRouge(self,choice):
        if(choice=="Y"):
            self.isRouge=True
        else:
            self.isRouge=False