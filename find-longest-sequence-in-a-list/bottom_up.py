import numpy as np
import time

def find_longest_sequence(lst):
    max_seq = [lst[0]]
    sequences = [max_seq] 
    for n in range(1, len(lst)):
        for i in range(len(sequences) - 1, -1, -1):
            #print("{}, sequences {}".format(i, sequences))
            #time.sleep(5)
            seq = sequences[i]
            # if last element of sequence less than input array
            if seq[-1] < lst[n]:
                sequences.append(seq + [lst[n]])
                if len(sequences[-1]) > len(max_seq):
                    max_seq = sequences[-1]
                    break
            else:
                # remember to append a list with a number 
                sequences.append([lst[n]])
    return max_seq

if __name__ == '__main__':
    lst = [1, 6, 7, 4, 6, 1, 3, 4, 6, 19, 12, 14, 35, 66]
    print(find_longest_sequence(lst))
    lst = [1, 6, 7, 4, 6, 1, 3, 4, 6, 19, 12, 14, 35, 2]
    print(find_longest_sequence(lst))
    lst = [5, 1, 2, 4, 5, 3, 7]
    print(find_longest_sequence(lst))

