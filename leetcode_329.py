def longestIncreasingPath(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: int
    """
    rows, cols = len(matrix), len(matrix[0])
    memo = [[-1] * cols for _ in range(rows)] # every value in [i][j] is the longest increasing value starting at [i][j]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    res = 0
    def dfs(i, j):
        # if already tried, return directly
        if memo[i][j] != -1:
            return memo[i][j]
        max_len = 1
        for dx, dy in directions:
            ni, nj = i + dx, j + dy
            # check boundary
            if 0 <= ni < rows and 0 <= nj < cols:
                if matrix[ni][nj] > matrix[i][j]:
                    max_len = max(max_len, 1 + dfs(ni, nj))
        memo[i][j] = max_len
        return max_len

    for i in range(rows):
        for j in range(cols):
            res = max(res, dfs(i, j))
    return res


print([-1] * 7)

