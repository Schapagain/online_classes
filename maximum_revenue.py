# Uses python3

def getMaxRevenue(profits_per_click,number_of_clicks):

    from functools import reduce
    # Sort both profits and average number of clicks
    # in non-increasing order so that we can pair 
    # up corresponding elements to maximize pairwise product

    profits_per_click = sorted(profits_per_click,reverse=True)
    number_of_clicks = sorted(number_of_clicks,reverse=True)
    
    # Return the sum of all corresponding products
    print(int(reduce(lambda x,y:x+y, [a*b for (a,b) in zip(profits_per_click,number_of_clicks)])))

profits_per_click = []
number_of_clicks = []

num_ads = int(input().strip())
profits_per_click = list(map(int,input().strip().split()))
number_of_clicks = list(map(int,input().strip().split()))

assert(num_ads == len(profits_per_click) == len(number_of_clicks))

getMaxRevenue(profits_per_click,number_of_clicks)

