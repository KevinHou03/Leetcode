def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    rows, cols = len(grid), len(grid[0])
    max_area = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y):
        if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0:
            return 0
        grid[x][y] = 0
        area = 1
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            area += dfs(nx, ny)
        return area


    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

    return max_area

grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(maxAreaOfIsland(grid))


'''
def maxAreaOfIsland(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    rows, cols = len(grid), len(grid[0])
    max_area = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    def dfs(x, y, area):
        """Perform DFS and modify area in place."""
        if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0:
            return
        
        grid[x][y] = 0  # Mark as visited
        area[0] += 1  # Modify area inside the list

        for dx, dy in dirs:
            dfs(x + dx, y + dy, area)  # Recur for all 4 directions

    # Iterate through the grid and start DFS when we find an unvisited land cell
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                area = [0]  # Use a list to store the area (mutable)
                dfs(i, j, area)  # Pass as reference
                max_area = max(max_area, area[0])  # Update max area

    return max_area

'''