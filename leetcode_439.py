def parseTernary(expression):
    """
    :type expression: str
    :rtype: str
    """
    # 每次遇到“？”都是一次递归决策，但是我不想使用递归，而是使用stack
    # ternary你要先解内层，再归入外层，所有我们从右往左
    # eg: F ? 1 : (T ? 4 : 5)

    stack = []
    i = len(expression) - 1

    while i >= 0:
        if expression[i] == '?':
            t_val = stack.pop()
            f_val = stack.pop()
            stack.append(t_val if expression[i - 1] == 'T' else f_val)
            i -= 1
        elif expression[i] != ':':
            stack.append(expression[i])
            i -= 1

    return stack[0] #



