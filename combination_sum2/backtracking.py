

def combination_sum2(candidates, target):
    res = []
    nums = sorted(candidates) # takes O(n)
    backtracking(nums, 0, target, [], res)
    print(f"candidates: {candidates} , target:  {target}, result: {res}")
    return res 


def backtracking(nums, index, diff, path, res):
    if diff < 0:
        return 
    
    if diff == 0:
        res.append(list(path))
        return 

    for i in range(index, len(nums)):
        if i != index and nums[i-1] == nums[i]:
            continue # only allows same number to backtrack during the start index 
        path.append(nums[i])  
        backtracking(nums, i+1, diff-nums[i], path, res)
        path.pop() # backtracking 




input1 = [2,3,6,7]
target1 = 12

''' each number in the candidates may only be used once in the combinations
the solution set must not contain duplicate combinations''' 

result = combination_sum2(input1, target1)

