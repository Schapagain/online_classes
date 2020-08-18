# Uses Python3

def findMaxSum(weights,capacity):
    '''
        For a given set of weights, find the maximum sum
        that is at most equal to capacity
    '''
    num_weights = len(weights)
    dp_arr = [[0]*(capacity+1) for _ in range(num_weights+1)]

    for i in range(1,capacity+1):
        for w in range(1,num_weights+1):
            less_items_same_capacity = dp_arr[w-1][i]
            less_items_less_capacity = 0
            if i >= weights[w-1]:
                less_items_less_capacity = dp_arr[w-1][i-weights[w-1]] + weights[w-1]
            dp_arr[w][i] = max(less_items_less_capacity,less_items_same_capacity)
    

    # No combination is possible to sum up to capacity
    used = [0] * num_weights
    if dp_arr[num_weights][capacity] != capacity:
        return used

    # If possible find one such combination by backtracking
    row = num_weights
    col = capacity
    while row>0  and col>0 :
        curr_val = dp_arr[row][col]
        if weights[row-1] <= col and dp_arr[row-1][col-weights[row-1]] + weights[row-1] == curr_val:
            used[row-1] = 1
            col-=weights[row-1]
        row-=1

    return used

def checkThreeWayPartition(values):
    '''
        Check if it is possible to evenly split the given values
        into three parts
    '''
    if sum(values) % 3 == 0:
        sum_each_part = sum(values) // 3
        sol = [1]*len(values)
        count=-1
        while any(sol):
            count+=1

            # if more than three unique solutions exist, it's possible to partition three-way
            if count==3:
                return 1

            sol = findMaxSum(values,sum_each_part)
            values = [values[i] for i in range(len(values)) if sol[i] == 0]
    return 0

from sys import stdin
num_weights,*values = list(map(int,stdin.read().strip().split()))

print(checkThreeWayPartition(values))