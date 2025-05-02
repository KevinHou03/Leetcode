def numDistinctIslands(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    # use relative position of a point on an island to the first-discover point coordinate to
    # identify if two island have the same shape

    # shape stores data of a island (relative coordinates)
    island = set()
    rows, cols = len(grid), len(grid[0])
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y, base_x, base_y, shape):
        # when discovered an island, execute dfs to traverse all points on this island
        # terminate when a point outside this island is found
        if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0:
            return
         # mark as visited
        grid[x][y] = 0

        # if not, record it
        shape.append((x - base_x, y - base_y))
        for dir in dirs:
            dfs(x + dir[0], y + dir[1], base_x, base_y, shape)


    # now traverse the grid, when meeting a '1', execute the dfs algorithm
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                shape = []
                dfs(i, j, i, j, shape)
                island.add(tuple(shape))
    return len(island)


grid = [[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]
print(numDistinctIslands(grid))