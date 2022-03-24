from random import randint
from time import sleep

victories = 0
while True:
    player = int(input("Enter a number betwenn 0 and 10 to play or 999 to stop: \n"))
    if player < 0:
        print("Enter a positive integer less than ten: ")
    elif player > 10 and player != 999:
        print("Enter an integer less than 10")
    elif player == 999:
        print("You decided to stop. I'm sorry I'm not so nice...(｡•́︿•̀｡)")
        print(f"Consecutive wins: {victories}")
        break
    else:
        computer = randint(0, 10)
        choice = str(input("Even or odd? [E / O] \n")).strip().upper()
        if choice == "E":
            print("You chose even!")
            sum = player + computer
            if sum % 2 == 0:
                victories += 1
                sleep(1)
                print(f"The computer chose {computer}.")
                print(f"{sum} it's even, so you've won!")
            else:
                sleep(1)
                print(f"The computer chose {computer}.")
                print(f"{sum} it's odd, so you've loose!")
                print(f"Consecutive wins: {victories}")
                break
        elif choice == "O":
            sum = player + computer
            print("You chose odd!")
            if sum % 2 != 0:
                victories += 1
                sleep(1)
                print(f"The computer chose {computer}.")
                print(f"{sum} it's odd, so you've won!")
            else:
                sleep(1)
                print(f"The computer chose {computer}.")
                print(f"{sum} it's even, so you've loose!")
                print(f"Consecutive wins: {victories}")
                break
        else:
            print("Please choose Even or odd!")
            sleep(1.5)
            print("Please (づ｡◕‿‿◕｡)づ")
            sleep(1)
