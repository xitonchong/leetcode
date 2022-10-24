


def isValid(string):
    maps = {'}': '{', ']': '[', ')': '('}
    stack = []
    for char in string:
        # if stack is not empty and char in maps and last stack is in maps
        if stack and (char in maps) and (stack[-1] == maps[char]):
            # here deals with closing bracket only
            #print(char, char in maps)
            stack.pop()
        else:
            stack.append(char)
        
    # stack need to be empty for true
    print(string, not stack)
    return not stack



assert isValid("()[]{}") == True 
assert isValid("()[[]{}") == False