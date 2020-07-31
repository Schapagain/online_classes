

def nFib(n):

    firstNum = 0
    secondNum = 1
    for _ in range(n):
        firstNum,secondNum = secondNum,firstNum+secondNum
    
    return firstNum

n=int(input().strip())

print(nFib(n))
