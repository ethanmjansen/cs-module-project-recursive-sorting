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
    start2 = mid + 1
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1
        else: 
            value = arr[start2]
            index = start2
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]
                index -= 1
              
            arr[start] = value
  
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1
          
def merge_sort_in_place(arr, l, r): 
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m)
        merge_sort_in_place(arr, m + 1, r)
  
        merge_in_place(arr, l, m, r)


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
'''def timsort(arr):
    # Your code here

    return arr'''
