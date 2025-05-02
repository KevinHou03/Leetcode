from collections import defaultdict

from mpmath.calculus.calculus import defun


def findLonelyPixel(picture):
    """
    :type picture: List[List[str]]
    :rtype: int
    """
    result = 0
    rows, cols = len(picture), len(picture[0])
    row_set = defaultdict(list)
    col_set = defaultdict(list)

    for i in range(rows):
        for j in range(cols):
            if picture[i][j] == 'B':
                row_set[i].append(j)
                col_set[j].append(i)
    print(row_set)
    print(col_set)

    for item in row_set:
        if len(row_set[item]) == 1:
            col = row_set[item][0]
            if len(col_set[col]) == 1:
                result += 1
    return result



picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
print(findLonelyPixel(picture))
