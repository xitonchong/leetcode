

def bubble_sort(list1):
    print(list1)
    for n in range(len(list1)):
        swapped = False
        for i in range(len(list1)-n-1):
            if list1[i] > list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
                print(n, i, list1)
                swapped = True
        if swapped == False:
            break
    return list1


list1 = [4, 5, 1, 8, 3, 4]

print(bubble_sort(list1))