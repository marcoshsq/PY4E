# Exercise 083 - Validating Math Expressions

"""Create a program where the user types any expression that uses parentheses. 
Your application should analyze whether the passed expression has 
the open and closed parentheses in the correct order."""

list_exp = []
exp = str(input("Enter an expression: \n"))

for symbol in exp:
    if symbol == "(":
        list_exp.append(symbol)

    elif symbol == ")":
        if len(list_exp) > 0:
            list_exp.pop(-1)

        else:
            list_exp.append(")")
            break

if len(list_exp) == 0:
    print("Valid")
else:
    print("Invalid")
