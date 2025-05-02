def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    rows, cols = len(board), len(board[0])
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, 1], [-1, -1], [1, -1], [-1, 1]]

    def count_neighbors(x, y):
        count = 0
        for dir in dirs:
            nx, ny = x + dir[0], y + dir[1]
            # check boundary
            if 0 <= nx < rows and 0 <= ny < cols and abs(board[nx][ny]) == 1:
                count += 1
        return count

    for i in range(rows):
        for j in range(cols):
            living_neighbors = count_neighbors(i, j)
            if board[i][j] == 1:
                if living_neighbors < 2 or living_neighbors > 3:
                    # live -> die
                    board[i][j] = -1
            else:
                if living_neighbors == 3:
                    board[i][j] = 888 # means now it is dead but soon to be alive

    for i in range(rows):
        for j in range(cols):
            if board[i][j] == -1:
                board[i][j] = 0
            elif board[i][j] == 888:
                board[i][j] = 1

