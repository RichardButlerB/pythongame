# name: Killer Z
# author: Rich
# 4-3-19
# description: Zombies attach! will you make it out alive?
import sys
import random
import time
from time import sleep


def displayIntro():
    print("Zombies are coming!!!")
    print("Will you survive through the night and make it to saftey")
    print("Enter Your Name if you DARE\n")
displayIntro()
time.sleep(2)
uname = input("What is your name? ")
print("Hello", uname)
time.sleep(1)
ready = input("Are you ready? [y/n] ")
if ready.lower() == "n": #in case of caps
    time.sleep(1)
    print("I see! You are not brave enough. YOU MUST NEED TO PREPARE FURTHER!")
    quit()
if ready.lower() == "y":
    time.sleep(1)
    print("I hope so!", uname +",", "Your journey starts at home in a two story house, in your bed.\nIt is 3am and a scratching noise awakens you from the first floor window \n")


def choosepath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("What do you do?\n[1] Go back to sleep and hope for the best  [2] Go check it out and protect what is yours? " )

        if path == "1":
            print("\nBIG MISTAKE!!!")
            print("The noise you were awoken by was not a bird nor a cat, in fact it was a hungry ZOMBIE")
            print("the zombie broke the window and let his zombie friends in.")
            print("they made their way up the stairs and into you room while you slept")
            print("you knew you made a BIG MISTAKE from the first bite.")
            print("you screamed at the top of your lungs while the hoard of zombies ate at your flesh")
            exit()

        if path == "2":
            print("\nYou slowly sit up from your bed looking for something you could use as a weapon just in case you need it.")
            print("walking lightly to your closet and the noise has not stopped, You STOP suddenly to listen to the noise of a cracking window")
            time.sleep(1)
            print("\nwhat ever it is it sounds like it may have come in the house.")
            print("you slowly carry on to the closet and in the closet you need to choose your weapon")
            time.sleep(1)
    return path
choosepath()


def weapon():
    chooseWeapon = ""
    while chooseWeapon != "1" and chooseWeapon != "2" and chooseWeapon != "3":
            chooseWeapon = input("\nWhat is your weapon of choice?\n [1]Your trusty shotgun?\n [2]An old Samurai Souvenir\n [3]Mag Flash light \n choose wisely..")


            if chooseWeapon == "1":
                print("Excellent choice. The shotgun has tremendous power, however it is also loud and will attract the others.\n"
                  "you cock the shotgun ever so quietly as to not alert whatever is making the sound downstairs.\n")
            time.sleep(9)
            def goshotty():
                    print("You head to the stairs, slowly while trying to be as silent as possible.\n"
                        "You hear light creaking under feet as you reach the first step of the stairs\n"
                        "sweating and trembling you take a deep breath and take the first step\n"
                        "pausing to listen for any noises\n"
                        "its so dark you think to yourself - very quickly to not distract from self preservation\n"
                        "the stairs are creeking louder now\n"
                        "you have arrived at the bottom step and....\n")
                    time.sleep(9)
                    print("The noise you were awoken to is louder now. It sounds like a pack of wolves feasting on a giant caribou\n"
                            "you take your last step and the step makes a high pitch creeeeeaaaak \n")
                    time.sleep(9)
                    print("the movement and sounds stop\n"
                            "you quickly look towards the window\n"
                            "5 undead beings are eating your dog")
                    dog = input("You ready your shotgun, aim at the 5 beings that spotted you. \n"
                            "[1] Squeeze the trigger and shoot [2] run back upstairs")
                    if dog == "1":
                                print("You shoot the first Zombie that runs at you\n"
                                "\n!!!!!!!!!!!!!!\n"
                                "!!!!!BANG!!!!!\n"
                                "!!!!!!!!!!!!!!\n"
                                "\nThe second Zombie jumps at you and you pull the trigger and nothing.\n"
                                "There was only one bullet in the shotgun, and you have used it.\n"
                                "you swing the shotgun like a bat and take out 2 zombies\n"
                                "another zombie lunges at you and you kick it in the balls\n"
                                "its balls fall to the floor\n"
                                "as you are standing there you're in shock that the zombie had balls\n"
                                "while in shock the last zombie jumps at you from behind and tears apart the nape of you neck\n ")
                    time.sleep(6)

                    dead = "!!!!!!YOUR DEAD!!!!!!"
                    for char in dead:
                            sleep(0.1)
                            print(dead, end="", flush=True)


            goshotty()

            if chooseWeapon == "2":
                print("waaaaa taaaaa you think you are a ninja huh? well the Samurai sword is a great choice. Its silent, has reach and is very sharp")


            if chooseWeapon == "3":
                print("ok this will do. you will be able to see, its heavy and you can wack anything that comes your way.")

    return chooseWeapon
weapon()




