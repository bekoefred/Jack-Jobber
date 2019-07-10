import random
import time

roll_again = "YES"

while roll_again =="yes" or roll_again =="y" or roll_again =="Y" or roll_again =="YES":
     print("\nRolling the Dice again....")


time.sleep(1)

dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

print("The Values are::")

print("Dice 1 = dice1", "\nDice 2 = dice2")

if dice1 == dice2:
    print("Your Roll Results in Double")
else:
    print("Roll again")
roll_again = input("\nRoll the dice again? (Y/N)")