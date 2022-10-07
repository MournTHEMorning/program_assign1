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
 #The multiline comment/string is to quicken debugging and testing
        """verify="N"
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
"""
        #FORCING PLAYERNAME=TESTER_NAME
        playerName=Fore.GREEN+"Tester_Name[Please-add-RESET-at-end]"

            #FORCING ROUGE AS PARTNER
        # gMod.RougeAccess().selectRouge() 
        # print(gMod.RougeAccess().getRoleStatus())
        # print("ROUGE!")

        #     #FORCING SCOUT AS PARTNER
        gMod.ScoutAccess().selectScout()
        print(gMod.ScoutAccess().getRoleStatus())
        print("SCOUT")

        #gotta print out treasure after the game end+menu pops up. Add a breakline after the player's role to see stats. Then input statement after the roll, to see results? (skip that for now, but add later)

        #commentted out intro, level 1, 2a for faster testing
        """
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

        #Intro for lv2a
        print(breakLine+"Around your team, the perimeter begin to disappear into the ground one by one. You cling to the wall, as the growing void nears. \nYou yelp, yet gravity does not seem to greet you. The growing void strangely stops a couple meters from where you stand. \nAnother tremble, as the couple meters of land begin to descend like an old elevator.\nAs the sun goes further away, the platform continues downwards and a rancid smell begins to grow. You inch away from the wall \nto look off the ledge, causing you to scream in horror. A skull was inches away from your face, as others seem to \nglare in envy at your safe descent. The rotting smell of death seems to grow, as the platform stops in a rumble.")

        #specialized dialogue (for character growth)
        if (gMod.RougeAccess().getRoleStatus()):
            print("\nROUGE happily hops off the platform, eager to see solid ground."+Fore.RED+"\nROUGE: Whew... That almost felt like forever! So, where are we...?"+Fore.RESET+" They feel their waist coat and \'A-ha!\' at a lighter."+line)
        else:
            print("\nSCOUT cautiously walks off the platform. You hear them sifting through their large backpack. Warmth welcomes you.\n"+Fore.CYAN+"SCOUT: It\'s safe."+Fore.RESET+" They tilt their head towards the tunnel."+line)

        print("The moment you step off the platform, it begins to ascend. You reach out, as if it will respond. \nSlowly, the rest of the cave is shrouded in darkness. With caution, you both walk into\nthe tunnel. Ominously, the cavern is coated with dried blood, skeletons, and chewed up clothes from various eras.\nStrangely, there is an especially large pile of skeletons near a golden Y-shaped sigil. Curious, you walk towards \nit, as the walls are painted in vibrant colour and rich history. \nQuickly you take out your camera for later analysis.\n"+playerName+": This is Yushin\'s unrecorded history! I-i-- Did they use paints? \nWow, I wish I can collect samples!! Oh, I wonder... \n"+Fore.RESET+"You continue to rant and take pictures, as your team goes deeper into the cavern.\n")

        #lvl 2a
        print("For hours, your team sees broken bridges to obvious tripwires. You even used a grappling hook, but it broke on the \nlast swing... Ahead, you barely see a worn out tightrope with rusted spears under it.")
        #specialized dialogue
        if (gMod.RougeAccess().getRoleStatus()):
            print(Fore.RED+"\nROUGE: Ah! I wish we still had our grappling hook..."+Fore.RESET)
        else:
            print("\nSCOUT stays silent and mutters a \'huh...\' Strangely, instead of looking forward, your partner follows a white line towards a wall."+Fore.CYAN+"\nSCOUT: Wait a moment... Is this?"+Fore.RESET)
        rollAgain=True

        #rolling for lv2a, similar as above
        while(rollAgain):
            if(gMod.RougeAccess().getRoleStatus()):
                rollInput=input(breakLine+Fore.GREEN+"ROLL for PRIMITIVE![Input R]: ").upper()
            else:
                rollInput=input(line+Fore.GREEN+"\nSCOUT\'s SPECIALITY [HACK] IS IN EFFECT!\nROLL to support them![Input R]: ").upper()

            diceResult=gMod.dice(rollInput)
            rollAgain=False

            if(type(diceResult)==int):
                print("YOU ROLLED:"+Fore.RESET,diceResult)
            else:
                print("Please roll again!")
                rollAgain=True

            #adding ROUGE: PRI bonus
        if(gMod.RougeAccess().getRoleStatus()==True):
            print(Fore.RED+"PARTNER\'S BONUS(PRI):"+Fore.RESET, gMod.RougeAccess().getPRI())
            bonus=gMod.traitBonus(diceResult,gMod.RougeAccess().getPRI())

            #adding SCOUT: HACK bonus
        else:
            print(Fore.CYAN+"PARTNER\'S BONUS(HACK):"+Fore.RESET, gMod.ScoutAccess().getSpecial())
            bonus=gMod.traitBonus(diceResult,gMod.ScoutAccess().getSpecial())

        print("YOU AND YOUR PARTNER ROLLED A", bonus)

        #lv2a results
        if(gMod.winLoss(bonus)==0):
            print("You recieved: "+Fore.YELLOW+"a CRIT LOSS(3 and under)!"+line)
            if(gMod.RougeAccess().getRoleStatus()):
                print("Panicking, ROUGE goes to the edge of the pit.\n"+playerName+": Hey, what are you--"+Fore.RESET+" ROUGE throws the lighter into the pit, as you rush over to them.\n"+playerName+": ROUGE! WHY DID YOU DO THAT?"+Fore.RED+"\nROUGE: I-i thought maybe there would be a-- "+Fore.RESET+"You shush them in irritation.\nUsing the little cave light available, you cross first. Your arms wave in the air helplessly, \nas your feet wobble forwards. When you feel solid ground, you call your partner over.\nWanting to catch up, ROUGE steps erratically. Every step they take is like risk. For what seems like forever, \nROUGE jumps the last few feet, as the darkness emits a loud \'SNAP!\' \nA body crashes into you, almost making you both to fall into the pit.")
            else:
                print("Thinking SCOUT has gotten tired from the travel, you look away for a moment, thinking how to approach the tightrope. \nLike how dawn turns to night, you wonder why the light has lessened. You look at SCOUT but, they are no one in sight. \nYou panic, shouting their name. From the other side of tightrope, you notice a growing light\n"+playerName+": SCOUT! Is that you? "+Fore.RESET+"SCOUT waves over, emerging from the wall...? They wave you over, \nas anxiousness crawls up your spine. Your arms wave in the air helplessly, as your feet wobble forwards in \nhope of better footing. \nAs you come closer to solid ground, your feet begin to move erratically. \nHearing a \'SNAP'\ from behind, you jump the last bit of distance. You crash into SCOUT, as they groan from impact.")
        elif(gMod.winLoss(bonus)==1):
            print("You recieved:"+Fore.YELLOW+"a LOSS(4-6)!"+line)
            if(gMod.RougeAccess().getRoleStatus()):
                print("Panicking, ROUGE goes to the edge of the pit.\n"+playerName+": Hey, what are you-- "+Fore.RESET+"In sudden realization, you run to stop them from throwing away the lighter.\nYou grab them just in time, glaring at them."+Fore.RED+"\nROUGE: I-i thought maybe there would be a--\n"+playerName+": I don\'t even want to hear it..."+Fore.RESET+"\nUsing the remaining light, you cross first. Your arms wave in the air helplessly, as your feet wobble \nforwards in hope of better footing. Your vision is growing dimmer and dimmer, as the tightrope almost \ndisappears from beneath you. Without any sight, you find your way to solid ground, calling your partner over.\nYou see them pacing and encouraging themselves before their attempt. Every step they take is a risk."+Fore.RED+"\nROUGE: Whew! That was not so bad-- "+Fore.RESET+"The lighter goes out, leaving you to sigh.")
            else:
                print("Thinking SCOUT has gotten tired from the travel, you look away for a moment, thinking how to approach the tightrope. \nLike how dawn turns to night, you wonder why the light has lessened. You look at SCOUT but, they disappear behind a wall. \nConfused, you hit the wall, as you shout their name.\n"+playerName+": They will come back... right? "+Fore.RESET+"Then, you notice a growing light and call out to SCOUT, who waves you over. \nYour arms wave in the air helplessly, as your feet wobble forwards in hope of better footing. \nAs you come closer to solid ground, your feet begin to move erratically but eventually reach solid ground.\n"+playerName+": Where did you go?"+Fore.CYAN+"\nSCOUT: Secret passage. I guess you were not behind me."+Fore.RESET)
        elif(gMod.winLoss(bonus)==2):
            print("You recieved: "+Fore.YELLOW+"a WIN(7-11)!"+line)
            if(gMod.RougeAccess().getRoleStatus()):
                print("Panicking, ROUGE goes to the edge of the pit.\n"+playerName+": Hey, what are you-- "+Fore.RESET+"With a grand gesture, they throw the lighter to other side, as the fire extinguishes.\n"+playerName+": ROUGE! WHY DID YOU DO THAT?"+Fore.RED+"\nROUGE: I was thinking we could save the lighter for later..? Oh.. Yeah, that was not a smart idea, was it?"+Fore.RESET+"\nYou facepalm, having to work with the faint cave light. After adjusting to the darkness, you cross first. Your arms wave in the \nair helplessly, as your feet wobble forwards in hope of better footing. Eventually, you feel solid ground and call your partner over.\nYou see them pacing before their attempt, and every step feels infinite."+Fore.RED+"\nROUGE: Whew! That was not so bad! The lighter is here too! "+Fore.RESET+"\nThey grin and click the lighter, revealing the path once again.")
            else:
                print("Curious, you observe SCOUT fiddle with the wall. "+Fore.CYAN+"\nSCOUT: It is not a wall... but rather a secret tunnel. "+Fore.RESET+"\nAlmost on queue, the stone wall slides open, and SCOUT closes up their backpack. In the tunnel, \nthere are odd structures, and with all the rumbling, it causes haste to your step. Understanding, your team jogs \ndown the tunnel to another \'wall\'. Within minutes, SCOUT breaks the mechanism, leading you to the other side.")
        #ROUGE's crit win is logically impossible, since -2(PRI skill)+12(max on die)=10(win, not crit win)
        #HENCE, only SCOUT's is available for crit win
        elif(gMod.winLoss(bonus)==3):
            print("You recieved: "+Fore.YELLOW+"a CRIT WIN(12 and above)!"+Fore.RESET+line)
            print("Curious, you observe SCOUT fiddle with the wall. "+Fore.CYAN+"\nSCOUT: It is not a wall... but rather a secret tunnel. "+Fore.RESET+"\nAlmost on queue, the stone wall slides open, and SCOUT closes up their backpack. In the tunnel, \nthere are torches around. SCOUT lights the torches within the secret passageway, revealing a cobblestone shrine. \nThe both of you gasp, remembering the Yushin\'s tradition of remembering the departed. \nQuickly, you take photos and gently remove a papyrus from the wall."+Fore.CYAN+"\nSCOUT: What does it say,"+playerName+Fore.CYAN+"? "+Fore.RESET+"You quickly translate the characters.\n"+playerName+": \'Dearest\', I think it\'s a name, \'Ethikosh, we miss you dearly. May you rest \nin your art of passion.\' ...I think they built this place."+Fore.CYAN+"\nSCOUT: Amazing... Can we take it? "+Fore.RESET+"You smile and nod, placing the papyrus in their backpack. You glance at the shrine once more and take \nthe torch with you, before leaving the side room.")

            
        print(line+"Every step leads to more cramped spaces and traps. Your partner had a close call with a pressure plate and poison darts.\nThe deeper you go, the more rustling and clattering you hear from the darkness... It must be the wind, right?\nOn the bright side, there are less bodies and blood on the path, which means that the treasure awaits...")

        #intro to lvl2b setting
        print(breakLine+"Many kilometres later, there is a sunlit path. You look at each other and walk a little bit faster. The small pathways lead to a large, \nchiseled cave painted in gold and white. Even stranger, ores upon ores of luminous gemstones emulate sunlight, \neven growing grass and being a habitat to insects and rodents. You snap a picture but it fails to capture the moment.\n"+playerName+": Wow... This is amazing! And over there! "+Fore.RESET+"\nYou point towards marble stairs, leading to a large circular doorway... with a keyhole.\n"+playerName+": Oh, come on! "+Fore.RESET+"Stomping towards the door, you hear a click beneath your feet. \nRumble. Arm being pulled. Fallen down. You let your mind catch up.")

        #specialized dialogue, player almost dying (lvl 2ab)
        if (gMod.RougeAccess().getRoleStatus()):
            print(Fore.RED+"\nROUGE: Glad I\'m not the only one with pressure plate problems! You almost got smashed by that rock, friend!"+Fore.RESET)
        else:
            print(Fore.CYAN+"\nSCOUT: ...please be careful. "+Fore.RESET+"They look at you with a silent worry.")
        
        #intro to lvl2b puzzle
        print(line+"You look ahead to see cobblestone flooring with a stalactite standing where you once stood.\n"+playerName+": Just like the poison darts... but why does this look-- OH! "+Fore.RESET+"\nQuickly, you scour your camera roll for... that one! \nYou wave over your partner, showing one of the murals from the entrance. The photo shows a painted version of the room with a\nred line, gesturing the way through the door is through the path. \n\nIn short, by following the path, the team will pass safely, or else...")

        #specialized dialogue, lvl2b
        if (gMod.RougeAccess().getRoleStatus()):
            print(Fore.RED+"ROUGE: So?? What are we waiting for? Let\'s go!"+Fore.RESET+" They look at the cobblestone floor and smile.\n"+Fore.RED+"ROUGE: This actually reminds me of a routine I did one time! Wa-hoo! Takes me back!"+Fore.RESET)
        else:
            print("SCOUT looks ahead with an unreadable expression.")        
        """
        
        rollAgain=True
        #rolling for lv2b, similar as above
        while(rollAgain):
            if(gMod.RougeAccess().getRoleStatus()):
                rollInput=input(breakLine+Fore.GREEN+"ROUGE\'s SPECIALITY [DANCE] IS IN EFFECT!\nROLL to support them![Input R]: ").upper()
            else:
                rollInput=input(line+Fore.GREEN+"\nROLL for PHYSICAL abilities![Input R]: ").upper()

            diceResult=gMod.dice(rollInput)
            rollAgain=False

            if(type(diceResult)==int):
                print("YOU ROLLED:"+Fore.RESET,diceResult)
            else:
                print("Please roll again!")
                rollAgain=True

        #adding bonus
        if(gMod.RougeAccess().getRoleStatus()==True):
            print(Fore.RED+"PARTNER\'S BONUS(DAN):"+Fore.RESET, gMod.RougeAccess().getSpecial())
            bonus=gMod.traitBonus(diceResult,gMod.RougeAccess().getSpecial())

        elif(gMod.ScoutAccess().getRoleStatus()==True):
            print(Fore.CYAN+"PARTNER\'S BONUS(PHY):"+Fore.RESET, gMod.ScoutAccess().getPHY())
            bonus=gMod.traitBonus(diceResult,gMod.ScoutAccess().getPHY())

        print("YOU AND YOUR PARTNER ROLLED A", bonus)


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