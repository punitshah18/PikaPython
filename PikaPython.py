import time
import random

#-----------------------------------------------------------

def truefalse():
  que = ""
  que1 = ""
  que2 = ""
  que3 = ""
  que4 = ""

  print("============================================")
  que = input("BRONZOR: ZUBAT is a dark type (T/F)")
  time.sleep(1)
  que = que.upper
  que1 = input("BRONZOR: You can find GOLBAT in MT. MOON (T/F)")
  time.sleep(1)
  que1 = que1.upper
  que2 = input("BRONZOR: Electric moves have no effect on rock types (T/F)")
  time.sleep(1)
  que2 = que2.upper
  que3 = input("BRONZOR: RARE CANDIES only allow you to level up in increments of 1 (T/F)")
  time.sleep(1)
  que3 = que3.upper
  que4 = input("BRONZOR: REVIVES revivie a Pokemon and heals them to full health (T/F)")
  time.sleep(1)
  que4 = que4.upper
  
  if(que == "T") and (que1 == "T") and (que2 == "F") and (que3 == "F") and (que4 == "T"):
    print("BRONZOR: Wow PIKACHU! You got all five correct! A deal is a deal! The way to the exit is.........................")
    pikaend()
  else:
    print("BRONZOR: Sorry PIKACHU but you got one or more answers wrong! I cannot give you the directions to the exit :(")

#-----------------------------------------------------------
    
def fill():
  guess2 = ""
  while not (guess2 == "nintendo"):
    guess2 = input("Guess the word: N__T_ND_ \n")
    if(guess2 == "NINTENDO") or (guess2 == "nintendo"):
      print("PARAS: Well done! Continue along the path :)")
      break
    else:
      print ("PARAS: Try again!")

#-----------------------------------------------------------
      
def pokeball2():
  poke = random.randint(1,4)
  if (poke == 1):
    print ("PIKACHU received a POTION!")
  elif (poke == 2):
    print ("PIKACHU received a TM01!")
  elif (poke == 3):
    print ("PIKACHU received a REVIVE!")
  else:
    print ("PIKACHU received an ANTIDOTE!")

#-----------------------------------------------------------
    
def pokeball():
    print("───────▄█████████████▄──────")
    print("─────▄███▓▓▓▓▓▓▓▓▓▓▓▓▓███▄────")
    print("────███▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███───")
    print("───██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██──")
    print("──██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─")
    print("─██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██─")
    print("██▓▓▓▓▓▓▓▓▓▓▓▓███████▓▓▓▓▓▓▓▓▓▓▓▓██")
    print("██▓▓▓▓▓▓▓▓▓▓▓██░░░░░██▓▓▓▓▓▓▓▓▓▓▓██")
    print("██▓▓▓▓▓▓▓▓▓▓██░░███░░██▓▓▓▓▓▓▓▓▓▓██")
    print("██████████████░░███░░██████████████")
    print("██░░░░░░░░░░██░░███░░██░░░░░░░░░░██")
    print("██░░░░░░░░░░░██░░░░░██░░░░░░░░░░░██")
    print("██░░░░░░░░░░░░███████░░░░░░░░░░░░██")
    print("─██░░░░░░░░░░░░░░░░░░░░░░░░░░░░██─")
    print("──██░░░░░░░░░░░░░░░░░░░░░░░░░██──")
    print("───██░░░░░░░░░░░░░░░░░░░░░░██───")
    print("────███░░░░░░░░░░░░░░░░░███────")
    print("─────▀███░░░░░░░░░░░░░███▀────")

#-----------------------------------------------------------
    
def pikaend():
  time.sleep(1)
  print("PIKACHU continues down the path he is on. He sees a light in the distance! \nHe found the exit!")
  time.sleep(1) 
  print ("He runs out to see ASH waiting for him. \nThey are reunited and continue their journey on ROUTE 4!")
  time.sleep(1)
  pikaart()
  print("\n___     __   __     __  ")
  print(" | |__||_   |_ |\\ ||  \\ ")
  print(" | |  ||__  |__| \\||__/ ")
  quit()
  
