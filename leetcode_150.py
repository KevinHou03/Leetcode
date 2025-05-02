def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """

    stack = []
    for element in tokens:
        if element.isdigit() or (element[0] == '-' and element[1:].isdigit()):  # 允许负数
            stack.append(int(element))
        else:
            num1 = stack.pop()
            num2 = stack.pop()
            if element == "+":
                stack.append(num1 + num2)
            elif element == '-':
                stack.append(num1 - num2)
            elif element == '*':
                stack.append(num1 * num2)
            elif element == '/':
                stack.append(int(num1 / num2))
    return stack[0]


