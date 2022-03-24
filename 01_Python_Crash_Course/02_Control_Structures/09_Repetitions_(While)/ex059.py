# Exercise 059 - Creating an Options Menu

"""Create a program that reads two values and displays a menu on the screen:
[ 1 ] sum
[ 2 ] multiply
[ 3 ] bigger
[ 4 ] add new numbers
[5] exit the program
Your program should perform the requested operation in each case."""

# Since this is going to be a "big" program, let's create a script.
# 1. We create our menu, and display it
# 2. We create the logic of our loop
# 3. The user input
# 4. If he chose 1
# 5. If he chose 2
# 6. If he chose 3
# 7. If he chose 4
# 7. If he chose 5

# ....

# 1. Let's display our menu
# 2. Since we want it to be repeated, the menu will be indented in the loop
flag = 0
while flag != 1:
    print("=" * 5, "Simple Calculator!", "=" * 5)
    value_01 = int(input("Enter a value: "))
    value_02 = int(input("Enter another value: "))
    print("=" * 25)
    print("[ 1 ] sum")
    print("[ 2 ] multiply")
    print("[ 3 ] bigger")
    print("[ 4 ] add new numbers")
    print("[ 5 ] exit")
    print("=" * 25)

    # 3. Now the user choice
    choice = int(input("Enter your option: "))

    # 4. Now start the menu choices

    # 5. If he chose 1
    if choice == 1:
        sum = value_01 + value_02
        print(f"The sum between {value_01} and {value_02} is {sum}")

    # 6. If he chose 2
    elif choice == 2:
        product = value_01 * value_02
        print(f"The product from {value_01} and {value_02} is {product}")

    # 7. If he chose 3, we'll ident again, to see which value is greater than
    elif choice == 3:
        if value_01 > value_02:
            print(f"Betwenn {value_01} and {value_02}, the bigger is {value_01}")
        elif value_01 < value_02:
            print(f"Betwenn {value_01} and {value_02}, the bigger is {value_02}")
        else:
            print("The values are the same!")

    # 8. Chose 4, we star the loop again
    elif choice == 4:
        continue

    # 9. We add to our flag, and stop the loop
    elif choice == 5:
        flag += 1

    # 10. If the user input a different number than the options available
    else:
        print("Wrong data, try again: ")
        continue

# Note, we didn't learn how to deal with errors, and this final else will only
# work for numbers, not strings, we'll learn later about the try except command
