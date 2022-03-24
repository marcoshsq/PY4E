# Exercise 073 - Tuples with Soccer Teams

"""Create a tuple filled with the top 20 of the Brazilian Football Championship Table,
in order of placement. Then show:

a) The first 5 teams.
b) The last 4 placed.
c) Teams in alphabetical order.
"""


teams = (
    "América-MG",
    "Athletico-PR",
    "Atlético-GO",
    "Atlético-MG",
    "Internacional",
    "Juventude",
    "Palmeiras",
    "Santos",
    "São Paulo",
    "Corinthians",
    "Coritiba",
    "Cuiabá",
    "Flamengo",
    "Fluminense",
    "Fortaleza",
    "Goiás",
    "Avaí",
    "Botafogo",
    "Bragantino",
    "Ceará",
)

print("-=" * 15)
print(f"{'Brazilian Championship classification'}")
print("-=" * 15)
print(f"The first 5 teams are {teams[0:5]}")  # a)
print("-=" * 15)
print(f"The last 4 placed are {teams[-4:]}")  # b)
print("-=" * 15)
print(f"Teams in alphabetical order {sorted(teams)}")  # c)
print("-=" * 15)
print("END")
