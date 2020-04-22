# Text-Based Adventure Game
#Matthew Christie
#May 2019 - current

#Import required packages
import time
from random import randint
from os import system
system("title Prisoner - Text-Based Adventure Game")        #Set title of window


exit = False

while exit == False:


    def Display_Program_Information():
        print("")
        print("")
        print("'Escape' - Text Based Adventure Game")              #Display Program Information
        print("")
        print("Coded/Written By Matthew Christie")
        print("")
        print("Build: V0.1")
        print("")
        print("")
        print("")
        print("")
        time.sleep(2)
        return

    name_array = ["John", "James", "Clara", "Ramona"]
    start_array = [randint(50, 1400), randint(50, 13000), randint(50, 5000), randint(50, 10000)]
    length_array = [4,38,14,29]


    intro_loop = False
    Room1 = False
    Room2 = False
    Room3 = False
    Room4 = False



    #Function Declarations
    def intro():
        print (character_name, start_day, sentence_length)
        return

        #Intro
    #print("What's your name, Prisoner?")
    #print(name_array[0], name_array[1], name_array[2], name_array[3])
    #character_name = input(">>> ")
    #character_name = character_name.lower

    #Print character selection on seperate lines with the addition of short bios
    print("What's your name again prisoner?")
    print("")
    #print("[" + name_array[0] + "]"
    print("      is a wild card. Ever since a young age he was in with the wrong crowds and couldn't stay out of trouble.")
    print("")
    print(name_array[1])
    print("")
    print(name_array[2])
    print("")
    print(name_array[3])
    print("")
    character_name = input(">>> ")


    if character_name == name_array[0]:
        sentence_length = length_array[0]
        sentence_length_intro = ""
        start_day = start_array[0]
        intro()
    elif character_name == name_array[1]:
        sentence_length = length_array[1]
        start_day = start_array[1]
        intro()
    elif character_name == name_array[2]:
        sentence_length = length_array[2]
        start_day = start_array[2]
        intro()
    elif character_name == name_array[3]:
        sentence_length = length_array[3]
        start_day = start_array[3]
        intro()



    # Days Served THEN YEARS TOTAl WHICH MEANS DAYS LEFT
    # start_day DAYS -THEN- sentence_length YEARS -WHICH MEANs- (sentence_length*365)-start_day
    #print("So," + (character_name) + " it says here you're in for ..., with" + (start_day) + " years served of a" + (sentence_length) +  " year sentence - wow")

    days = (sentence_length)*365 - start_day
    print(" So " + str(character_name) + ", it says here you're in for ..., with " + str(start_day) + " days served of a " + str(sentence_length) + " year sentence - wow. So just in case you need a hand with that math it means you have, let me see here... " + str(days))
    time.sleep(5)


    #print("So," + (character_name) + " it says here you're in for ..., with" + (start_day) + " years served of a" + (sentence_length) +  " year sentence - wow")


    #Create day generation for what the Warden says
    #sentence_length, randomly choose within this range

        #war_speech = randint(int(sentence_length/2), sentence_length)
    #war_speechS = randint(50, length_array[0])
    #print(war_speechS)



        #Room1 (Start)
    #Room1 = True
    #while Room1s == True:
    #print("")           #print Room1 intro
    #print("You awake back in your cell.")
    #Room1Input = input("")

    #while Room1 == True:     #Creat Loop Function


    #if "Move to room "              #change to make it if input includes phrase "move" + "room ..."

        #Room2


        #Room3


        #Hidden Room (make less conspicious)


        #Room4


        #Room5 (End)
