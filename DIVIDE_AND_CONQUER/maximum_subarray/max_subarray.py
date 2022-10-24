



def maxSubarray(arr):
    ''' break down the problem in half: such that...
    left = [0, mid of array] 
    right = [mid of array, right]
    cross = [left, right]

    '''

    def cross_merge(nums, left, mid, right):
        left_total = float("-inf")
        cross_sum = 0
        for i in range(mid, left-1, -1):
            cross_sum += nums[i]
            left_total = max(left_total, cross_sum)

        left_total = left_total if left_total != float("-inf") else 0

        right_total = float("-inf")
        cross_sum = 0
        for i in range(mid+1, right+1):
            cross_sum += nums[i]
            right_total = max(right_total, cross_sum)

        right_total = right_total if right_total != float("-inf") else 0
        
        return left_total + right_total
            

    def merge(nums, left, right):
        if left == right:
            return nums[left]
        mid = left + (right-left)//2
        left_sum = merge(nums, left, mid)
        right_sum = merge(nums, mid+1, right)
        cross_sum = cross_merge(nums, left, mid, right)
        return max(left_sum, right_sum, cross_sum)

    
    result = merge(arr, 0, len(arr)-1)
    print(arr, ' -> ', result )
    return  result



''' this has the time complexity of O(n)
    Each call takes O(1) and there are N calls, thus'''


assert maxSubarray([-2,1,-3,4,-1,2,1,-5,4]) == 6 
assert maxSubarray([-2, 1, 3, -2]) == 4