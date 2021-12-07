# Basic Dice Program Generator

import random

print("Welcome to the Basic Dice Program Generator!")

d6 = random.randint(1, 6)
d8 = random.randint (1, 8)
d10 = random.randint (1, 10)
d12 = random.randint (1, 12)

print('''
The dices have numbers, the numbers are 1 to 12.
The dice that have 12 numbers is called d12, so 
d6 = 1, 6 numbers
d8 = 1, 8 numbers
So, if you wish a dice with 8 numbers, write "d18" below.
Else, you type "N" and the program exits.

We have four dices, the dices are d6, d8, d10, d12
Enjoy. =]
        ''')

dice_value = str(input("Select the number of the dices (ex: d6, d8, d10, d12): "))

if dice_value == "d6":
    print ("The dices rolled is: ", d6)
elif dice_value == "d8":
    print ("The dices rolled is: ", d8)
elif dice_value == "d10":
    print ("The dices rolled is: ", d10)
elif dice_value == "d12":
    print ("The dices rolled is: ", d12)
else:
    print("Finishing the program!")

print("Finish the program!")



