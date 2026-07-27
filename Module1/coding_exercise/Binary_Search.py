def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1
            
        else:
            right = mid - 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 11], 7))  
print(binary_search([1, 3, 5, 7, 9, 11], 6))  
print(binary_search([], 5))                   