


def perfectSquares(n):
    i = 1
    lst = []
    while i*i <= n:
        lst.append(i*i)
        i+=1 

    toCheck = {n}
    cnt = 0
    while toCheck:
        #print(cnt)
        cnt += 1
        temp = set()
        print(toCheck)
        for x in toCheck:    
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp 
    
    #print(cnt)
    return cnt 

    




print(perfectSquares(12))
print(perfectSquares(22))