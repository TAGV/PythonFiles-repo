#Count & String

#mystring = 'racadabiiiiaiiii'


def findsubstring(mystring,substring):
    print(f'Found substring "{substring}" at index : {mystring.find(substring)}')
    print(f'The total count of substring "{substring}" in string "{mystring}" is : {mystring.count(substring)}')

def find_reverse_substring(mystring,substring):
    reverse_string = mystring[::-1]
    print("================================================================================================")
    print(f'In Reversed string,found substring "{substring}" at index : {reverse_string.find(substring)}')
    print(f'In Reversed string,the total count of substring "{substring}" in string "{reverse_string}" is : {reverse_string.count(substring)}')



take_input = input("Enter any string of your choice...\n")
subs_tring = input("Enter the substring you need to find and get its count...\n")
print("================================================================================================")
findsubstring(take_input, subs_tring)
find_reverse_substring(take_input,subs_tring)


