
def kthSmallest(matrix, k):
    """
    :type matrix: List[List[int]]
    :type k: int
    :rtype: int
    """
    row_index = (k - 1) // len(matrix[0])
    col_index = (k - 1) % len(matrix[0])
    print(row_index, col_index)

    return matrix[row_index][col_index]




matrix = [[1,5,9],[10,11,13],[12,13,15]]
print(kthSmallest(matrix,8))