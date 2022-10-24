import itertools as it

# note that the iterable can be string, dictionary, list
# in this case string which contains negative float numbers
iterable = ['-0.234', '-0.04325', '-0.43134', '-0.315', '-0.6322', '-0.245',
            '-0.5325', '-0.6341', '-0.5214', '-0.531', '-0.124', '-0.0252']
float_iterable = [float(x) for x in iterable]
print(f"float iterable {float_iterable}")

def myfunc():
    return lambda x: x[:4]

result = [list(g) for k, g in it.groupby(sorted(float_iterable), key=lambda x: "{:.1f}".format(float(x))) ]
# result = [list(g) for k, g in it.groupby(sorted(iterable), key=lambda x: x[:4])] # if grouping first few character of a string 

print(result)