#-----------------------------------------------------------
  
def Scramble():
  guess = " "
  phrase1 = "ABSENCE MAKES THE HEART GROW FONDER"
  i = 0
  time.sleep(1)
  while not (guess == phrase1):
    print ("=====================================")
    print ("aeencbs kmaes eht reaht gwor donfer")
    time.sleep(1)
    guess = input("Unscramble the sentence! \n")
    guess = guess.upper()
    if(guess == phrase1):
      print ("GEODUDE smiles and nods his head! \n It turns out he was faking the whole time! He was waiting for the right Pokemon to come along and solve his puzzle!")
      pikaend()
      break
    if not(guess == phrase1):
      print ("GEODUDE: *Shakes head* \nGuess again")
      i = i+1
      if (i==3):
        ("GEODUDE looks at you in disgust and leaves")
        break
      
#-----------------------------------------------------------
    
def pikaart():
  print("                                           ")
  print("                                        _.| ") 
  time.sleep(0.5)
  print("                                      .'  | ")
  time.sleep(0.5)
  print("                                    ,'    |")
  time.sleep(0.5)
  print("                                   /      /")
  time.sleep(0.5)
  print("                      _..----\"\"---.'      /")
  time.sleep(0.5)
  print("_.....---------...,-\"\"                  ,'")
  time.sleep(0.5)
  print("`-._  \\                                /")
  time.sleep(0.5)
  print("`    -.+_            __           ,--. .")
  time.sleep(0.5)
  print("         `-.._     .:  ).        (`--\"| \\ ")
  time.sleep(0.5)
  print("              7    | `\" |         `...'  \\ ")
  time.sleep(0.5)
  print("              |     `--'     '+\"        ,\". ,\"\"-")
  time.sleep(0.5)
  print("              |   _...        .____     | |/    '")
  time.sleep(0.5)
  print("         _.   |  .    `.  '--\"   /      `./     j");
  time.sleep(0.5)
  print("        \\' `-.|  '     |   `.   /        /     /")
  time.sleep(0.5)
  print("        '     `-. `---\"      `-\"        /     /")
  time.sleep(0.5)
  print("         \\       `.                  _,'     /")
  time.sleep(0.5)
  print("          \\        `                        .")
  time.sleep(0.5)
  print("           \\                                j")
  time.sleep(0.5)
  print("            \\                              /")
  time.sleep(0.5)
  print("             `.                           .")
  time.sleep(0.5)
  print("              +                          \\")
  time.sleep(0.5)
  print("              |                           L")
  time.sleep(0.5)
  print("              |                           |")
  time.sleep(0.5)
  print("              |  _ /,                     |")
  time.sleep(0.5)
  print("              | | L)'..                   |")
  time.sleep(0.5)
  print("              | .    | `                  |")
  time.sleep(0.5)
  print("              '  \\'   L                   '")
  time.sleep(0.5)
  print("               \\  \\   |                  j")
  time.sleep(0.5)
  print("                `. `__'                 /")
  time.sleep(0.5)
  print("              _,.--.---........__      /")
  time.sleep(0.5)
  print("             ---.,'---`         |   -j\"")
  time.sleep(0.5)
  print("              .-'  '....__      L    |")
  time.sleep(0.5)
  print("            \"\"--..    _,-'       \\ l||")
  time.sleep(0.5)
  print("                ,-'  .....------. `||'")
  time.sleep(0.5)
  print("            _,'                /")
  time.sleep(0.5)
  print("          ,'                  /")
  time.sleep(0.5)
  print("         '---------+-        /")
  time.sleep(0.5)
  print("                  /         /")
  time.sleep(0.5)
  print("                .'         /")
  time.sleep(0.5)
  print("              .'          /")
  time.sleep(0.5)
  print("            ,'           /")
  time.sleep(0.5)
  print("          _'....----\"\"\"\"\" ")
  time.sleep(0.5)

#-----------------------------------------------------------

