#Generator example 1
import string


def alphabets():
    for n in string.ascii_lowercase:
        print(n,end=" ")


alphabets()
print()
print("========================")

def alphabets_gen():
    for n in string.ascii_uppercase:
        yield n

print(alphabets_gen())
for it in alphabets_gen():
    print(it,end=" ")