# Uses Python3
from functools import cmp_to_key

def compare_fragmentsAB(a,b):
    '''
    Comparator function for number fragments
    '''
    
    # Convert a,b to strings
    a = str(a)
    b = str(b)

    # Numbers formed by joining fragments
    ab = a+b
    ba = b+a

    # Return comparator values
    if ab>ba:
        return 1
    elif ab<ba:
        return -1
    else:
        return 0

def findMaximumSalary(list_fragments):

    # Create a copy of the
    # Sort all digits in non-increasing order
    sorted_fragments = sorted(list_fragments,key=cmp_to_key(compare_fragmentsAB),reverse=True)

    # Join all fragments together to form the maximal number
    max_salary = int(''.join(sorted_fragments))

    return max_salary

num_fragments = int(input().strip())
list_fragments = list(input().strip().split())

assert(num_fragments == len(list_fragments))

print(findMaximumSalary(list_fragments))