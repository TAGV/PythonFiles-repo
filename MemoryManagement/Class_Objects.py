class Memory:
    pass



#Differnt class obj , diff references
act1 = Memory()
act2 = Memory()

#Same id
act3 = act1

print(id(act1))
print(id(act2))
print(id(act3))