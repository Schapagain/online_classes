# Uses Python3

def hasMajority(all_elements):

    # sort the list of elements
    sorted_elements = sorted(all_elements)
    mid_index = len(sorted_elements) // 2
    frequency_middle_element = sorted_elements.count(sorted_elements[mid_index])
    return int(frequency_middle_element > mid_index)

n = int(input().strip())
all_elements = list(map(int,input().strip().split()))

assert(n == len(all_elements))

print(hasMajority(all_elements))