

def isPalindrome(string):
    if (len(string) == 0) | (len(string) == 1):
        return True
    
    if string[0] == string[-1]:
        return isPalindrome(string[1:-1])

    return False



list_string = ["kayak", "pokemon"]

for string in list_string:
    print(isPalindrome(string))