''' 
'''

from collections import defaultdict, Enum


class Color(Enum):
    WHITE = 1 # vertex is not processed yet.
    GRAY = 2 # all descendent are not processed yet.
    BLACK = 3  # encoutered gray vertex, therer is a cycle.


