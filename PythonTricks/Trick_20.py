# Removing Empty Lists from a List

mylist = [1, 2, 3, 4, [], [], "", 6, 7, ""]

# 1st Method

# new_list = list(filter(None,mylist))                # [1, 2, 3, 4, 6, 7]
# new_list = list(filter(lambda x:x,mylist))           # [1, 2, 3, 4, 6, 7]
# new_list = list(filter(lambda x:x==[],mylist))          #[[], []]
# new_list = list(filter(lambda x:x=='',mylist))          #['']
new_list = list(filter(lambda x: not x, mylist))  # [[], [], '']
print(new_list)

# 2nd Method

# nlist = [x for x in mylist]                         #[1, 2, 3, 4, [], [], '', 6, 7, '']
# nlist = [x for x in mylist if x]                        #[1, 2, 3, 4, 6, 7]
# nlist = [x for x in mylist if not x]                    #[[], [], '', '']
# nlist = [x for x in mylist if x == ""]                  #['', '']
nlist = [x for x in mylist if x == []]  # [[], []]
print(nlist)
