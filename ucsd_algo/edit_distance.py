# Uses Python3

def findEditDistance(seq1,seq2):

    len1 = len(seq1)+1
    len2 = len(seq2)+1

    dp_matrix = [[0 for j in range(len1)] for i in range(len2)]

    # fill up the first column/rows

    dp_matrix[0] = [j for j in range(len1)]
    for i in range(len2):
        dp_matrix[i][0] = i

    # stepwise buildup of the dp matrix
    for i in range(1,len2):
        for j in range(1,len1):  
            insert_cost = dp_matrix[i][j-1]+1
            delete_cost = dp_matrix[i-1][j]+1

            if seq1[j-1] == seq2[i-1]:
                match_cost = dp_matrix[i-1][j-1]
            else:
                match_cost = dp_matrix[i-1][j-1]+1
            dp_matrix[i][j] = min(insert_cost,delete_cost,match_cost)

    # return the bottom corner
    return dp_matrix[len2-1][len1-1]

from sys import stdin
seq1 = stdin.readline().strip()
seq2 = stdin.readline().strip()

print(findEditDistance(seq1,seq2))