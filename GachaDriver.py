#importing the GachaItem class and the python random module
from GachaItemsClass import GachaItem as GI
import random as rd

#Initiaise a seed for functions in the random module to use. 
#With no entered parameters the seed will be the current system time.
rd.seed()

#Lists to store the possible gacha rewards(All are lists of objects)
gacha5starCharacter = [GI("c", "Diluc", 5), GI("c", "Mona", 5), GI("c", "Keqing", 5), GI("c", "Qiqi", 5), GI("c", "Jean", 5)]

gacha5starWeapon = [GI("w", "Amos' bow", 5), GI("w", "Skyward Harp", 5), GI("w", "Lost Prayer to the Sacred Winds", 5), GI("w", "Skyward Atlas", 5),
 GI("w", "Skyward Pride", 5), GI("w", "Wolf's Gravestone", 5), GI("w", "Primordial Jade Winged-Spear", 5), 
 GI("w", "Skyward Spine", 5), GI("w", "Aquila Favonia", 5), GI("w", "Skyward Blade", 5)]

gacha4starCharacter = [GI("c", "Sayu", 4), GI("c", "Sucrose", 4), GI("c", "Chongyun", 4), GI("c", "Diona", 4), GI("c", "Kaeya", 4), GI("c", "Rosaria", 4),
 GI("c", "Beidou", 4), GI("c", "Fisch;", 4), GI("c", "Kujou Sara", 4), GI("c", "Lisa", 4), GI("c", "Razor", 4), GI("c", "Gorou", 4),
 GI("c", "Ningguang", 4), GI("c", "Noelle", 4), GI("c", "Barbara", 4), GI("c", "Xingqiu", 4), GI("c", "Amber", 4), GI("c", "Bennett", 4),
 GI("c", "Thoma", 4), GI("c", "Xiangling", 4), GI("c", "Xinyan", 4), GI("c", "Yanfei", 4)]

gacha4starWeapon = [GI("w", "Favonius Warbow", 4), GI("w", "Rust", 4), GI("w", "Sacrificial Bow", 4), GI("w", "The Stringless", 4),
 GI("w", "Eye of Perception", 4), GI("w", "Favonius Codex", 4), GI("w", "Sacrificial Fragments", 4), GI("w", "The Widsith", 4), 
 GI("w", "Favonius Greatsword", 4), GI("w", "Rainslasher", 4), GI("w", "Sacrificial Greatsword", 4), GI("w", "The Bell", 4), 
 GI("w", "Dragon's Bane", 4), GI("w", "Favonius Lance", 4), GI("w", "Favonius Sword", 4), GI("w", "Lion's Roar", 4), 
 GI("w", "Sacrificial Sword", 4), GI("w", "The Flute", 4)]

gacha3starWeapon = [GI("w", "Raven Bow", 3), GI("w", "Sharpshooter's Oath", 3), GI("w", "Slingshot", 3), GI("w", "Emerald Orb", 3),
 GI("w", "Magic Guide", 3), GI("w", "Thrilling Tales of Dragon Slayers", 3), GI("w", "Bloodtainted Greatsword", 3), GI("w", "Debate Club", 3),
 GI("w", "Ferrous Shadow", 3), GI("w", "Black Tassel", 3), GI("w", "Cool Steel", 3), GI("w", "Harbinger of Dawn", 3),
 GI("w", "Skyrider Sword", 3)]


def itemRoll():
    return rd.randint(1, 1000) #function that returns a random integer between 1 and 1000(inclusive)

def typeRoll():
    return rd.choice(("c","w")) #function that randomly chooses c(for chaarcter) and w(for weapon)

#The next two functions are used to determine whether you obtain a weapon or character drop
def roll5star(): 
    #if statement that is true if typeRoll() results in "c". It will then roll from the assigned list of 5 star characters
    #if typeRoll() results in "w" then it will roll from the assigned list of 5 star weapons
    if typeRoll() == "c":
        intRoll = rd.randint(0, 4) #obtains a random number in a given range
        return gacha5starCharacter[intRoll] #Obtains a character from the list of objects based on the random number via index number
    else:
        intRoll = rd.randint(0, 9)
        return gacha5starWeapon[intRoll] 

def roll4star():
    #Logically and functionally similar to roll5star() it will roll from the assiigned list of available 4 star weapons
    #and characters instead of the list of 5 star characters/weapons.
    if typeRoll() == "c":
        intRoll = rd.randint(0, 23)
        return gacha4starCharacter[intRoll]
    else:
        intRoll = rd.randint(0, 17)
        return gacha4starWeapon[intRoll]

