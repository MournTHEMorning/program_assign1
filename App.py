"""ALL USER INTERACTIVITY. This connects to all files (Rouge.py and Scout.py, App.py uses the file) 
This uses all variables, methods, and classes related """
from ast import For
import colorama, Game
from colorama import Fore
gMod=Game.game()

line=Fore.RESET+"\n-----*-----\n"
breakLine=Fore.RESET+"\n============~*~============\n"
leaveGame=False

#fore.cyan for scout
#fore.red for rouge

#menu
#https://patorjk.com/software/taag/#p=display&f=Line%20Blocks&t=Treasure
print(Fore.YELLOW+"""_______  ______   ______  ______   ______   _    _   ______   ______ 
  | |   | |  | \ | |     | |  | | / |      | |  | | | |  | \ | |     
  | |   | |__| | | |---- | |__| | '------. | |  | | | |__| | | |---- 
  |_|   |_|  \_\ |_|____ |_|  |_|  ____|_/ \_|__|_| |_|  \_\ |_|____ """)
print("\n                       [TREASURE]")

#USED TO TEST GAME WITHOUT MENU
menuAns="S"

while(leaveGame==False):
    print(Fore.RESET+"\n\nSTART"+Fore.GREEN+" [S]"+Fore.WHITE+"\nHOW TO PLAY"+Fore.GREEN+" [H]"+Fore.WHITE+"\nPARTNERS: BIO"+Fore.GREEN+" [P]"+Fore.WHITE+"\nEXIT GAME"+Fore.GREEN+" [E]")
    #menuAns = input(Fore.GREEN+"**PLEASE TYPE HERE: "+Fore.RESET).upper()
    print(line)

    #start
    if (menuAns=="S"):
        
        verify="N"
        #PLAYER NAME
        while(verify=="N"):
            playerName=input("WHAT IS YOUR NAME?: ").capitalize()
            playerName=(Fore.GREEN+playerName)
            print("Your name is: "+playerName+". Correct?")
            verify  = input(Fore.GREEN+"**TYPE YES[Y] or NO[N]: "+Fore.RESET).upper()
            print(line)
            
        #partner prompt
        roleSelected="N"
        while(roleSelected=="N"):
            print(playerName+", is it? Now, who will be your partner? \n**ONCE YOU SELECT, YOU WILL NOT BE ABLE TO CHANGE PARTNERS")
            print(Fore.RED+"ROUGE: A dramatic but goodhearted explorer!\n		STATS: INT 0 | PHY 1 | SOC 1 | PRI -2 | SPECIALTY: DANCE")
            print(Fore.CYAN+"\nSCOUT: A cold but passionate explorer!\n 		STATS: INT 1 | PHY 0 | SOC -2 | PRI 1 | SPECIALTY: HACK")
            roleSelected=input(Fore.GREEN+"WHO SHALL JOIN YOU? [Type their FULL NAME]: "+Fore.RESET).upper()
            if(roleSelected=="ROUGE" or roleSelected=="SCOUT"):
                verify  = input(Fore.GREEN+"**TYPE YES[Y] to confirm: "+Fore.RESET).upper()
                if (verify=="Y"):
                    if(roleSelected=="ROUGE"):
                        gMod.RougeAccess().selectRouge()
                        print(Fore.RED+"\nROUGE: "+playerName+Fore.RED+" is it? I\'m actually quite surprised that I can tag along! It will be my honour to find this cool treasure! \n...What are we waiting for? Let\'s go!")
                    else:
                        gMod.ScoutAccess().selectScout()
                        print(Fore.CYAN+"\nSCOUT: "+playerName+Fore.CYAN+" correct? ...alright. I will meet you there.")
                else:
                    roleSelected="N"

            else:
                print("\nPlease select a proper partner!"+line)
                roleSelected="N"

        input(Fore.GREEN+"Press the ENTER KEY to continue: ")#to skip option for now

        #FORCING PLAYERNAME=TESTER_NAME
        #playerName=Fore.GREEN+"Tester_Name[Please-add-RESET-at-end]"

        #     #FORCING ROUGE AS PARTNER
        # gMod.RougeAccess().selectRouge() 
        # print(gMod.RougeAccess().getRoleStatus())

        #     #FORCING SCOUT AS PARTNER
        # gMod.ScoutAccess().selectScout()
        # print(gMod.ScoutAccess().getRoleStatus())

        #gotta print out treasure after the game end+menu pops up. Add a breakline after the player's role to see stats. Then input statement after the roll, to see results? (skip that for now, but add later)

        #intro
        print(line+Fore.RESET+"Many interviews with surviving explorers, a plane flight, gut-wrenching boat ride, and four hour hike later: Your team finally reached the ruins.\nMarble-coloured spires attempt to hide behind dense foliage of vines, trees, and weeds. \nThe cracked, white tiles once were as pristine of the spires, but one can tell that this was centuries ago.")
        
        #specialized dialogue
        if (gMod.RougeAccess().getRoleStatus()):
            print(Fore.RED+"\nROUGE: Alright! Let\'s get searching!")
        else:
            print(Fore.CYAN+"\nSCOUT is already several feet away, searching for clues...")
        rollAgain=True

        #rolling for lv1
        while(rollAgain):
            rollInput=input(line+Fore.GREEN+"ROLL for INTEL![Input R]: ").upper()
            diceResult=gMod.dice(rollInput)
            rollAgain=False

            #if valid input
            if(type(diceResult)==int):
                print("YOU ROLLED:"+Fore.RESET,diceResult)
            else:
                print("Please roll again!")
                rollAgain=True
        
        #adding bonus
        if(gMod.RougeAccess().getRoleStatus()==True):
            print(Fore.RED+"PARTNER\'S BONUS(INT):"+Fore.RESET, gMod.RougeAccess().getINT())
            bonus=gMod.traitBonus(diceResult,gMod.RougeAccess().getINT())

        elif(gMod.ScoutAccess().getRoleStatus()==True):
            print(Fore.CYAN+"PARTNER\'S BONUS(INT):"+Fore.RESET, gMod.ScoutAccess().getINT())
            bonus=gMod.traitBonus(diceResult,gMod.ScoutAccess().getINT())

        print("YOU AND YOUR PARTNER ROLLED A", bonus)

        #lv1 results
        if(gMod.winLoss(bonus)==0):
            print("You recieved: "+Fore.YELLOW+"a CRIT LOSS(3 and under)!"+line)
            print("Your team scour the grounds for clues. Unfortunately, the long travel has \nmade the team exhausted, not recalling any of the clues... Desperate, you check a familiar vine...\n")
            if(gMod.RougeAccess().getRoleStatus()):
                print("Their open expression says it all."+Fore.RED+"\nROUGE: UGH! When I signed up for this, I didn\'t think they would be so... un-obvious!"+Fore.RESET+" They weakly\nslap the wall in anger, causing you to only sigh and lean on the wall. The ruins seem to tremble.")
            else:
                print("They pace from one end to another, repeating their steps for the tenth time now. You wave them over to brainstorm,\nbut they wave you off and continue mumbling. Exhausted, you march towards them instead. Near SCOUT, you hear a click and the ruins seem to tremble.")
        elif(gMod.winLoss(bonus)==1):
            print("You recieved:"+Fore.YELLOW+"a LOSS(4-6)!"+line)
            print("Your team scour the grounds for clues. The interviews nare hazy, but you both recall the Yushin\'s insignia-- a gold and white \nV-shape, as you recall -- would lead to a contraption.\n")
            if(gMod.RougeAccess().getRoleStatus()):
                print(Fore.RED+"ROUGE: Ugh! Where is that thing?\n"+playerName+": You mean, insignia?\n"+Fore.RED+"ROUGE: Yes! That thing! Where is it??"+Fore.RESET+" This was as convenient as a child asking if they were there yet, you thought. \nThey stepped on a yellow stain-- wait a moment.\n"+playerName+": Wait a moment! The stain on the tiles! Gold and white, leading..."+Fore.RESET+"\nQuickly, they dash off towards a random pile of vines.\n\nYou both looked in the insignia\'s general area for hours. ROUGE shoots you an irritated look."+Fore.RED+"\nROUGE: UGH! When I signed up for this, I didn\'t think they would be so... un-obvious!"+Fore.RESET+" They weakly slap the wall in anger, causing you to only sigh and lean on the wall. The ruins seem to tremble.")
            else:
                print("SCOUT took a snack break, leaving you to continue searching. Looking high and low, you sigh.\n"+Fore.CYAN+"SCOUT: Anything? "+Fore.RESET+"You shake your head, as SCOUT walks ahead. They stepped on a yellow stain-- wait a moment.\n"+playerName+": Wait! The stain on the tiles! Gold and white, like-- "+Fore.RESET+"However, SCOUT has already left, already cluing in. \n\nYou both looked in the insignia\'s general area for hours, but no leads. SCOUT paces from one end to another, repeating their steps for the ninth time now.\nIn the middle of their tenth pace, they jog over to a familiar wall. Curious, you follow, as the ruins seem to tremble.") 
        elif(gMod.winLoss(bonus)==2):
            print("You recieved: "+Fore.YELLOW+"a WIN(7-11)!"+line)
            print("Your team scour the grounds for clues. Fortunately, you \nboth recall the Yushin\'s insignia-- a gold and white Y-like shape. \nThe contraption would be to the Northern side of the insignia. \n")
            if(gMod.RougeAccess().getRoleStatus()):
                print(Fore.RED+"ROUGE: The insignia must be North, right? "+Fore.RESET+"They rush ahead and begin climbing the ruins, walking on some yellow-stained \ntiles in the process. Wondering if it is a trick of the light, you call to ROUGE.\n"+playerName+": ROUGE! Does this look like the insignia? "+Fore.RESET+"You jump on the golden tiles. ROUGE responds with a loud \'Wa-hoo!\'\nWith everything going to plan, you head Northbound from the insignia. Every wall looks similar, but there is a slight \nshine of gold underneath some of the greenery. With hesitance, you begin leaning into the tile, before ROUGE \ncrashes into you."+Fore.RED+"\nROUGE: What are we looking-- "+Fore.RESET+" The ruins seem to tremble.")
            else:
                print("SCOUT took a snack break and a nap to recharge from the long journey.\n"+playerName+": I suppose I do this alone... "+Fore.RESET+"You sigh, as you begin with the lower level. No sign. \nClimbing up the vines, you notice a faded, golden Y-like shape. Down below, you see SCOUT near the insignia. \nBy the time you climb down, they have marched to the right side of the ruins.\n"+playerName+": Hey! I found the-- "+Fore.RESET+"Near SCOUT, you hear a click and the ruins seem to tremble.")
        elif(gMod.winLoss(bonus)==3):
            print("You recieved: "+Fore.YELLOW+"a CRIT WIN(12 and above)!"+line)
            print("Your team scour the grounds for clues. According to the surviving adventurers, \nthe Yushin\'s insignia is a gold and white Y-like shape. The contraption is to the North of the insignia.\n")
            if(gMod.RougeAccess().getRoleStatus()):
                print(Fore.RED+"ROUGE: Now where is that insignia..."+Fore.RESET+"You spot some faded, golden tiles.\n"+playerName+": Would that be it? "+Fore.RESET+"ROUGE responds with a loud \'Wa-hoo!\'With everything going to plan, you head Northbound from the insignia. Every wall \nlooks similar, but there is a slight shine of gold underneath some of the greenery.\n"+Fore.RED+"ROUGE: That's gotta be it! ...race you? "+Fore.RESET+"You two race over to the golden tile. Unfortunately, they won, but you worry more over the trembling ruins.")
            else:
                print("You begin climbing the vines surrounding the ruins, searching for the golden tiles You breathe in the sight. The Yushin themselves stood \nhere many centuries ago!\n"+playerName+": How amazing...  oh? "+Fore.RESET+"By the time you climb down, SCOUT finishes their snack break.\n"+playerName+": Hey! I found the tiles!"+Fore.RESET+" SCOUT raises their eyebrows.\n"+Fore.CYAN+"SCOUT: Really? ...great! "+Fore.RESET+"You lead them, stomping harshly on the golden hue. They take their compass, pointing North. Within a short walk, there is a \nslight shine of gold underneath the greenery. Filled with excitement, you rush over. You push the tile, as you see... a smile(?) and feel a rumble.")

        input("PRESS ENTER TO CONTINUE TESTING, DEV!")

    #how to
    elif (menuAns=="H"):
        print(Fore.YELLOW+"\'Within the Yushin empire, there rests a treasure within the \'wealth of shining power / you may change the paths of rivers\'\'\n")
        print(Fore.RESET+"WELCOME TO TREASURE! You play as a museum\'s lead researcher of Yushin-- an advanced civilization that\naided ancient Rome to Babylon. Hearing a rumour about an unknown artifact, you and your fellow treasure-hunter discover some ruins...")
        print(Fore.GREEN+"\nHOW TO PLAY:\n1) PICK A PARTNER:"+Fore.RESET+" You will require assistance on your journey. Will you pick"+Fore.RED+" ROUGE --an adventurous aristocrat--"+Fore.RESET+" \nor "+Fore.CYAN+"SCOUT --a seasoned adventurer"+Fore.RESET+"? Note that they will have varying skills of Intellegence[INT], Physical Stamina[PHY],\nSocial Skills[SOC], and Primitive Abilities[PRI]\n")
        print(Fore.GREEN+"2) ROLL THE DICE:"+Fore.RESET+" Along your journey, you will be prompted to roll a 12-sided die. What one rolls, determines their fate... \n")
        print(Fore.GREEN+"3) OBSERVE THE OUTCOME:"+Fore.RESET+" Your roll and your partner\'s skills will determine your outcome in the upcoming challenges. The possible results go as follows: \n     Major Loss: 3 or under\n     Loss: 4 to 6\n     Win:7 to 11\n     Major Win: 12 or above\n\n"+Fore.GREEN+"4) HAVE FUN AND GOOD LUCK!")
        print(line+Fore.YELLOW+"\nWill you find the TREASURE? PLAY TO FIND OUT!"+Fore.RESET)
        input(Fore.RESET+"\n*FOR MORE INFO, READ THE DOCUMENTATION!\n"+Fore.GREEN+"PRESS ENTER TO RETURN TO THE MENU: ")

    #partner info
    elif (menuAns=="P"):
        print(Fore.YELLOW+"\'In treacherous ruins, it is a gift to have companion alongside one\'s side...\'\n")
        print(Fore.WHITE+"ROUGE:\n"+Fore.RED+"     BACKGROUND: Seeking adventure, ROUGE left their aristocratic lifestyle to become an adventure. Funded by their family fortune,\nthey travel to find their purpose in the world. A reckless but supportive ally along the journey!\n\n STRENGTHS: PHYSICAL, SOCIAL \n WEAKNESS: PRIMITIVE \n\n SPECIALTY SKILL: DANCE\n   Being upperclass, they can sway from to the beat (or no beat..?) from waltz to breakdance!")
        print(Fore.WHITE+"\nSCOUT:\n"+Fore.CYAN+"     BACKGROUND: Many moons ago, their late uncle seeked the Yushin\'s treasure as SCOUT became his unofficial pupil. When he \npassed, they left dissaproving parents to finish what their uncle started. A quiet but reliable ally along the journey!\n\n STRENGTHS: INTELLEGENCE, PRIMITIVE \n WEAKNESS: SOCIAL \n\n SPECIALTY SKILL: HACK\n   Learning from their uncle\'s tales, they understand and can crack many mechanical puzzles with ease!")

        input(Fore.RESET+"\n*FOR MORE INFO, READ THE DOCUMENTATION!\n"+Fore.GREEN+"PRESS ENTER TO RETURN TO THE MENU: ")

    #exit
    elif(menuAns=="E"):
        print(Fore.YELLOW+"THANK YOU FOR PLAYING! FAREWELL!")
        leaveGame=True

    else:
        print("PLEASE GIVE A VALID INPUT!\n\n")
    
    print(Fore.RESET+breakLine)