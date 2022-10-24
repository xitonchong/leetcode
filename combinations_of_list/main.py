def combs(a):
    #cs = [] # dost not matter 
    if len(a) == 0:
        print('empty a condition found')
        return [[]]
    cs = []
    print('here')

    for c in combs(a[1:]):
        cs += [c, c+[a[0]]]
        print(c, a)
        #print(f"cs: {cs}, c: {c}, a[0]: {[a[0]]}, c+[a[0]]:  {c+[a[0]]}, a: {a}")
    return cs


print(combs([1,2,3]))