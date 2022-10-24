
def combs(n, k, path, res):
    if len(path) == k:
        res.append(path[:])
        return 

    for i in range(len(n)):
        combs(n[i+1:], k, path+[n[i]], res)

    return 





k = 2

res = []
combs([1,2,3], k, [], res )
print(res)
assert res == [[1,2], [1,3], [2,3]] 