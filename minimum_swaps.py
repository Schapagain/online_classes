def minimumSwaps(arr):
    '''
        Return the minimum number of swaps 
        necessary to sort the array in non-decreasing order
    '''
    still_swapping = True
    num_swaps = 0
    while (still_swapping):
        still_swapping = False
        for curr_pos,init_pos in enumerate(arr):
            if curr_pos != init_pos-1:
                arr[curr_pos], arr[init_pos-1] = arr[init_pos-1], arr[curr_pos]
                still_swapping = True
                num_swaps += 1

        print(arr)
    return num_swaps

arr = list(map(int,input().strip().split()))
print(minimumSwaps(arr))
