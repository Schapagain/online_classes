# Uses Python3


def binarySearch(sorted_list,key_list):

    search_result = []
    for key in key_list:
        low = 0
        high = len(sorted_list)-1
        while high >= low:

            mid = low + (high-low) // 2
            foundIndex = -1

            if sorted_list[mid] == key:
                foundIndex = mid
                break
            elif key > sorted_list[mid]:
                low = mid + 1
            else:
                high = mid - 1
        search_result.append(foundIndex)

    return search_result

# Slicing away the length of arrays at [0]
sorted_list = list(map(int,input().strip().split()))[1:]
key_list = list(map(int,input().strip().split()))[1:]

search_results = binarySearch(sorted_list,key_list)
print(' '.join(list(map(str,search_results))))
