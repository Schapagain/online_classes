# Uses Python3

def mergeLists(left_half,right_half):

    num_inversions = 0
    left_index = 0
    right_index = 0
    merged = []

    # Pick the smallest element from both lists and 
    # append it to the merged list until one of the lists
    # is exhausted
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
            
        else:
            merged.append(right_half[right_index])
            num_inversions += len(left_half) - left_index
            right_index += 1
        

    # If the left half still contains some elements
    # dump all of them on the final arr
    while left_index < len(left_half):
        merged.append(left_half[left_index])
        left_index += 1
    
    # If the right half still contains some elements
    # dump all of them on the final arr
    while right_index < len(right_half):
        merged.append(right_half[right_index])
        right_index += 1
    return (num_inversions,merged)

def findNumberOfInversions(arr):

    num_inversions = 0
    if len(arr) == 1:
        return 0
    else:
        # Split the array into two halves 
        mid_point = len(arr) // 2
        left_half = arr[:mid_point]
        right_half = arr[mid_point:]

        # Then merge sort recursively on both halves
        num_inversions += findNumberOfInversions(left_half)
        num_inversions += findNumberOfInversions(right_half)

        merge_results = mergeLists(left_half,right_half)
        arr[:] = merge_results[1]
        num_inversions += merge_results[0]

        return num_inversions

n = int(input().strip())
arr = list(map(int,input().strip().split()))
sorted_arr = arr.copy()
print(findNumberOfInversions(sorted_arr))