# Isaac St Hubert Module 3.2 12/21/2025
# This program alters the original chohan program to include a bonus rule

"""Cho-Han, by Al Sweigart al@inventwithpython.com
The traditional Japanese dice game of even-odd.
View this code athttps://nostarch.com/big-book-small-python-projects
Tags: short, beginner, game"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, by Al Sweigart al@inventwithpython.com

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

BONUS RULE:
If the total of the dice roll is 2 or 7, you receive a 10 mon bonus!
''')  # Adds a description of the bonus to the introduction

purse = 5000
while True:
    
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        # Changes input prompt to initials
        pot = input('IS: ')
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            
            pot = int(pot) 
            break  

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    # Sums up the total used to determine bonus
    total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor, still covering the')
    print('dice and asks for your bet.')
    print()
    print('    CHO (even) or HAN (odd)?')


    while True:
        bet = input('IS: ').upper()
        if bet != 'CHO' and bet != 'HAN':
            print('Please enter either "CHO" or "HAN".')
            continue
        else:
            break


    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)


    # Checks for bonus
    if total == 2 or total == 7:
        print('Bonus! The dice total was', total, 
              '— you receive a 10 mon bonus!')
        purse += 10


    rollIsEven = total % 2 == 0
    if rollIsEven:
        correctBet = 'CHO'
    else:
        correctBet = 'HAN'

    playerWon = bet == correctBet


    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        # Add house_fee to calculate 12%
        house_fee = pot * 12 // 100
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')


    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
