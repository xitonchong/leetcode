nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
largest = -9999999
#sum1 = 0

for index, value in enumerate(nums):
    sum1 = value
    # store number in sum1
    for index2, value2 in enumerate(nums):
        if index2 <= index:
            print(f"index 2 is more than index 1")
            continue
        print(f"here is value 1: {value}")
        if index == index2:
            continue
        else:
            sum1 += value2
            print(value2)
            if sum1 > largest:
                largest = sum1



print(largest)