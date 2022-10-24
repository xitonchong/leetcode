# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.

from typing import List

def canJump(nums: List[int]) -> bool:
    result = dfs(nums, 0,  hashes=len(nums)*[False] )
    print(nums, result)
    return result 


def dfs(nums, idx, hashes):
    if idx >= len(nums) -1:
        return True


    if hashes[idx]:
        return False 

    for i in range(nums[idx], 0, -1):
        jump = i + idx 
        if dfs(nums, jump, hashes):
            return True 
        jump -= i 

    hashes[idx] = True
    return False 



nums = [2,3, 1, 1, 4]
assert canJump(nums) == True 

nums = [3,2,1,0, 4]
assert canJump(nums) == False 
