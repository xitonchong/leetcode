
def intToRoman( num: int) -> str:
    threshold = [1000, 900, 500, 400, 100, 90, 50, 40,  10, 9,  5, 4, 1]
    symbol = ['M', 'CM','D', 'CD', 'C', 'XC',  'L', 'XL', 'X', 'IX',  'V', 'IV', 'I']
    threshold2symbol = dict(zip(threshold, symbol))
    
    #print(threshold2symbol)
    str1 = ""
    for t in threshold:
        while num >= t:
            num -= t 
            str1+= str(threshold2symbol[t])
    return str1



print(intToRoman(1226))