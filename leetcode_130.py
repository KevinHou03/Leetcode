def solve(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """

    if not board:
        return

    # dfs
    def dfs(i, j):
        #跳过非0的点和越界的点
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0])or board[i][j] != 0:
            return
        # 标记为“不用更改为X“
        board[i][j] = "N"
        dfs(i + 1, j)
        dfs(i - 1, j)
        dfs(i, j + 1)
        dfs(i, j - 1)

    #检查第一行和最后一行
    for i in range(len(board[0])):
        if board[0][i] == "0":
            dfs(0, i)
        if board[len(board) - 1][i] == "0":
            dfs(len(board) - 1, i)

    for j in range(len(board)):
        if board[j][0] == "0":
            dfs(j, 0)
        if board[j][len(board[0] - 1)] == "0":
            dfs(j, len(board[0]) - 1)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == "0":
                board[i][j] = "X"
            elif board[i][j] == "N":
                board[i][j] = "0"


