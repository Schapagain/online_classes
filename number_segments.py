#Uses Python3

def getInsertionIndex(sorted_list,key):

    low = 0
    high = len(sorted_list)-1
    while high >= low:

        mid = (low+high)//2
        midVal = sorted_list[mid]
        if midVal == key:
            return mid
        elif key > midVal:
            low = mid + 1
            ret_idx = low - 1
        else:
            high = mid - 1
            ret_idx = high

    return ret_idx

def findNumberCoveringSegments(all_segments,all_points):
    '''
        For a given set of points, and a set of segments,
        return the maximum number of segments covered by
        any single point
    '''
    temp_dict=dict()
    for start,end in all_segments:
        all_keys = temp_dict.keys()
        if start in all_keys:
            temp_dict[start] += 1
        else:
            temp_dict[start] = 1
        if (end+1) in all_keys:
            temp_dict[end+1] -= 1
        else:
            temp_dict[end+1] = -1

    temp_arr = sorted(temp_dict)

    # Create a prefix-sum array
    prefix_sum = []
    prev = 0
    for k in temp_arr:
        curr =  temp_dict[k] + prev
        prefix_sum.append(curr)
        prev = curr

    insertion_indicies = list(map(lambda x: getInsertionIndex(temp_arr,x),all_points))

    cnt = []
    for index in insertion_indicies:
        if index <0 or index >= len(prefix_sum):
            cnt.append(0)
        else:
        	cnt.append(prefix_sum[index])
    
    return max(cnt)

# # Stores segments as a list of tuples (start_point,end_point)
all_segments = []

num_segments,num_points = list(map(int,input().strip().split()))

for _ in range(num_segments):
    start,end =  list(map(int,input().strip().split()))
    all_segments.append((start,end))

all_points = list(map(int,input().strip().split()))
print(findNumberCoveringSegments(all_segments,all_points))
