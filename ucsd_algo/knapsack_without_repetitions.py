# Uses Python3

def findMaximumGold(weights,capacity):
    '''
        For a given set of gold bars with weights w_i, 
        find the maximum weight of gold that fits into 
        a backpack of given capacity
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
    
    return dp_arr[num_weights][capacity]


from sys import stdin
capacity,num_weights,*weights = list(map(int,stdin.read().strip().split()))

print(findMaximumGold(weights,capacity))