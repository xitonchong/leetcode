
from typing import List

def fourSum(nums: List[int], target: int) -> List[List[int]]:
    return dfs([], nums, [False]*len(nums), [], target)
    
    
    
def dfs(mylist, nums, visited, res, target):
    
    if len(mylist) == 4 and (sum(mylist) == target):
        mylist = sorted(mylist[:])
        if mylist in res:
            return 

        res.append(mylist[:]) # [:] to return deep copy
        return 
    
    for i, no in enumerate(nums):
        if visited[i]:
            continue
        visited[i] = True # mark it as visited 
        mylist.append(no)

        dfs(mylist, nums, visited, res, target)
        
        # unmark it as visited 
        visited[i] = False
        mylist.pop()
        
    return res


input1 = [1,0,-1,0,-2,2, 3, -3]
print(fourSum(input1, 0))