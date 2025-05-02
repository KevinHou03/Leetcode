

def trap(height):
    """
    :type height: List[int]
    :rtype: int
    """

    max_left, max_right, minLR, = [], [], []
    max_l, max_r = 0, 0
    for i in range(len(height)):
        max_left.append(max_l)
        max_l = max(max_l, height[i])
    print(max_left)

    for j in range(len(height) - 1, -1, -1):
        max_right.append(max_r)
        max_r = max(max_r, height[j])
    max_right = max_right[::-1]

    minLR = [max(0, min(max_left[k], max_right[k]) - height[k]) for k in range(len(height))]

    return sum(minLR)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
trap(height)


