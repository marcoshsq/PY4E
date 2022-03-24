# Exercise 076 - Tuple Price List

"""Create a program that has a single tuple with product 
names and their respective prices, in sequence. At the end, 
show a price listing, organizing the data in tabular form.
"""

product_list = (
    "Caderno",
    7,
    "Lápis",
    3,
    "Borracha",
    0.75,
    "Canetas",
    1.50,
    "Apontador",
    2.50,
    "Réguas",
    3,
    "Papel Sulfite",
    7,
    "Mochila",
    55,
    "Calendário",
    15,
    "Livros",
    155,
    "Notebook",
    2500,
    "Agenda",
    25,
)

print("=" * 39)
print(f"{'PRICE TABLE'}:^40")
print("=" * 39)

for i in range(0, len(product_list)):
    if i % 2 == 0:
        print(f"{product_list[i]:.<30}", end="")
    else:
        print(f"R$ {product_list[i]:>7.2f}")
print("=" * 39)
