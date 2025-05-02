def findDiagonalOrder(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[int]
    """
    rows, cols = len(mat), len(mat[0])
    res = []
    diags = {} # {i + j : [a,b,c...]}

    for i in range(rows):
        for j in range(cols):
            di = i + j
            if di not in diags:
                diags[di] = []
            diags[di].append(mat[i][j])

    for i in diags.keys():
        if i % 2 == 0:
            res.extend(reversed(diags[i]))
        else:
            res.extend(diags[i])
    return res


mat = [[1,2,3],[4,5,6],[7,8,9]]

print(findDiagonalOrder(mat))