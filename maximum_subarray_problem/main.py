

def max_subarray(list1):

    start = 0
    end = len(list1)
    max_sum = 0
    current_sum = 0
    best_start, best_end = 0 ,0 

    for idx, num in enumerate(list1):
        end = idx
        current_sum += num
        if current_sum < 0:
            start = end + 1
            current_sum  = 0


        if current_sum > max_sum:
            max_sum = current_sum
            best_start = start
            best_end = end+1

    return max_sum, best_start, best_end

input1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, start, end = max_subarray(input1)


print(max_sum, start, end, input1[start:end])