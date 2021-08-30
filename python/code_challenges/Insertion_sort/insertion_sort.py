def insertion_sort(unsorted_list):
    r=len(unsorted_list)
    for i in range (1,r):
        j = i - 1
        temp_item = unsorted_list[i]
        while temp_item < unsorted_list[j] and j >= 0:
            unsorted_list[j+1] = unsorted_list[j]
            j = j - 1
        unsorted_list[j+1] = temp_item
    return unsorted_list

if __name__ == "__main__":

    print(insertion_sort([8,0,29,82,6,30]))
    print(insertion_sort([8,4,23,42,16,15]))

