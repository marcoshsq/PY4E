# Exercise 053 - Palindrome Detector

"""Create a program that reads any sentence and tells if it is a palindrome, 
disregarding the spaces."""

"""A palindrome is a word, phrase, or number that remains 
the same when read backwards. e.g.: Apos a sopa, A sacada da casa, A torre da derrota,
 o lobo ama o bolo, Anotaram a data da maratona, e etc."""


# 1. First we ask the user input for a sentece, and just to make things easier
# We remove any spaces with strip, and put all im caps with upper
phrase_original = str(input("Enter a sentence: ")).upper().strip()

# 2. Then let's break the sentence into words with split
splitted_words = phrase_original.split()

# 3. Now we put everything together, forming a text block with the join function
rearranged_sentence = "".join(splitted_words)

# 4. Now let's create a backwards version of our sentence for comparison
backwards_sentence = ""

# 5. We will use for to reorder the sentence in reverse.
for i in range(len(rearranged_sentence) - 1, -1, -1):
    backwards_sentence += rearranged_sentence[i]

print(
    f"The sentence {rearranged_sentence} When read in reverse is {backwards_sentence}"
)

# 6. And finally an if statement to say whether or not the sentence is a palindrome
if rearranged_sentence == backwards_sentence:
    print("The phrase is a palindrome")
else:
    print("The phrase isn't a palindrome")


# Another way to do this exercise without the for loop, just using string slicing

phrase_original = str(input("Enter a sentence: ")).upper().strip()
splitted_words = phrase_original.split()
rearranged_sentence = "".join(splitted_words)
backwards_sentence = rearranged_sentence[::-1]
print(
    f"The sentence {rearranged_sentence} When read in reverse is {backwards_sentence}"
)
if rearranged_sentence == backwards_sentence:
    print("The phrase is a palindrome")
else:
    print("The phrase isn't a palindrome")
