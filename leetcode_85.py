def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    def calculate_max_area(heights):
        stack = []
        max_area = 0

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, (i - index) * height)
                start = index
            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)
        return max_area

    if not matrix or not matrix[0]:
        return 0
    rows, cols = len(matrix), len(matrix[0])
    heights = [0] * cols
    max_area = 0

    for row in matrix:
        for j in range(cols):
            if row[j] == '1':
                heights[j] += 1
            else:
                heights[j] = 0
        max_area = max(max_area, calculate_max_area(heights))
    return max_area


