# Uses Python3

def finMinimumOperations(n):
    '''
        Given only the operations +1, *2, and *3,
        return [min_op,op_seq] where 
        min_op = minimum number of operations to get to n
        op_seq = the intermediate values including 1,n used by min_op steps
    '''

    steps_memory = [0,[0]]* (n+1)
    steps_memory[1:4] = [[0,[1]],[1,[1,2]],[1,[1,3]]]
    for i in range(4,n+1):

        prev_steps = steps_memory[i-1][1]
        min_to_i = steps_memory[i-1][0] 
        if i % 3 == 0:
            min_to_one_thirds_i = steps_memory[i//3][0]
            if min_to_one_thirds_i < min_to_i:
                min_to_i = min_to_one_thirds_i
                prev_steps = steps_memory[i//3][1]
        if i % 2 == 0:
            min_to_half_i = steps_memory[i//2][0]
            if min_to_half_i < min_to_i:
                min_to_i = min_to_half_i
                prev_steps = steps_memory[i//2][1]

        steps_memory[i] = [min_to_i+1,prev_steps+[i]]
    return steps_memory[n]
n = int(input().strip())

min_steps,steps = finMinimumOperations(n)

print(min_steps)
print(*steps,end=' ')
print()