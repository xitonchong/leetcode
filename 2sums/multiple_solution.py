from typing import List 

def twoSum(nums: List[int], target: int) -> List[int]:
    n = len(nums)
    
    #nums = sorted(nums) # DO NOT PUT SORTED HERE!
    # l = 0
    # r = n
    solution = []
    
    for l in range(n):
        for r in range(l+1, n):
            if (nums[l] + nums[r] == target):
                solution.append([l,r])
                print(nums[l] + nums[r])
                
    return solution



testcase = [2, 7, 11, 15]


# return the indices that total to the target 
input1 = [2, 7, 11, 15]
answer1 = 9


#assert twoSum(input1, answer1) == [[0,1]], print(twoSum(input1, answer1) )
assert twoSum([3,2,4], 6) == [[1,2]], print(twoSum([3,2,4], 6))