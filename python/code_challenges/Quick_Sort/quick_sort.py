def Quick_Sort(arr, left, right):
    if left < right:
        # Partition the array by setting the position of the pivot value
        position = partition(arr, left, right)
        #  Sort the left
        Quick_Sort(arr, left, position - 1)
        #  Sort the right
        Quick_Sort(arr, position + 1, right)


def partition(arr, left, right):
    #  set a pivot value as a point of reference
    pivot = arr[right]
    #  create a variable to track the largest index of numbers lower than the defined pivot
    lower = left - 1
    i = left
    while i < right:
        if arr[i] <= pivot:
            lower += 1
            swap(arr, i, lower)
        i += 1
    #  place the value of the pivot location in the middle.
    #  all numbers smaller than the pivot are on the left, larger on the right.
    swap(arr, right, lower + 1)
    # return the pivot index point
    return lower + 1


def swap(arr, i, low):
    temp = arr[i]
    arr[i] = arr[low]
    arr[low] = temp


arr = [114, 55, 343, 32]
Quick_Sort(arr, 0, len(arr) - 1)
print(arr)

