def binary_search(data, target):
    left = 0  # Initialize the left pointer to the start of the list
    right = len(data) - 1  # Initialize the right pointer to the end of the list
    
    while left <= right:  # Perform the binary search until left becomes greater than right
        mid = (left + right) // 2  # Calculate the middle index using integer division
        
        if data[mid] == target:  # If the middle element is the target, return the index
            return mid
        
        elif data[mid] < target:  # If the middle element is less than the target
            left = mid + 1  # Update the left pointer to search the right half
        
        else:  # If the middle element is greater than the target
            right = mid - 1  # Update the right pointer to search the left half
    
    return -1  # If the target is not found, return -1 to indicate it's not in the list

# Test the binary_search function
sorted_list = [2, 5, 8, 12, 15, 19, 22, 27, 31]
target_value = 12
index = binary_search(sorted_list, target_value)
print(index)  # Output: 3
