import itertools

counter = 0
for perm in itertools.permutations("ABCD"):
    print(perm)
    counter += 1

print("Total permutations of the string = ",counter)