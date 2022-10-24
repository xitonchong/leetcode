
from typing import List 

def dfs(perm, nums, visited, res):

    # specify stop condition
    if len(nums) == len(perm):
        res.append(perm[:]) #[:] returns a deepcopy
        return 

    for i, no in enumerate(nums):
        if visited[i]:
            continue

        visited[i] = True 
        perm.append(no)

        dfs(perm, nums, visited, res)

        visited[i] = False
        perm.pop()
    return res

nums = [1,2,4]

result = dfs([], nums, [False]*len(nums), [])# result is list to append
print(result)


