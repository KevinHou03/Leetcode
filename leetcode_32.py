def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    stack = [-1]  # 初始化栈，存入基准索引 -1
    max_length = 0  # 记录最大有效长度

    for i, char in enumerate(s):
        if char == '(':
            # 记录左括号索引
            stack.append(i)
        else:
            # 右括号尝试匹配
            stack.pop()
            if not stack:
                # 如果栈为空，说明当前右括号无效，记录基准索引
                stack.append(i)
            else:
                # 如果栈不为空，计算有效长度
                max_length = max(max_length, i - stack[-1])

    return max_length
