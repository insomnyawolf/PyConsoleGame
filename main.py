import random
import msvcrt #msvcrt.getch()
import sys

score = 0

K1 = "d"
K2 = "f"
K3 = "j"
K4 = "k"

def rnd(a,b):
    num = random.randint(a,b)
    return(num)
def keyid():
    id = rnd(1,4)
    if   (id == 1):
        return K1
    elif (id == 2):
        return K2
    elif (id == 3):
        return K3
    elif (id == 4):
        return K4 
def key():
    id = keyid()
    if   (id == K1):
        print("[ " + K1 + " ]  [   ]  [   ]  [   ]")
        return K1
    elif (id == K2):
        print("[   ]  [ " + K2 + " ]  [   ]  [   ]")
        return K2
    elif (id == K3):
        print("[   ]  [   ]  [ " + K3 + " ]  [   ]")
        return K3
    elif (id == K4):
        print("[   ]  [   ]  [   ]  [ " + K4 + " ]")
        return K4
def help():
    print("To Do")
while True:
    print("Type play , help or quit")
    thing = raw_input()
    if(thing == "quit"):
       break 
    elif(thing == "play"):
        print("Entered Playing Mode")
        while True:
            id = key()
            thing = msvcrt.getwch()
            if (id == thing):
                score += 1
            else:
                print ("You Failed. Your score is: %s" % score)
                break
    elif(thing == "help"):
        help()
    else:
        continue