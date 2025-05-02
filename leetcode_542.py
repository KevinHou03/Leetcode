from collections import deque


def updateMatrix(mat):
    """
    :type mat: List[List[int]]
    :rtype: List[List[int]]
    """
    # bfs
    rows, cols = len(mat), len(mat[0])
    dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    ans = [float('inf') * cols for _ in range(rows)]

    queue = deque()

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                ans[i][j] = 0

                queue.append((i, j))

    while queue:
        x, y = queue.popleft()
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]
            if 0 <= nx < rows and 0 <= ny < cols and ans[nx][ny] > ans[x][y] + 1:
                ans[nx][ny] = ans[x][y] + 1
                queue.append((nx, ny))

    return ans


