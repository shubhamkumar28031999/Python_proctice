import sys

all_matrix=[[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
           [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
           [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
           [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
           [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
           [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
           [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
           [[2, 7, 6], [9, 5, 1], [4, 3, 8]]]
def forming_magic_square(mat):
    cost=[sys.maxsize]*len(all_matrix)
    for ref_matrix in all_matrix:
        temp_cost=0
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                if ref_matrix[x][y]!=mat[x][y]:
                    temp_cost+=abs(ref_matrix[x][y]-mat[x][y])
        cost.append((temp_cost))
    return min(cost)

