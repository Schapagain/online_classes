# Uses python3
import sys

def get_change(m):

    # We need a nonincreasing order of denominations here
    # for the algorithm below to work
    denominations = [10,5,1]

    num_coins = 0
    curr_change = m
    for coin in denominations:
        num_coins += curr_change // coin
        curr_change %= coin

    return num_coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))