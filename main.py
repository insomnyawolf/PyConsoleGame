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

class utils:

    def rnd(self,a, b):
        num = random.randint(a, b)
        return (num)

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def help(self):
        print("To Do")


class game:

    def keynumber(self):
        u = utils()
        return u.rnd(1, keyn)

    def key(self):
        g = game()
        keyid = g.keynumber()
        count = 1
        output = ""
        variable = ""
        while (count <= keyn):
            if (count == keyid):
                output += "[="
                if (keyid == 1):
                    output += K1
                    variable = K1
                elif (keyid == 2):
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
            count += 1
        keys_print.append(output)
        keys.append(variable)

    def scroll(self):
        u = utils()
        u.clear()
        x = True
        for val in keys_print:
            if (x):
                print("====" + val + "====")
                x = False
            else:
                print("    " + val + "    ")

    def start(self):
        n = 0
        g = game()
        while (n < 10):
            g.key()
            n += 1
        g.scroll()

    def score(self,score_count):
        print ("You Failed. Your score is: %s" % score_count)

    def run(self):
        while True:
            score_count = 0
            g = game()
            u = utils()
            g.start()
            while True:
                if (keys[0] == msvcrt.getwch()):
                    del keys[0]
                    del keys_print[0]
                    g.scroll()
                    g.key()
                    score_count += 1
                else:
                    g.score(score_count)
                    del keys[:]
                    del keys_print[:]
                    break
            print("press q to quit, anything else to retry")
            if (msvcrt.getwch() == "q"):
                u.clear()
                break

while True:
    print("Type play , help or quit")
    thing = raw_input()
    if (thing == "quit" or thing == "q" ):
        break
    elif (thing == "help" or thing == "h" ):
        u = utils()
        u.help()
    elif (thing == "play" or thing == "p"):
        print("Entered Playing Mode")
        print("How many keys do you want?")
        while True:
            #try:
                keyn = input()
                #if (keyn < 1 or keyn > 10):
                    #raise Exception
                g = game()
                g.run()
                break
            #except:
                #print ("Please, enter a number between 1 and 10")


        # ToDo

#Well Done Score System
#reverse scroll mode

#Proper Game Scroll

#InFile Keybindings


#CODE CLEAN