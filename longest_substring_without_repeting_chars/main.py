

# Python3 program to find and print longest
# substring without repeating characters.
 
# Function to find and print longest
# substring without repeating characters.
def findLongestSubstring(string):
    st = 0
    history = {}
    history[string[st]] = 0
    n = len(string)
    max_length = 0

    for idx in range(1,n):
        # if char no in history
        if string[idx] not in history:
            #print(string[idx])
            history[string[idx]] = idx
        else:
            #char in history
            if history[string[idx]] > st: # if the history index is after our st
                 

                length = idx - st
                if length > max_length:
                    start = st
                    max_length = length
                st = history[string[idx]] + 1
            history[string[idx]] = idx

    if max_length < idx - st:
        max_length = idx  - st
        start = st

    return string[start: start + max_length-1]
 
# Driver Code
if __name__ == "__main__":
 
    string = "GEEKSFORGEEKS"
    string = "HAPPYBIRTHDAY"
    print(findLongestSubstring(string))
