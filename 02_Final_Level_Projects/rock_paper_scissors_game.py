from random import randint
import time

itens = ("Rock", "Paper", "Scissors")
pc_choice = randint(0, 2)

print("-=" * 10, "Rock, Paper ou Scissors", "-=" * 10)
print(
    """
                         [0] Rock
                         [1] Paper
                         [2] Scissors
"""
)

print("-=" * 33)


player_choice = int(input("What's your move (Choose between 0, 1 and 2): "))

print("JO")
time.sleep(1)
print("KEN")
time.sleep(1)
print("PO")
time.sleep(1)

print(f"Python chose {itens[pc_choice]}")
print(f"You chose {itens[player_choice]}")

if pc_choice == 0:  # Python chose rock
    if player_choice == 0:
        print("it's a tie")

    elif player_choice == 1:
        print("You win!")

    elif player_choice == 2:
        print("You loose!")

    else:
        print("Invalid Move")

if pc_choice == 1:  # Python chose paper
    if player_choice == 0:
        print("You loose!")
    elif player_choice == 1:
        print("it's a tie")

    elif player_choice == 2:
        print("You win!")

    else:
        print("Invalid Move")

if pc_choice == 2:  # Python chose scissors
    if player_choice == 0:
        print("You win!")
    elif player_choice == 1:
        print("You loose!")

    elif player_choice == 2:
        print("it's a tie")

    else:
        print("Invalid Move")
