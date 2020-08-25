# Uses Python3

def partition(arr,low,high):

    # Randomize the pivot selection
    import random
    pivotIndex = random.randint(low,high)
    pivot = arr[pivotIndex]

    # Swap the pivotIndex with the first element
    arr[low], arr[pivotIndex] = arr[pivotIndex], arr[low]

    lessIndex = low
    equalIndex = low+1

    # Go through array elements compartmentalizing them 
    # accorindg to their size wrt. the pivot
    for moreIndex in range(low+1,high+1):
        if arr[moreIndex] < pivot:
            arr[equalIndex],arr[moreIndex] = arr[moreIndex],arr[equalIndex]
            arr[lessIndex],arr[equalIndex] = arr[equalIndex],arr[lessIndex]
            lessIndex += 1
            equalIndex += 1
        
        elif arr[moreIndex] == pivot:
            arr[equalIndex],arr[moreIndex] = arr[moreIndex],arr[equalIndex]
            equalIndex += 1

    # Return the range of index whose elements are in the right position
    return (lessIndex,equalIndex)

def quickSort(arr,low,high):
    '''
        Sort the given array elements using a Quicksort with a 3-way partition 
    '''
    if low < high:
        pivotRange = partition(arr,low,high)
        leftSliceIndex = pivotRange[0]
        rightSliceIndex = pivotRange[1]

        quickSort(arr,low,leftSliceIndex)
        quickSort(arr,rightSliceIndex,high)

n = int(input().strip())
unsorted_list = list(map(int,input().strip().split()))
assert(n == len(unsorted_list))

quickSort(unsorted_list,0,n-1)
print(' '.join(map(str,unsorted_list)))