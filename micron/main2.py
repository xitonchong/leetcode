nums = [ -2, 1, -3, 4, -1, 2, 1, -5, 4]
nums = [-2, -3, 4, -5]


current_sum = 0
largest_sum = 0
for index, value in enumerate(nums):
    current_sum = max(value + current_sum, 0)
    largest_sum = max(current_sum, largest_sum)

print(largest_sum)


'''properties: if summation of current_sum and value < 0, the next positive integer is always preferred'''
# get the index for the start and end index
current_sum = 0
largest_sum = 0
for index, value in enumerate(nums):
    if value + current_sum > 0:
        current_sum += value
    else:
        current_sum = 0
        cur_index = index + 1
    
    if current_sum > largest_sum:
        largest_sum = current_sum
        index_end = index
        start_index = cur_index

print(largest_sum, start_index, index_end)






