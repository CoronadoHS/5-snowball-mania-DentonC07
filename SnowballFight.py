''' 
    Name: Snowball-Mania
    Author: Denton Carter
    Date: 12/3/24
    Class: AP Computer Science Principles
    Python: 3.11.5
'''
import random 

def main():
    print("Welcome to Snowball Mania!")
    name = input("What is your name? ") 
    opponent = input("Great to have you here, " + name + "! Who do you want to play against? ")
    print(name + " vs. " + opponent) 

    players = []
    players.append(name)
    players.append(opponent)

    nextPlayer = ""

    while (nextPlayer != "DONE"):
        nextPlayer = input("Are there any more opponents? If so, type them one ar a time (or DONE) and press 'Enter'. ")
        players.append(nextPlayer)
    players.remove("DONE") 

    choice = input("Do you want to choose who you throw the snowball at or do you want it to be random? (Type yes or no) ")

    gameplay(name, players, choice)
 

   

def gameplay(name, players, manual):
    import time   
    while (len(players) > 1): 
        thrower = random.choice(players)
        if (thrower == name):
            if (manual == "yes"):       
                target = input("\nYou are up! Who do you want to throw the snowball at? ")
                while (target == thrower):
                    target = input("No dummy. You can't hit yourself, choose someone else. ") 
            else:        
                target = random.choice(players)
                while (target == thrower):
                    target = random.choice(players) 
        else:        
                target = random.choice(players)
                while (target == thrower):
                    target = random.choice(players)
        print("\n" + thrower + " is throwing a snowball at " + target + ".")
        hitNum = random.randint(1, 5)
        success = hitResult(hitNum)
        if (success == True):
            KO = random.randint(1, 2)
            if (KO == 1):
                print("It's a hit! " + target + " is obilterated!") 
                players.remove(target)
            else:
                print(target + " got hit, but will live!")
        else:
            print("Unfortunatley, " + thrower + " has horrible aim and missed.")
        time.sleep(2.8) 
    print(players[0] + " is better than everyone else.")  


def hitResult(hitNum):
    if (hitNum == 3):
        return True
    return False

main()
