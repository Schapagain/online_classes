# Uses python3

def findMinCoveringSet(all_segments):
    '''
        Given a set of segments(startpoint, endpoint) in a number line, find the minimum
        number of points required such that each segment
        covers at least one point
    '''
    # First sort all segments by their right edges
    all_segments = sorted(all_segments,key = lambda x: x[1])
    set_of_points = []

    # Add the right edge of the first segment as the first point
    first_edge = all_segments[0]
    set_of_points.append(first_edge[1])

    # Then go through the rest of the segments
    for i in range(1,len(all_segments)):

        # If the current segment is already covered
        # by the last point added, skip this segment
        last_point_added = set_of_points[-1]
        if all_segments[i][0] <= last_point_added:
            continue

        # Else add the right edge of the current segment
        else:
            set_of_points.append(all_segments[i][1])

    return set_of_points

num_segments = int(input().strip())

# Stores segments as a list of tuples (start_point,end_point)
all_segments = []
for i in range(num_segments):
    segment =  tuple(map(int,input().strip().split()))
    all_segments.append(segment)

min_set_of_points = list(map(str,findMinCoveringSet(all_segments)))
print(len(min_set_of_points),' '.join(min_set_of_points),sep='\n')