def Battle1():
  hp=20
  hpz=35
  move=''
  num=0
  print("PIKACHU has 20 health points, and STEELIX has 35! ")
  time.sleep(1)

  while(hp>0 and hpz>0):
    time.sleep(1)
    move = input("\nWhat move will PIKACHU use? (a/b/c/d) \na) THUNDERSHOCK \nb) QUICK ATTACK \nc) SLAM \nd) THUNDERBOLT \n")
    time.sleep(1)

    if(move=="a"):
      print("PIKACHU used THUNDERSHOCK")
      time.sleep(1)
      hpz -= 12
    
    elif(move=="b"):
      print("PIKACHU used QUICK ATTACK")
      time.sleep(1)
      hpz -= 5
    
    elif(move=="c"):
      print("PIKACHU used SLAM")
      time.sleep(1)
      hpz -= 8
    
    elif(move=="d"):
      print("PIKACHU used THUNDERBOLT")
      time.sleep(1)
      hpz -= 12

    print("STEELIX now has ",hpz," health points")
    time.sleep(1)
    print("===================================")

    if(hpz<=0):
      print("STEELIX has lost! \nSTEELIX: Congratulations PIKACHU! You have made it out of MT. MOON!")
      time.sleep(1)
      pikaend()
      break
    
    num = random.randint(1,4)
    if(num==1):
      print("STEELIX used SMACK DOWN")
      time.sleep(1)
      hp -= 12
    
    elif(num==2):
      print("STEELIX used IRON TAIL")
      time.sleep(1)
      hp -= 10
    
    elif(num==3):
      print("STEELIX used HYPERBEAM \nIt missed!")
      time.sleep(1)
      hp -= 0
    
    elif(num==4):
      print("STEELIX used GIGA IMPACT")
      time.sleep(1)
      hp -= 15

    print("PIKACHU now has ",hp," health points")
    time.sleep(1)
    print("==========================")
    
    if(hp<=0):
      print("PIKACHU was knocked out! \nSTEELIX: Better luck next time! \nSTEELIX throws PIKACHU down to the lower level!\nPIKACHU wakes up an hour later \n")          
      time.sleep(1)
      break 

#-----------------------------------------------------------

def Battle2():
  hp=20
  hpz=20
  move=" "
  num=0
  print("Both PIKACHU and ZUBAT have 20 health points! ")
  time.sleep(1)

  while(hp>0 and hpz>0):
    time.sleep(1)
    move = input("\nWhat move will PIKACHU use? (a/b/c/d) \na) THUNDERBOLT \nb) QUICK ATTACK \nc) SLAM \nd) THUNDERSHOCK \n")
    time.sleep(1)

    if(move=="a"):
      print("PIKACHU used THUNDERSHOCK\n It was super effective!")
      time.sleep(1)
      hpz -= 12
    
    elif(move=="b"):
      print("PIKACHU used QUICK ATTACK")
      time.sleep(1)
      hpz -= 5
    
    elif(move=="c"):
      print("PIKACHU used SLAM")
      time.sleep(1)
      hpz -= 8
    
    elif(move=="d"):
      print("PIKACHU used THUNDERBOLT\n It was super effective! ")
      time.sleep(1)
      hpz -= 15

    print("ZUBAT now has ",hpz," health points")
    time.sleep(1)
    print("===================================")

    if(hpz<=0):
      print("ZUBAT has lost! \nZUBAT: Congratulations PIKACHU!")
      time.sleep(1)
      break
    
    num = random.randint(1,4)
    if(num==1):
      print("ZUBAT used WING ATTACK\nThat was not very effective!")
      time.sleep(1)
      hp -= 3
    
    elif(num==2):
      print("ZUBAT used BITE")
      time.sleep(1)
      hp -= 5
    
    elif(num==3):
      print("ZUBAT used TAKE DOWN")
      time.sleep(1)
      hp -= 7
    
    elif(num==4):
      print("ZUBAT used DOUBLE-EDGE")
      time.sleep(1)
      hp -= 10

    print("PIKACHU now has ",hp," health points")
    time.sleep(1)
    print("==========================")
    
    if(hp<=0):
      print("PIKACHU was knocked out! \nZUBAT: Better luck next time! \nZUBAT flys off.\nPIKACHU wakes up an hour later \n")          
      time.sleep(1)
      break

