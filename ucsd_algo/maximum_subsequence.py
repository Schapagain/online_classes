# Uses Python3

def printMatrix(m):
    for row in m:
        print(row)

def findMaxSubsequence3(seq1,seq2,seq3):
    '''
        Returns the length of the longest subsequence 
        among three given iterables
    '''
    len1 = len(seq1)+1
    len2 = len(seq2)+1
    len3 = len(seq3)+1

    dp_matrix = [[[0 for k in range(len3)] for j in range(len1)] for i in range(len2)]

    # stepwise buildup of the dp matrix
    for i in range(1,len2):
        for j in range(1,len1): 
            for k in range(1,len3): 
                cost1 = dp_matrix[i][j][k-1]
                cost2 = dp_matrix[i][j-1][k-1]
                cost3 = dp_matrix[i-1][j][k-1]
                cost4 = dp_matrix[i][j-1][k]
                cost5 = dp_matrix[i-1][j][k]
                cost6 = dp_matrix[i-1][j-1][k]

                match_cost = dp_matrix[i-1][j-1][k-1]
                
                overall_cost = max(cost1,cost2,cost3,cost4,cost5,cost6,match_cost)
                current_match = seq1[j-1] == seq2[i-1] == seq3[k-1]
                if (match_cost == overall_cost and  current_match):
                    overall_cost += 1
                dp_matrix[i][j][k] = overall_cost


    # return the bottom corner
    return dp_matrix[len2-1][len1-1][len3-1]

from sys import stdin
_ = stdin.readline()
seq1 = stdin.readline().strip().split()
_ = stdin.readline()
seq2 = stdin.readline().strip().split()
_ = stdin.readline()
seq3 = stdin.readline().strip().split()

print(findMaxSubsequence3(seq1,seq2,seq3))
