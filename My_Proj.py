def game(mine, comp):
    print(f"You chose {mine} and the computer chose {comp}")
    if mine == comp:
        print("It's a draw!")
    elif mine == "sissors" and comp == "paper":
        print("You win!")
    elif mine == "paper" and comp == "rock":
        print("You win!")
    elif mine == "rock" and comp == "sissors":
        print("You win!")
    else:
        print("You lose! :(")

import random
while True:
    choice = ("sissors",'paper','rock')
    comp = random.randint(0,2)
    comp = choice[comp]
    mine = input("Rock, Paper, Sissors!\nselect one!\n").lower()
    game(mine,comp)
    qn = input("\nDo you want to play another time? [y]/n ")
    if qn == "n":
        break