#-----------------------------------------------------------

def Battle():
  hp=20
  hpz=20
  move=" "
  num=0
  print("Both PIKACHU and ZUBAT have 20 health points! ")
  time.sleep(1)

  while(hp>0 and hpz>0):
    time.sleep(1)
    move = input("\nWhat move will PIKACHU use? (a/b/c/d) \na) THUNDERBOLT \nb) QUICK ATTACK \nc) SLAM \nd) THUNDERSHOCK \n")
    time.sleep(1)

    if(move=="a"):
      print("PIKACHU used THUNDERSHOCK\n It was super effective!")
      time.sleep(1)
      hpz -= 12
    
    elif(move=="b"):
      print("PIKACHU used QUICK ATTACK")
      time.sleep(1)
      hpz -= 5
    
    elif(move=="c"):
      print("PIKACHU used SLAM")
      time.sleep(1)
      hpz -= 8
    
    elif(move=="d"):
      print("PIKACHU used THUNDERBOLT\n It was super effective! ")
      time.sleep(1)
      hpz -= 15

    print("ZUBAT now has ",hpz," health points")
    time.sleep(1)
    print("===================================")

    if(hpz<=0):
      print("ZUBAT has lost! \nZUBAT: Congratulations PIKACHU! The hint is.... It is a common idiom. \n ZUBAT flys away. \n")
      time.sleep(1)
      break
    
    num = random.randint(1,4)
    if(num==1):
      print("ZUBAT used WING ATTACK\nThat was not very effective!")
      time.sleep(1)
      hp -= 3
    
    elif(num==2):
      print("ZUBAT used BITE")
      time.sleep(1)
      hp -= 5
    
    elif(num==3):
      print("ZUBAT used TAKE DOWN")
      time.sleep(1)
      hp -= 7
    
    elif(num==4):
      print("ZUBAT used DOUBLE-EDGE")
      time.sleep(1)
      hp -= 10

    print("PIKACHU now has ",hp," health points")
    time.sleep(1)
    print("==========================")
    
    if(hp<=0):
      print("PIKACHU was knocked out! \nZUBAT: Better luck next time! \nZUBAT flys off.\nPIKACHU wakes up an hour later \n")          
      time.sleep(1)
      break    

#-----------------------------------------------------------

