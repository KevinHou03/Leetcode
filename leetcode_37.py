def solveSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: None Do not return anything, modify board in-place instead.
    """
    row = [set() for _ in range(9)]
    col = [set() for _ in range(9)]
    box = [set() for _ in range(9)]


    # populate
    for i in range(9):
        for j in range(9):
            if board[i][j] != '.':
                num = int(board[i][j])
                row[i].add(num)
                col[j].add(num)

                box_id = i // 3 * 3 + j // 3 # why?
                box[box_id].add(num)

    def backtrack(i, j):
        nonlocal solved
        if i == 9:
            solved = True
            return
        new_i = i + (j + 1) // 9
        new_j = (j + 1) % 9

        if board[i][j] != ".":
            backtrack(new_i, new_j)
        else:
            for num in range(1, 10):
                box_id = i // 3 * 3 + j // 3
                if num not in box[i] and num not in col[i] and num not in box[box_id]:
                    row[i].add(num)
                    col[j].add(num)
                    box[box_id].add(num)
                    backtrack(new_i, new_j)
                    board[i][j] = str(num)

                    # pop
                    if not solved:
                        row[i].remove(num)
                        col[j].remove(num)
                        box[box_id].remove(num)
                        board[i][j] = "."

    solved = False
    backtrack(0, 0)
