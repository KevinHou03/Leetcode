def maxKilledEnemies(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    rows, cols = len(grid), len(grid[0])
    max_kill = 0
    row_kill = 0
    col_kill = [0] * cols

    for i in range(rows):
        for j in range(cols):
            if j == 0 or grid[i][j - 1] == "W":
                k = j
                row_kill = 0
                while k < cols and grid[i][k] != 'W':
                    if grid[i][k] == 'E':
                        row_kill += 1
                    k += 1

            if i == 0 or grid[i - 1][j] == 'W':
                s = i
                col_kill[j] = 0
                while s < rows and grid[s][j] != 'W':
                    if grid[s][j] == 'E':
                        col_kill[j] += 1
                    s += 1

            if grid[i][j] == '0':
                max_kill = max(max_kill, row_kill + col_kill[j])

    return max_kill