def Hangman():
  letter = " "
  i = 0
  word = " "
  x = "M*R*"

  while (i<=2):
    word = x
    print("╔══════════════╗")
    print("|      "+word+"      |")
    print("╚══════════════╝")

    letter = input("\nGuess a letter ")
    letter = letter.upper()
    time.sleep(1)

    if (letter == "E"):
      print ("You guessed the letter E")
      time.sleep(1)

      if (word == "M*R*"):
        print("SANDSHREW: Good job! You have guessed a correct letter! \n==========================\n")
        time.sleep(1)
        x = "MER*"
    
      elif (word == "MER*"):
        print("SANDSHREW: You already guessed that letter!")
        time.sleep(1)
        
      else:
        print("╔══════════════╗")
        print("|     MERP     |")
        print("╚══════════════╝")
        print("SANDSHREW: Congratulations! You have guessed the word! The word is MERP!\n==========================\n")
        time.sleep(1)
        print("\nCLEFAIRY: Wow! Thank you for your help PIKACHU!")
        time.sleep(1)
        break

    elif (letter == "P"):
      print ("You guessed the letter P")
      time.sleep(1)

      if (word == "M*R*"):
        print("SANDSHREW: Good job! You have guessed a correct letter! \n==========================\n")
        time.sleep(1)
        x = "M*RP"
    
      elif (word == "M*RP"):
        print("SANDSHREW: You already guessed that letter!")
        time.sleep(1)
        
      else:
        print("╔══════════════╗")
        print("|     MERP     |")
        print("╚══════════════╝")
        print("SANDSHREW: Congratulations! You have guessed the word! The word is MERP!\n==========================\n")
        time.sleep(1)
        print("\nCLEFAIRY: Wow! Thank you for your help PIKACHU!")
        time.sleep(1)
        break
    
    elif(letter == "Merp") | (letter == "MERP"):
      print("╔══════════════╗")
      print("|     MERP     |")
      print("╚══════════════╝")
      print("SANDSHREW: Congratulations! You have guessed the word! \nThe word is MERP!")
      time.sleep(1)
      print("\nCLEFAIRY: Wow! Thank you for your help PIKACHU! ")
      time.sleep(1)
      break
  
    else:
      print("You have guessed the letter "+letter+" \nSANDSHREW: That is an incorrect letter :(")
      time.sleep(1)
      i = i+1

      if(i==1):
        print("________")
        print("|       |")
        print("|       0")
        print("|      /|\\")
        print("|       |")
        print("|")
        print("|")
        print("\n==========================\n")

      elif(i==2):
        print("________")
        print("|       |")
        print("|       0")
        print("|      /|\\")
        print("|       |")
        print("|      /")
        print("|")
        print("\n==========================\n")
      
      elif(i==3):
        print("________")
        print("|       |")
        print("|       0")
        print("|      /|\\")
        print("|       |")
        print("|      / \\")
        print("|")
        print("\n==========================\n")
        print("SANDSHREW: You lose! The word was MERP!")
        time.sleep(1)
        print("=============================\n")
        time.sleep(1)
        print("CLEFAIRY: Oh no! thank you for your help though PIKACHU! ")
        time.sleep(1)

#-----------------------------------------------------------

def Introduction():
  print("\nPIKACHU and ASH were walking on ROUTE 3 when they stumbled upon MT. MOON.")
  time.sleep(1)
  print("However, to get from ROUTE 3 to ROUTE 4, they must go through MT. MOON!")
  time.sleep(1)
  print("As they walk in, PIKACHU gets distracted by a shiny object but ASH does not notice that PIKACHU has stopped following him.")
  time.sleep(1)
  print("ASH has made it out of the cave when he realizes PIKACHU is not by his side anymore.")
  time.sleep(1)
  print("He starts to worry and calls out to PIKACHU, at the exit, to help him find his way out.")
  time.sleep(1)
  print("With your help, PIKACHU must now figure out how to get out of MT. MOON safely and reunite with ASH!")
  time.sleep(1)

print(" __           |    __  _____")
print("|__)||_/ /\\   |  /  \\(_  |  ")
print("|   || \\/--\\  |__\\__/__) |  ")

cont = input("\nInsert any letter to start ")
Introduction()
cont2 = input("\nInsert any letter to continue ")

time.sleep(1)
print("\nMuch to PIKACHU'S dismay, he finds out that the shiny object was just a stone.")
time.sleep(1)
print("\nPIKACHU looks around for help and sees SANDSHREW and CLEFAIRY. He goes up to them and sees they are playing a game of Hangman.")
time.sleep(1)
print("CLEFAIRY is struggling to guess SANDSHREW'S word and asks PIKACHU to help her.")
time.sleep (3)
hangcont = input("\nInsert any letter to continue ")
time.sleep (3)
print("\nShe has a head, body, and one arm and has guessed two out of the four letters. \nWhat is the word? M*R*");
time.sleep (1)
print(" ________")
print("|       |")
print("|       0")
print("|      /|")
print("|       |")
print("|")
print("|")

#-----------------------------------------------------------

doweplayhangman = input("SANDSHREW: Would you like to play a round of Hangman, PIKACHU? (a/b)\na) YES \nb) NO ")

if (doweplayhangman == 'a'):
  print(" ")
  Hangman()

elif(doweplayhangman=='b'):
  print(" ")