def roll3star():
    #Does not require typeRoll() as the list of 3 star items only contains weapons
    #otherwise functionally/logically similar
    intRoll = rd.randint(0, 12)
    return gacha3starWeapon[intRoll]

#global variables that store the "pity". Pity is a bad-luck protection system.
#Pity system: After a certain number of rolls you will be guaranteed an item of a particular rarity
#if you have not received an item of that rarity in that number of pulls.
#Pity for a particualr drop rarity resets when you receive an item of the same particular rarity
pityCount4star = 0
pityCount5star = 0

def GachaStandardBanner():
    #Function to perform the rolls to determine gacha rewards.
    global pityCount5star #the global keyword must be used as variables cannot normally
    global pityCount4star #be updated from inside a function in Python
    #Variable to store an integer from 1 to 1000(represents percentiles from 0.001 to 100)
    gachaRoll = itemRoll()

    #if elif statements to determine the rarity of the drop. Checks from least rare to rarest.
    #3 star drops have a 94.3% chance to drop per pull and no pity system(as they are the most common drop)
    if (gachaRoll < 944) and (pityCount5star < 89) and (pityCount4star < 9):
        pityCount5star += 1 #this line and the line below it are used to raise the pity counter
        pityCount4star += 1 
        return roll3star() #roll3star() is used to determine which 3 star is obtained

    #4 star drops have a 5.1% chance to drop per pull and is safeguarded by a pity system
    #if you're at pity(in this case the tenth pull), you will be guaranteed a 4 star
    #if you were to hit 5 star pity however, the 5 star drop will override the 4 star drop
    #and push the 4 star guarantee to the roll right after
    elif (gachaRoll < 995 or pityCount4star >= 9) and (pityCount5star < 89):
        pityCount5star += 1
        pityCount4star = 0 #sets 4 star pity to 0
        return roll4star() #roll4star() is used to determine which 4 star is obtained

    #5 star drops have a 0.6% chance to drop per pull and is safeguarded by a pity system(similar to 4 stars)
    #However 5 star hard pity is set to the 90th pull instead of tenth
    else:
        pityCount4star += 1
        pityCount5star = 0 #sets 5 star pity to 0
        return roll5star() #roll5star() is used to determine which 5 star is obtained

def gachaPrint(pullNum):
    #function to print the resulting gacha rewards
    pullsDone = 0
    #while loop controlled by a parameter(pullNum) that determines number of rolls that will be done done. 
    #Stops when pullsDone is equal to pullNum
    while pullsDone < pullNum:
        TemporaryGachaRewardData = [GachaStandardBanner()] #list to hold data of a roll to be used in the print function
        #prints and formats item name and rarity of the item object
        print(f"Item Name:{TemporaryGachaRewardData[0].itemName} | Rarity: {TemporaryGachaRewardData[0].itemRarity} Star")
        #prints and formats the current pity for both 5 and 4 stars
        print(f"5 Star Pity: {pityCount5star} | 4 Star Pity: {pityCount4star}")
        #raises pullsDone by 1
        pullsDone += 1
    
def main(): #main function
    print("Welcome to the Genshin Impact Standard Banner roll simulator")
    #While True loop to allow pulling until the program is terminated
    while True:
        #Request for input so user can choose desired pull
        pullChoice = input("""Please choose between these options:
        1: Single Pull
        2: Ten Pull
        3: Pull until obtaining a 5 star
        4: Roll a custom number of times
        5: Quit(Warning: Resets your pity)
        Input: """)
        #if elif statements to check through chosen options
        #pulls once
        if pullChoice == "1":
            gachaPrint(1)

        #pulls 10 times
        elif pullChoice == "2":
            gachaPrint(10)
        
        #Pulls until you obtain a 5 star
        elif pullChoice == "3":
            no5star = True #store True in a variable so that we may update it
            while no5star:
                gachaPrint(1)
                #When you obtain a 5 star, its pity is set to 0. This fact can be used to check whether a 5 star has been obtained
                #When it does happen no5star is updated to false
                if pityCount5star == 0:
                    no5star = False

        #Choice 4 allows the user to input as many pulls as they want
        elif pullChoice == "4":
            while True: #request for input of number of desired pulls
                try: 
                    #utiliszing try-except for input validation
                    pullCustom = int(input("Enter a positive integer value to determine the number of pulls: "))
                except ValueError: #even if a word is inputted, the error can be caught and does not end the program
                    print("Not an integer! Enter a valid integer")
                    continue #the loop continues until a valid input is given
                else:
                    gachaPrint(pullCustom) #pulls a number of times equal to the input
                    break #breaks out of the While True loop

        #ends the program
        elif pullChoice == "5":
            quit()
        
        #input validation for choosing options
        else:
            pullChoice = input("Please enter a valid option: ")

main() #Calls main