words = [
    "Acura", "Ford", "Ferrari", "Honda", "Nissan", "Datsun",
]

letters = [
    "a", "f", "r", "r", "e", "i", "o", "h", "c", "s", "u", "w", "a", "n", "d",  # noqa
]

def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
#word_dictionary = {}

def can_it_be_spelled(word_list,letter_list):
    """
    Function to determine if the provided word can be spelled using the
    provided letters
      - Evaluation will ignore case
      - Each instance of the provided letters can only be used once
        (e.g. If there aren't enough a's then the word can't be spelled)
    """
    # Loop to check for each word in the given word list
    for word in word_list:

        flag = 1

        # Create a dictionary of each word from the "words" list
        word_dictionary = charCount(word)

        # Iterate over a each word in the word dictionary(using the key)
        # Condition 1 : Ignore the case and check if letter is present in the list of letters
        # Condition 2 : Check if value of each letter in dictionary is less than equal to
        #               frequency of the corresponding letter in letter list

        for key in (word_dictionary):
            if (key.lower() in letter_list) and (word_dictionary[key] <= letter_list.count(key.lower())):
                flag = 1
            else:
                flag = 0
                break

        # If flag is true, then word can be spelt using the set of letters.
        # If flag is false, then word cannot be spelt using the set of letters.
        if flag == 1:
            print(word+" = Spelled")
        else:
            print(word+" = Not Spelled")



if __name__ == "__main__":
    """
    Instructions:
    Iterate over the provided words and print whether each one
    can be spelled or not using the available letters.  Letters can be reused
    between words, but may only be used once within a word.
    """
    can_it_be_spelled(words,letters)
