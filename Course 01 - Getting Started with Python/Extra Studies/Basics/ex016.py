import math

# Extra Exercise 012

"""Make a Program for a paint shop:

The program should ask for the size in square meters of the area to be painted. 
Assume that the paint coverage is 1 liter for every 6 square meters and that the paint is sold in 18 liter gallons,
that cost R$ 80.00 or in cans of 3.6 liters, which cost R$ 25.00.

Inform the user of the quantities of ink to be purchased and the respective prices in 3 situations:

a) buy only 18 liter gallons;
b) buy only 3.6 liter cans;
c) mix cans and gallons, so that paint waste is less.

Add 10% clearance and always round the values up, ie, consider full cans."""

# 1. We create our variables, storing the values of the utterance
square_meter_per_liter = 6
gallon_price = 80
liters_gallon = 18
can_price = 25
liters_can = 3.6
safety_margin = 1.1

# 2. We ask how many square meters will be painted
square_meter = float(input("inform the amount of square meters (m²) to be painted:"))

# 3. We define how much paint will be consumed per square meter with the safety margin
consumption_liter = square_meter / square_meter_per_liter * safety_margin

# 4. For 18L gallons only
only_gallons = math.ceil(consumption_liter / liters_gallon)
only_gallons_price = only_gallons * gallon_price

# 5. For 3.6L cans only
only_cans = math.ceil(consumption_liter / liters_can)
only_cans_price = only_cans * can_price

# 6. Mixing cans and gallons
mixed_gallons_qty = consumption_liter // liters_gallon
mixed_cans_qty = math.ceil(
    (consumption_liter - mixed_gallons_qty * liters_gallon) / liters_can
)
mixed_gallons_price = mixed_gallons_qty * gallon_price
mixed_cans_price = mixed_cans_qty * can_price

# 7. We print everything
print("-=" * 10)
print(f"Paint consumption is: {consumption_liter:.2f} Liters")
print("-=" * 10)
print(f"The quantity of 18 liter gallons to be used is: {only_gallons:.0f}L")
print(f"The total value of 18 liter gallons is: R${only_gallons_price:.2f}")
print("-=" * 10)
print(f"The quantity of 3.6 liter cans to be used is: {only_cans:.0f}")
print(f"The total value of 3.6 liter cans is: R${only_cans_price:.2f}")
print("-=" * 10)
print("Considering the smallest waste of paint, we have:")
print(f"Quantity of gallons: {mixed_gallons_qty:.0f}")
print(f"Quantity of cans: {mixed_cans_qty:.0f}")
print(f"Mixed total amount: {mixed_gallons_qty + mixed_cans_qty:.0f}")
print(
    f"And the total value considering gallons and cans is: R$ {mixed_gallons_price + mixed_cans_price:.2f}"
)
