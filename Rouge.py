"""ROLE 1 module: ROUGE- THE ARISTOCRAT. This file contains variables and related methods."""
class rouge():
    """initalizing variables/attributes"""
    def __init__(self):
        #self.isRouge defines if Rouge character is activated
        self.isRouge=False
        #Rouge's Intel skill
        self.INTEL = 0
        #Rouge's Social Skill
        self.SOC=1
        #Rouge's Primitive skill
        self.PRI=-2
        #Rouge's Dance skill, speciality skill
        self.DAN=2

    """Getter methods"""
    """getRoleStatus() returns if Rouge is activated or not"""
    def getRoleStatus(self):
        return self.isRouge
    
    """getINT() returns Rouge's INT"""
    def getINT(self):
        return self.INTEL

    """getSOC() returns Rouge's SOC"""
    def getSOC(self):
        return self.SOC
    
    """getPRI() returns Rouge's PRI"""
    def getPRI(self):
        return self.PRI
    
    """getSpecial() returns value of Rouge's speciality, which is DANCE here"""
    def getSpecial(self):
        return self.DAN

    """Setter method, makes variable True for App.py to establish role is activated"""
    def selectRouge(self,choice):
        if(choice=="Y"):
            self.isRouge=True
        #When the player replays the game    
        else:
            self.isRouge=False