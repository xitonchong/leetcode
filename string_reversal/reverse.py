
def reverseString(string):
    if len(string) == 0: # stop condition
        return ""

    return reverseString(string[1:]) + string[0]

string ="helllow"


result = reverseString(string)
print(result)