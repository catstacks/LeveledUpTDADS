# dice.py file
import random

def dice_roll(sides):
    roll = random.randint(1, sides)
    print('You rolled a', roll)   
    roll_again = str(input('Would you like to roll again? Please enter Y or N to continue: '))
    while roll_again == 'Y' or roll_again == 'y' or roll_again == 'yes'  or roll_again == 'YES':
        return dice_roll(sides)
    print('Thanks for playing!')