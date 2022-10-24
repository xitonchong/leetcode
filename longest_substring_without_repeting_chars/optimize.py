


def findLongestSubstring(string):
    l = 0
    # use sliding window approach
    max_length = 0
    history = {}
    for r in range(len(string)):
        
        if (string[r] in history) and (l <= history[string[r]]):
            l = history[string[r]]+1 
        history[string[r]] = r
        current_length  = r - l + 1

        
        if max_length < current_length:
            max_length = current_length
            best_l = l 
            best_r = r + 1


    return len(string[best_l: best_r]), string[best_l: best_r]  #max_length
        


if __name__ == "__main__":
 
    string = "GEEKSFORGEEKS"
    #string = "HAPPYBIRTHDAY"
    print(findLongestSubstring(string))
