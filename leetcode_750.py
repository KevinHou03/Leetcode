def countCornerRectangles(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    # 任意枚举两行，两行种两列都有1的数量与2的combination C(x, 2) 就是他能组合的rectangle的数量
    # 计算公式为： （x * （x - 1）） // 2

    rows, cols = len(grid), len(grid[0])
    total_rec = 0
    for i in range(rows):
        for j in range(i + 1, rows):
            count = 0
            for k in range(cols):
                if grid[i][k] == 1 and grid[j][k] == 1:
                    count += 1
            # 必须至少要找到两对才能成一个rectangle
            if count >= 2:
                rec_count = (count * (count - 1)) // 2
                total_rec += rec_count

    return total_rec

