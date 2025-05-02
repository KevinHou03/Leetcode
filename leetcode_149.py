from collections import defaultdict
from math import gcd


def maxPoints(points):
    """
    :type points: List[List[int]]
    :rtype: int
    """
    def find_slope(x1, y1, x2, y2):
        dy = y2 - y1
        dx = x2 - x1

        g = gcd(dy, dx)
        return dy // g, dx // g

    max_p = 0
    for i in range(len(points)):
        # 对每一个anchor point创建一个字典，然后看哪一个slope出现的最多
        slope_dict = defaultdict(int)
        duplicates = 1 # 要加上他本身
        for j in range(i + 1, len(points)):
            slope = find_slope(points[i][0], points[i][1], points[j][0], points[j][1])
            if points[i] == points[j]:
                duplicates += 1
            else:
                slope_dict[slope] += 1
        max_p = max(max_p, duplicates + max(slope_dict.values(), default=0))

    return max_p

points =[[1,1],[2,2],[3,3]]
print(maxPoints(points))


