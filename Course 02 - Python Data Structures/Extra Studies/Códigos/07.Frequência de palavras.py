def letter_frequency(string_file):
    """Takes a text file, or a string, splits
    the string, creates a dictionary and counts
    the frequency of words in the string.

    Then return the dictionary sorted.

    Arg: string_file: type(str): Receives a string.

    Returns: A dictionary sorted.

    """

    word_frequency = dict()
    letters = string_file.split()
    for w in letters:
        word_frequency[w] = word_frequency.get(w, 0) + 1

    sorted_count = dict()
    sorted_keys = sorted(word_frequency, key=word_frequency.get, reverse=True)
    for w in sorted_keys:
        sorted_count[w] = word_frequency[w]

    return sorted_count


def remove_words():
    """Creates a list of words."""

    stopwords_list = list()
    while True:
        word = input("Enter a word: \nTo stop enter 0")
        if word == "0":
            break
        else:
            if word not in stopwords_list:
                stopwords_list.append(word)

    return print(stopwords_list)
