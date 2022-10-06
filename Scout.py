"""ROLE 2: SCOUT- THE HACKER. This file contains variables and related methods."""
class scout():
    def __init__(self):
        self.isScout=False
        self.name="SCOUT"
        self.INTEL = 1
        self.PHY=0
        self.SOC=-2
        self.PRI=1
        self.HACK=2

    #Getter methods
    def getName(self):
        return self.name
    
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

    #Setter methods
    def selectScout(self):
        self.isScout=True
        print(self.isScout)