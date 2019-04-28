import numpy as np

def longest_increasing_sequence(input_array, sequences, i):
    """ find the lognest sequence in a list"""
    """" how to solve this problem recursively?"""
    ''' algorithm, if last element < input_array[i]
            append
            update max list
            if not append:
                start a new list.
    '''
    if i == 0:
        max_seq = [input_array[0]]
        sequences.append(max_seq)
        return max_seq

    max_seq = longest_increasing_sequence(input_array, sequences,i-1)
    for seq in sequences:
        if seq[-1] < input_array[i]:
            sequences.append(seq + [input_array[i]])
            if len(sequences[-1]) > len(max_seq):
                max_seq = sequences[-1]
    sequences.append([input_array[i]])
    return max_seq


a = [1, 6, 7, 4, 6, 3, 4, 6, 19, 12, 14, 35, 66]
print(longest_increasing_sequence(a, [], len(a) - 1))
a = [1, 6, 7, 4, 6, 1, 3, 4, 6, 19, 12, 14, 35, 2]
print(longest_increasing_sequence(a, [], len(a) - 1))
a = [5, 1, 2, 4, 5, 3, 7]
print(longest_increasing_sequence(a, [], len(a) - 1))
