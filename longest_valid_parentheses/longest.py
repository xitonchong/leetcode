


def longestValidParentheses( s: str) -> int:

    print(dfs(s, len(s), 0, 0))
    
    
def dfs(s, length,  n, res):
    if n + 1 <= length:
        return s
    
    if (s[0] == '(') and (s[1] == ')'):
        res += 2 # left and right
        s = s[2:]
        n+=1 
        print(n, s, res)
        return s


    for c in dfs(s[1:], length, n+1, res):
        print('c ', c)
        if c == s[0]:
            res += 2
    return res 



longestValidParentheses('((())')