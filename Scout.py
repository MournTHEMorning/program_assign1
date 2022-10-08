"""ROLE 2 module: SCOUT- THE HACKER. This file contains variables and related methods."""
class scout():
    """initalizing variables/attributes"""
    def __init__(self):
        #self.isScout defines if Scout character is activated
        self.isScout=False
        #Scout's Intel skill
        self.INTEL = 1
        #Scout's physical skill
        self.PHY=0
        #Scout's social skill
        self.SOC=-2
        #Scout's speciality skill, which is hacking
        self.HACK=2

    """Getter methods"""
    """getRoleStatus() returns if Scout is activated or not"""
    def getRoleStatus(self):
        return self.isScout
    
    """getINT() returns INT"""
    def getINT(self):
        return self.INTEL
    
    """getPHY() returns PHY"""
    def getPHY(self):
        return self.PHY

    """getSOC() returns SOC"""
    def getSOC(self):
        return self.SOC
    
    """getSpecial() returns speciality, which is hack"""
    def getSpecial(self):
        return self.HACK

    """Setter method, makes variable True for App.py to establish role is activated"""
    def selectScout(self, choice):
        if(choice=="Y"):
            self.isScout=True
        #When the player replays the game    
        else:
            self.isScout=False