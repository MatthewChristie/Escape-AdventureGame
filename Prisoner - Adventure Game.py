# Text-Based Adventure Game
#Matthew Christie
#May 2019 - current

#Import required packages
import time
from random import randint
from os import system
system("title Prisoner - Text-Based Adventure Game")        #Set title of window

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
print("What's your name, Prisoner?")
print(name_array[0], name_array[1], name_array[2], name_array[3])
character_name = input(">>> ")

if character_name == name_array[0]:
    sentence_length = length_array[0]
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

    #Room1
Room1 = True
#while Room1s == True:
print("")           #print Room1 intro
print("You awake back in your cell.")
Room1Input = input("")
