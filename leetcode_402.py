def removeKdigits(num, k):
    """
    :type num: str
    :type k: int
    :rtype: str
    """
    # 用贪心 + 单调栈 monotonic stack，当前数字小于栈顶的时候弹出栈顶，并且当前数字入栈
    # 栈内是递增的

    if len(num) <= k:
        return '0'

    mono_stack = []
    for _num in num:
        while k > 0 and mono_stack and mono_stack[-1] > _num:
            mono_stack.pop()
            k -= 1
        mono_stack.append(_num)

    # 如果所有数字都便利完了但是k还不为0，证明还要手动删除剩下k个数字

    while k > 0:
        mono_stack.pop()
        k -= 1

    print(mono_stack)
    while mono_stack[0] == '0' and len(mono_stack) > 1:
        mono_stack = mono_stack[1:]
    return ''.join(mono_stack)
print(removeKdigits('10', 2))





