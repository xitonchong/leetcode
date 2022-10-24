from itertools import groupby

s = "aaaaabbbcccccdddadaaa"

from itertools import groupby

groups = groupby(s)

result = [(label, sum(1 for _ in group)) for label, group in groups]


final_string = "".join("{}{}".format(label, count) for label, count in result)
print(final_string)