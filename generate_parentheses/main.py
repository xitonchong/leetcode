


def generateParenthesis(n):

    # genreate different patterns of bracket with valid syntax
    def dfs(cur, open_no, close_no):
        res = []

        #close condition
        if open_no == 0 == close_no:
            return [cur]

        if open_no:
            res.extend(dfs(cur+'(', open_no-1, close_no+1))

        if close_no:
            res.extend(dfs(cur+')', open_no, close_no-1))

        return res

    arr = dfs('', n, 0)
    print(arr)
    return arr


assert generateParenthesis(3) == ['((()))', '(()())', '(())()', '()(())', '()()()']