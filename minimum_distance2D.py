# Uses Python3

import math
import itertools as iter

def findDistance(point1,point2):
    x1,y1 = point1
    x2,y2 = point2

    return math.sqrt((y2-y1)**2+(x2-x1)**2)

def findMiminumDistance(all_points,all_points_y,l,h):

    '''
        Returns the distance between the closest two points
        in all_points[l:h] inclusive
        
        note: all_points_y = all_points must be sorted by their y-coordinate
    '''

    # If there are less than four points, 
    # find minDist using the traditional method
    if h-l+1 <= 3:
        all_pairs = list(iter.combinations(all_points[l:h+1],2))
        min_dist = math.inf
        for pair in all_pairs:
            curr_dist = findDistance(*pair)
            if curr_dist < min_dist:
                min_dist = curr_dist
        return min_dist

    # Recursively divide the plane into halves
    m = (h+l) // 2
    min_left = findMiminumDistance(all_points,all_points_y,l,m)
    min_right = findMiminumDistance(all_points,all_points_y,m+1,h)
    min_both = min(min_left,min_right)

    # Find the region around the dividing line
    T=[]
    for point in all_points[l:h+1]:
        if abs(point[0]-all_points[m][0])<=min_both:
            T.append(point)
    
    # Go through T and find the minimum distance among them
    min_dist = math.inf
    k = len(T)
    for i in range(k):
        for j in range(i+1,min(i+7,k-1)+1):
            curr_dist = findDistance(T[i],T[j])
            if curr_dist < min_dist:
                min_dist = curr_dist

    return min(min_dist,min_both)

num_points = int(input().strip())
all_points = []
for i in range(num_points):
    all_points.append(list(map(int,input().strip().split())))

# Sort by x-coordinate
all_points = sorted(all_points,key=lambda x: x[0])
all_points_y = sorted(all_points,key=lambda x: x[1])

print(findMiminumDistance(all_points,all_points_y,0,num_points-1))