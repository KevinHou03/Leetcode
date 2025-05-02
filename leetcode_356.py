def isReflected(points):
    """
    :type points: List[List[int]]
    :rtype: bool
    """

    # find boundary points, set the symmetric line
    _min = min(x for x, y in points)
    _max = max(x for x, y in points)

    line = (_min + _max) / 2

    for point in points:
        x, y = point
        if [2 * line - x,y] not in points:
            return False

    return True


points = [[0,0], [1,0]]
print(isReflected(points))