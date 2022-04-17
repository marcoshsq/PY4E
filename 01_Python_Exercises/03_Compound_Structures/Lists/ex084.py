# Exercise 084 - Composite List and Data Analysis

"""Make a program that reads the name and weight of several people, 
keeping everything in a list. At the end, show:

A) How many people were registered.
B) A list with the heaviest people.
C) A list with the lightest people.
"""

sec_list = list()
main_list = list()
heavy = light = 0


while True:
    sec_list.append(str(input("Please, enter your name: \n")))
    sec_list.append(float(input("Please, enter your weight: \n")))
    question = str(input("Wish to continue: [Yes] or [No]\n")).upper().strip()
    if len(main_list) == 0:
        heavy = light = sec_list[1]
    else:
        if sec_list[1] > heavy:
            heavy = sec_list[1]
        if sec_list[1] < light:
            light = sec_list

    main_list.append(sec_list[:])
    sec_list.clear()

    if question[0] in "Nn":
        print("Process finished...")
        break
    else:
        continue

print(f"Number of registered people: {len(main_list)}\n")
print(f"The greatest weight was {heavy}kg ")
for i in main_list:
    if i[1] == heavy:
        print(f"{i[0]}", end=" ")

print(f"The lowest weight was {light}kg \n")
for j in main_list:
    if j[1] == light:
        print(f"{j[0]}", end=" ")
