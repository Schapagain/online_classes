# Uses Python3

def getMaxLoot(all_items,capacity):
    # Sort all available items by per unit value in nonincreasing order
    all_items = sorted(all_items, key = lambda x: x[0], reverse=True)

    # Go through each available item and fill the knapsack greedily
    value_taken = 0
    for item in all_items:

        # Either fill the whole of the knapsack with the first item
        # or take all of the first item and move on to the second one
        amt_of_first_item = min(item[1],capacity)
        value_taken += amt_of_first_item * item[0]

        capacity -= amt_of_first_item

        if capacity == 0:
            return value_taken
    
    # If there's not enough items to fill the knapsack 
    # return the value after using all the items
    return value_taken

num_items,capacity = list(map(int,input().strip().split()))
all_items =[]

# Take in value, weight and store (value per weight, weight) in a list of tuples
for i in range(num_items):
    value,weight = list(map(int,input().strip().split()))
    all_items.append((value/weight,weight))

print(f'{getMaxLoot(all_items,capacity):0.4f}')
