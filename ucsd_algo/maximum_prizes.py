# Uses Python3

def findPrizeList(num_candies):

    if num_candies < 3:
        return [num_candies]

    # Add first two prizes in the list
    prizes = [1,2]
    candies_remaining = num_candies - 3

    # Add one more position if we have enough candies
    # else add remaining candies to the prize for 
    # previous positioono
    while candies_remaining > 0:
        last_prize_added = prizes[-1]
        if candies_remaining >= last_prize_added + 1:
            prizes.append(last_prize_added+1)
            candies_remaining -= last_prize_added+1
        else:
            prizes[-1] += candies_remaining
            candies_remaining = 0
    
    return prizes
        
num_candies = int(input().strip())
prizes = list(map(str,findPrizeList(num_candies)))
print(f'{len(prizes)}\n{" ".join(prizes)}')