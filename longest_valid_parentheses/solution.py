
''' use stack concept to store each right bracket 
    length = left bracket - right bracket index
''' 


def longestValidParentheses( s: str) -> int:
    
    stack = [ [')', -1]] # cannot right bracket start first
    max_length = 0
    for idx, cur_p in enumerate(s):
        if (cur_p == ')') and (stack[-1][0] == '('):
            stack.pop()
            # update the max length
            max_length = max(max_length, idx - stack[-1][1])
            # if count total of valid parentheses without consecutive
            #max_length += 2
        else: 
            stack.append([cur_p, idx])
    return max_length 



print(longestValidParentheses('(()((())'))