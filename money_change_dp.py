def money_change(money,coins,min_coins):
    '''
        Returns the minimum number of coins of the given designations
        required to change the given amount of money
    '''
    
    if money == 0:
        return 0
    
    if min_coins[money] <= money:
        return min_coins[money]

    for coin in coins:
        if money>=coin:
            curr_coins = money_change(money-coin,coins,min_coins) + 1
            if curr_coins < min_coins[money]:
                min_coins[money] = curr_coins
    
    return min_coins[money]


coins = [1,3,4]
money = int(input().strip())
min_coins = [money+1] * (money+1)
print(money_change(money,coins,min_coins))