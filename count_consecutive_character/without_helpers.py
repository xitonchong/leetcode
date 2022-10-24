
s = "aaaaabbbcccccdddadaaa"

new_str = ""
counter = 0
prev = s[0]
for char in s:
    if char != prev:
        if counter == 1:
            new_str += "{}".format(prev)
        else:
            new_str += "{}{}".format(prev, counter)
        prev = char 
        counter = 0
    counter += 1
new_str += "{}{}".format(prev, counter)

#new_str = new_str.replace('1', '')
print(new_str)