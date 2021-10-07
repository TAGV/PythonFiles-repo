#Check if the string is palindrome

def checkPalindrome(input_string):
    result = input_string.find(input_string[::-1])==0       #checks every index, if same it equates it to zero,returns true
    return result


while True:
    userinput = input("Enter the string if it is a palindrome\n")
    ispalindrome = checkPalindrome(userinput)
    if ispalindrome == True:
        print("Its a Palindrome")
        break
    else:
        print("Nope,Its not a Palindrome")
        continue