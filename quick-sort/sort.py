

def partition(start, end, arr):
    # choose the last element as the pivot
    # initialize left and right pointer as -1,0
    # if 
    pivot = arr[end]
    i = start-1
    for j in range(start, end):
        if arr[j] <= pivot:
            # swap the element
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i+1], arr[end] = arr[end], arr[i+1]
    
    return i+1


def quicksort(start, end, arr):
    # quick sort is a recursiave function after partitioning
    if start < end:
        p = partition(start, end, arr)
        print(p, arr)

        quicksort(start, p-1, arr)
        quicksort(p+1, end, arr)
    




arr = [10,80,30,90,40,50,70]
# time complexity is O(n log(n)), worst time complexity is when pivot is the largest or lowest element O(n^2)

quicksort(0, len(arr)-1, arr)  # intial condition
print(arr)