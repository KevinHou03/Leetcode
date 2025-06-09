def lexicalOrder(n):
    """
    :type n: int
    :rtype: List[int]
    """

    res = []
    def dfs(cur):
        if cur > n:
            return
        res.append(cur)
        for i in range(10):
            next_num = cur * 10 + i
            if next_num > n:
                continue
            dfs(next_num)
    for i in range(1, 10):
        dfs(i)
    return res


print(lexicalOrder(10))