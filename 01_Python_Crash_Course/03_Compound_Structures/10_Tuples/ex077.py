# Exercise 077 - Counting Vowels in Tuple

""" Create a program that has a multi-word tuple (don't use accents).
After that, you must show, for each word, what its vowels are."""

words = (
    "gruesome",
    "beds",
    "well-made",
    "embarrassed",
    "income",
    "love",
    "smoke",
    "middle",
    "cold",
    "voiceless",
    "various",
    "icy" "long-term",
    "slave",
    "young",
    "steep",
    "flaky",
    "fry",
    "crayon",
    "announce",
    "agonizing",
    "add",
    "gun",
    "stove",
)

for i in words:
    print(f"\nIn the word {i.upper()} we have ", end="")
    for j in i:
        if j.lower() in "aeiou":
            print(f"{j.upper()}", end=" ")
