'''Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers
 sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times.
 Two combinations are unique if the frequency of at least one of the chosen 
 numbers is different.

It is guaranteed that the number of unique combinations that sum up to target 
is less than 150 combinations for the given input.'''


def combinationSum(input1, target):
    result = []
    dfs(input1, target, [], result)
    print(f"{input1}: target: {target} -> {result}")
    return result 

def dfs(nums, target, path, result):
    if target < 0:
        return

    if target == 0:
        result.append(path[:])
        return 

    
    # we allow repetiive input, so no need to use hasmap
    for i in range(len(nums)):
        dfs(nums[i:], target - nums[i],  path+[nums[i]], result )



input1 = [2,3,6,7]
target1 = 12



result = combinationSum(input1, target1)