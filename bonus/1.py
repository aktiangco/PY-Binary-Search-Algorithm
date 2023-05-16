def recursive_bsearch(lst, val):
    if len(lst) == 0:  # Base case: If the list is empty, the element is not found
        return False
    
    mid = len(lst)// 2  # Index of the middle element
    
    if lst[mid] == val:  # Base case: If the middle element is equal to the target element, it is found
        return True
    
    elif val < lst[mid]:  # Recursive case: If the target element is less than the middle element, search the lower half
        return recursive_bsearch(lst[:mid], val)
    
    else:  # Recursive case: If the target element is greater than the middle element, search the upper half
        return recursive_bsearch(lst[mid+1:], val)

# Test the recursive_bsearch function
test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(recursive_bsearch(test_list, 12))  # Output: True
