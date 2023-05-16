# Function: Binary Search
# Input: data - a sorted list of elements, el - the element to find
# Output: True if the element is found, False otherwise
def binary_search(data, el):
    first = 0  # index of the first element in the search space
    last = len(data) - 1  # index of the last element in the search space
    found = False  # flag to indicate whether the element is found or not
      
    # Perform binary search until the element is found or the search space is exhausted
    while first <= last and not found:
        mid = (first + last) // 2  # index of the middle element in the search space        
        if data[mid] == el:
            found = True  # Element is found at the middle index        
        else:
            if el < data[mid]:
                last = mid - 1  # Discard the right half of the search space and repeat on the left half
            else:
                first = mid + 1  # Discard the left half of the search space and repeat on the right half
    
    return found

# Test the binary_search function
test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]
print(binary_search(test_list, 12))  # Output: True
