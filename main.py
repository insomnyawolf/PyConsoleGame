import random
import msvcrt #msvcrt.getch()
import os

K1 = "q"
K2 = "w"
K3 = "e"
K4 = "r"
K5 = "v"
K6 = "n"
K7 = "u"
K8 = "i"
K9 = "o"
K10= "p"

keys=[]
keys_print=[]

def rnd(a,b):
    num = random.randint(a,b)
    return(num)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def keynumber():
    return rnd(1,keyn)

def key():
    keyid = keynumber()
    count = 1
    output = ""
    variable = ""
    while (count <= keyn):
        if(count == keyid):
            output += "[="
            if  (keyid == 1):
                output += K1
                variable = K1
            elif(keyid == 2):
                output += K2
                variable = K2
            elif (keyid == 3):
                output += K3
                variable = K3
            elif (keyid == 4):
                output += K4
                variable = K4
            elif (keyid == 5):
                output += K5
                variable = K5
            elif (keyid == 6):
                output += K6
                variable = K6
            elif (keyid == 7):
                output += K7
                variable = K7
            elif (keyid == 8):
                output += K8
                variable = K8
            elif (keyid == 9):
                output += K9
                variable = K9
            elif (keyid == 10):
                output += K10
                variable = K10
            output += "=]"

        else:
            output += "[   ]"
        output += "  "
        count+=1
    keys_print.append(output)
    keys.append(variable)

def start():
    n = 0
    while (n < 10):
        key()
        n+=1
    scroll()

def scroll():
    clear()
    for val in keys_print:
        print(val)

def help():
    print("To Do")

def score(score_count):
    print ("You Failed. Your score is: %s" % score_count)
    
def game():
    while True:
        score_count = 0
        start()
        while True:
            print(keys[0])
            if (keys[0] == msvcrt.getwch()):
                del keys[0]
                del keys_print[0]
                scroll()
                key()
                score_count += 1
            else:
                score(score_count)
                del keys[:]
                del keys_print[:]
                break
        print("press q to quit, anything else to retry")
        if (msvcrt.getwch() == "q"):
            clear()
            break

while True:
    print("Type play , help or quit")
    thing = raw_input()
    if(thing == "quit"):
        break 
    elif(thing == "play"):
        print("Entered Playing Mode")
        print("How many keys do you want?")
        while True:
            try:
                keyn = input()
                if (keyn < 1 or keyn > 10):
                    raise Exception()
                break
            except:
                print ("Please, enter a number between 1 and 10")
        game()
    elif(thing == "help"):
        help()

        # ToDo

#Well Done Score System
#reverse scroll mode

#Proper Game Scroll

#InFile Keybindings


#CODE CLEAN