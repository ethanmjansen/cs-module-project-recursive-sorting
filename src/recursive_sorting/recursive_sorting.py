# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # set indexes to 0 
    left_index, right_index = 0, 0
    # result is the new merged array
    result = []
    # set while loop condition to break when base case
    while left_index < len(arrA) and right_index < len(arrB):
        # if a is less than b append b
        if arrA[left_index] < arrB[right_index]:
            result.append(arrA[left_index])
            left_index += 1
        # if a is greater than b append a
        else:
            result.append(arrB[right_index])
            right_index += 1

    # throw it on to the end 
    result += arrA[left_index:]
    result += arrB[right_index:]
    return result


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here

    if len(arr) <= 1:  # base case
        return arr

    # split in half
    half = len(arr) // 2
    left = merge_sort(arr[:half])
    right = merge_sort(arr[half:])

    # bring it back together
    return merge(left, right)


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    n1 = mid - start + 1
    n2 = end - mid
  
    # create temp arrays 
    L = [0] * (n1) 
    R = [0] * (n2) 
  
    # Copy data to temp arrays L[] and R[] 
    for i in range(0 , n1): 
        L[i] = arr[start + i] 
  
    for j in range(0 , n2): 
        R[j] = arr[mid + 1 + j] 
  
    # Merge the temp arrays back into arr[l..r] 
    i = 0     # Initial index of first subarray 
    j = 0     # Initial index of second subarray 
    k = start     # Initial index of merged subarray 
  
    while i < n1 and j < n2 : 
        if L[i] <= R[j]: 
            arr[k] = L[i] 
            i += 1
        else: 
            arr[k] = R[j] 
            j += 1
        k += 1
  
    # Copy the remaining elements of L[], if there 
    # are any 
    while i < n1: 
        arr[k] = L[i] 
        i += 1
        k += 1
  
    # Copy the remaining elements of R[], if there 
    # are any 
    while j < n2: 
        arr[k] = R[j] 
        j += 1
        k += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if l < r: 
  
        # Same as (l+r)//2, but avoids overflow for 
        # large l and h 
        m = (l+(r-1))//2
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m) 
        merge_sort_in_place(arr, m + 1, r) 
        merge_in_place(arr, l, m, r) 

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
