import random
import msvcrt #msvcrt.getch()

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

def rnd(a,b):
    num = random.randint(a,b)
    return(num) 

def keynumber():
    return rnd(1,keyn)

def key():
    keyid = keynumber()
    count = 1
    output = ""
    variable = ""
    while (count <= keyn):
        if(count == keyid):
            output += "[ "
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
            output += " ]  "

        else:
            output += "[   ]  "
        count+=1
    print (output)
    return variable

def help():
    print("To Do")

def score(score_count):
    print ("You Failed. Your score is: %s" % score_count)
    
def game():
    while True:
        score_count = 0
        while True:
            if (key() == msvcrt.getwch()):
                score_count += 1
            else:
                score(score_count)
                break
        print("press q to quit, anything else to retry")
        if (msvcrt.getwch() == "q"):
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
                if (keyn < 0 or keyn > 10):
                    raise Exception()
                break
            except:
                print ("Please, enter a number between 1 and 10")
        game()
    elif(thing == "help"):
        help()