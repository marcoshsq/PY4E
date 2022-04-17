# Extra Exercise 009

"""João, a good man, bought a computer to monitor the daily income of his work.

Every time he brings in a weight of fish greater than that established by the state fishing regulations (50 kilos) he must pay a fine of R$4.00 per excess kilo.

João needs you to write a program that reads the variable weight (weight of fish) and calculates the excess.

Record in the excess variable the amount of kilos beyond the limit and in the fine variable the amount of the fine that João must pay.
Print the program data with the appropriate messages."""

# For each kg above the established 50kg, a fine of R$4.00 per excess kg;
# Create a program that reads the amount of fish in kg and says the surplus;
# Create a variable that receives the extra value;
# Calculate the amount of the fine.

peso = float(input("Enter the number of kilograms of fish: "))
if peso > 50:
    excedente = peso - 50
    multa = excedente * 4
    print(f"You have {excedente}kg more than allowed")
    print(f"The amount of the fine is R${multa}")
elif peso <= 50:
    print("Quantity within the allowed")
else:
    print("Nothing")
