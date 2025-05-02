def pacificAtlantic(heights):
    """
    :type heights: List[List[int]]
    :rtype: List[List[int]]
    """

    # mark the cell that can be reached by pacific rim using set
    # mark the cell that can be reached by atlantic rim using set
    # find intersection
    rows, cols, = len(heights), len(heights[0])
    dirs = [[0, 1], [1, 0], [0, -1], [-1,0]]

    pacific = set()
    atlantic = set()

    def dfs(x, y, visited):
        cur_height = heights[x][y]
        if (x, y) not in visited:
            visited.add((x, y))
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and heights[nx][ny] >= cur_height:
                dfs(nx, ny, visited)

    for i in range(rows):
        dfs(i, 0, pacific)
        dfs(i, cols - 1, atlantic)

    for j in range(cols):
        dfs(0, j, pacific)
        dfs(rows - 1, j, atlantic)


    return list(pacific & atlantic)


heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))

