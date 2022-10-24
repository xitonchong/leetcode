


def twoSum(list1, target):

    history = {}
    for i, _ in enumerate(list1):
        diff = target - list1[i]
        if diff in history:
            return [ history[diff], i ]
        history[list1[i]] = i



input1 = [2, 7, 11, 15]
answer1 = 9


assert twoSum(input1, answer1) == [0,1], print(twoSum(input1, answer1) )
assert twoSum([3,2,4], 6) == [1,2], print(twoSum([3,2,4], 6))