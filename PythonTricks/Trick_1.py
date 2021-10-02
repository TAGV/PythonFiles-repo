#Merging dictionaries in a single line

dict_a = {'Arnold':'Terminator','Neo':'Matrix'}
dict_b = {'SRK':'KHNH','AK':'RDB'}
dict_c = {'test_1':1,'test_2':2}

dict_merge = {**dict_b,**dict_a,**dict_c}       #Merging Happens on this line

print(dict_merge)