print("\nDISTANT VOICE: PIKACHU!")
time.sleep(1)
print("PIKACHU hears ASH'S voice and is reminded that he is lost.")
time.sleep(1)
print("He asks CLEFAIRY and SANDSHREW for help on where the exit is and they point to a path straight ahead.")
time.sleep(1)
print("Pikachu follows the path and encounters a path to the left and a path to the right.")
time.sleep(1)
path=input("Which way should PIKACHU go? (a/b) \na) LEFT \nb) RIGHT \n")
time.sleep(1)

if(path=="a"):
  print("\n PIKACHU went left but it's a dead end!")
  time.sleep(1)
  print("PIKACHU is cornered by a ZUBAT and is challenged to a battle")
  zubatbattle=input("Do you want to battle ZUBAT? (a/b) \na) YES \nb) NO ")
  time.sleep(1)

  if (zubatbattle=="a"):
    print(" ")
    Battle()
    cont3=input("Insert any letter to continue ")
  elif (zubatbattle=="b"):
    print("ZUBAT flies off!")

elif(path=="b"):
  print("PIKACHU went right.")
  time.sleep(1)

print("PIKACHU follows the path and encounters a ladder!")
ladder=input("\nShould PIKACHU go down the ladder or stay on the current level? (a/b) \na) DOWN \nb) STAY\n")

if(ladder=="a"):
  print("PIKACHU went down the ladder and is now on the lower level of MT. MOON")
  time.sleep(1)
  print("PIKACHU sees GEODUDE and runs over to ask him for help on where the exit is")
  time.sleep(1)
  print("GEODUDE: *cough* *cough* ")
  time.sleep(1)
  print("GEODUDE is sick and cannot speak. He writes something in the dirt on the ground but the words are all scrambled")
  Scramble()

elif(ladder=="b"):
  print("PIKACHU stays on the same level")
  time.sleep(1)
  print("PIKACHU sees a light in front of him...it must be the exit! \nBefore PIKACHU reaches the exit he is cut off by a STEELIX! You two must battle!")
  Battle1()
  Scramble()

time.sleep(1)
print("PIKACHU follows the path until he comes to a dead end!")
time.sleep(1)
print("He looks down and sees a POKEBALL")
pokeball()
time.sleep(2)
pokeball2()
time.sleep(1)
cont4 = input("\nInsert any letter to continue")
time.sleep(1)
print ("=======================================")
time.sleep(1)
print ("\nPIKACHU looks to his right and sees a ladder. He proceeds to take it down to the lower level of MT. MOON")
time.sleep(1)
print("PIKACHU follows the path and comes face to face with PARAS")
time.sleep(1)
print("PARAS: I will not let you pass unless you can solve my fill in the blank ")
time.sleep(1)
fill()
time.sleep(1)
print("=================================")
time.sleep(1)
print("PIKACHU continues on the path and sees a GEODUDE with a DOME FOSSIL and a HELIX FOSSIL")
time.sleep(1)
fossil = input("GEODUDE: Hello PIKACHU! Feel free to take one! Which will you take? (a/b) \na) DOME FOSSIL \nb) HELIX FOSSIL \n")
time.sleep(1)
if (fossil == "a"):
  print("\nPIKACHU has taken the DOME FOSSIL!")
else:
  print("\nPIKACHU has taken the HELIX FOSSIL!")

print("GEODUDE: Good luck with your journey. \nGEODUDE walks away with the other fossil")
time.sleep(1)
print("PIKACHU continues on the path and stumbles into BRONZOR")
time.sleep(1)
print("BRONZOR: I will offer you the way out of MT. MOON if you can answer these five true or false questions correct consecutively on the FIRST TRY")
truefalse()

time.sleep(1)
print("PIKACHU continues down the path and he sees another ladder!")
time.sleep(1)
end = input("Should PIKACHU continue on this path, or should he go DOWN? (a/b) \na) STAY \nb) DOWN")
if (end == "a"):
  print ("PIKACHU went straight!")
  pikaend()
else:
  print ("PIKACHU went down!")
  time.sleep(1)
  print("PIKACHU runs into an(other) ZUBAT!")
  Battle2()
  time.sleep(1)
  print("PIKACHU has won the battle!")
  pikaend()
