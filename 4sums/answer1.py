
#https://leetcode.com/problems/4sum/discuss/1341243/Python-O(n3)-and-why-we-can-not-do-better-explained



def fourSum( nums, target):
    nums.sort()
    n, ans = len(nums), []
    for i in range(n):
        for j in range(i + 1, n):
            goal = target - nums[i] - nums[j]
            beg, end = j + 1, n - 1

            while beg < end:
                if nums[beg] + nums[end] < goal:
                    beg += 1
                elif nums[beg] + nums[end] > goal:
                    end -= 1
                else:
                    ans.append((nums[i], nums[j], nums[beg], nums[end]))
                    beg += 1
                    end -= 1

    return set(ans)

# sets are hashable but not lists

input1 = [1,0,-1,0,-2,2]
print(fourSum(input1, 0))