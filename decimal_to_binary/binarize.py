


def decimal2binary(num1:int , res:str ) -> str:
    # recursive function
    if num1 == 0:
        return res


    res = str(num1 % 2) + res
    return decimal2binary(num1//2, res)


result = decimal2binary(10, '')
print(10, result)
assert result == '1010', print('assertion error ')







