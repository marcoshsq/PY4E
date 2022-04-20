# Exercise 009 - Approving Loan
"""Write a program to approve the bank loan for the purchase of a house. Ask the value of the home, the buyer's salary and how many years he will pay.
The monthly installment cannot exceed 30% of the salary or else the loan will be denied."""

# First we ask some questions.
house_price = float(input("what is the price of the house: "))
salary = float(input("what is your salary: "))
years_loan = int(input("In how many years will the loan be made?: "))

# Calculate loan amount
installment_value = house_price / (years_loan * 12)  # Convert years to months

# If the criteria are met and the loan is approved
if installment_value < (salary * 0.30):
    print("The loan has been approved! ")
    print(f"The value of the installment is R${installment_value:.2f}")
    print(f"You must pay for {years_loan * 12} months")

# If the criteria isn't met and the loan isn't approved
elif installment_value >= (salary * 0.30):
    print("The loan was denied! ")
    print(f"The loan amount was {installment_value:.2f} and your salary is R${salary}")
    print("insufficient income!")

# In case the inputs are wrong
else:
    print("incorrect values")
