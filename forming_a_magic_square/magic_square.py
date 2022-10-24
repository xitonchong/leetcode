from itertools import permutations
import numpy as np 


arr = [[5,3,4], [1,5,8], [6,4,2]]
flatten_arr = [x for row in arr for x in row]

#print(flatten_arr)
possible_permutations = permutations(range(1,10))

#print(possible_permutations)

lowest_cost = 99999999

for perm in possible_permutations:
    # possible square constraints
    magic_constant = sum(perm[0:3])
    diagonal = sum([perm[0]+perm[4]+perm[8]])
    diagonal2 = sum([perm[2]+perm[4]+perm[6]])
    if sum(perm[3:6]) == magic_constant and sum(perm[6:9]) == magic_constant and \
        magic_constant == diagonal and magic_constant == diagonal2 and \
        magic_constant == sum(perm[0:9:3]) and magic_constant == sum(perm[1:9:3]) and magic_constant == sum(perm[2:9:3]):
        matrix = [perm[0:3], perm[3:6], perm[6:9]]
        #print(matrix)
        #diff =  np.array(matrix) - np.array(arr)
        total = sum(abs(perm[i] - flatten_arr[i]) for i in range(0,9))
        if total < lowest_cost:
            lowest_cost = total
            magic_square = matrix 


            print(magic_square, lowest_cost, magic_constant)
