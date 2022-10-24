
from typing import List 
from collections import Counter

def permuteUnique(nums):
    result = []

    def dfs(built, counter):
        if len(built) == len(nums):
            result.append(built[:]) #deecopy or list(built)
            return 

        for num in counter:
            if counter[num] > 0:
                built.append(num)
                counter[num] -= 1
                dfs(built, counter) # cannot pass built.append(num) into function

                counter[num]+=1
                built.pop() 


    
    dfs([], Counter(nums))
    print(nums, ' -> ', result)
    return result

permuteUnique([1,2,1])

permuteUnique([2, 5, 1])