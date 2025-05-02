def calculate(s):
    """
    :type s: str
    :rtype: int
    """

    stack = [] # only store result and sign
    sign = 1
    num = 0 # the current number we are on
    res = 0 # 目前这个括号内，或者没有括号也行，的计算结果，是累积的

    has_sign = 0
    signs = '+-'

    for element in s:
        if element.isdigit():
            num = num * 10 + int(element) #这样多位数也可以得到了 str -> int
        elif element in '+-':
            has_sign = 1
            res += sign * num
            num = 0 # 遇到sign说明上一个num结束了，归0
            sign = 1 if element == '+' else -1
        elif element == '(':
            stack.append(res)
            stack.append(sign)
            # num = 0
            res = 0
            sign = 1
        elif element == ')':
            res += sign * num
            num = 0
            res *= stack.pop()
            res += stack.pop()
    res += sign * num

    if not has_sign:
        s = "".join(char for char in s if char.isdigit())
    return res if has_sign else int(s)


print(calculate("1-11"))