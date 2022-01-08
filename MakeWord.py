words = [
    "reroari","Acura", "Ford", "Ferrari", "Honda", "Nissan","Datsun"
]

letters = [
    "a", "f", "r", "r", "e", "i", "o", "h", "c", "s", "u", "w", "a", "n", "d"
]



def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i,0) + 1

    return dict


def possible_words(lwords, charSet):
    for word in lwords:

        flag = 1
        chars = charCount(word) # Created a dictionary of the word

        for key in (chars):                                                                      # Iterate over a each word dictionary
            if (key.lower() in charSet) and (chars[key] <= charSet.count(key.lower())):          # Ignore the case and check if letter is present
                flag = 1
            else:
                flag = 0
                break

        if flag == 1:
            print(word+" = Spelled")
        else:
            print(word+" = Not Spelled")



possible_words(words, letters)



