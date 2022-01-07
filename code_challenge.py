words = [
    "Ferrari","Acura", "Ford", "Ferrari", "Honda", "Nissan","Datsun"
]

letters = [
    "a", "f", "r", "r", "e", "i", "o", "h", "c", "s", "u", "w", "a", "n", "d",
]



def charCount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    #print(dict)
    return dict


def possible_words(lwords, charSet):
    for word in lwords:
        #print(word)
        flag = 1
        chars = charCount(word) # Created a dictionary of the word
        #print(chars)

        for key in chars:       # Iterate over a single dictionary
            if key.lower() not in charSet: # Ignore the case
                flag = 0
            else:
                #print("Count of letters : ",charSet.count(key))
                #print(chars[key])
                if charSet.count(key) != chars[key]:
                    flag = 1
        if flag == 1:
            print(word)


possible_words(words, letters)



