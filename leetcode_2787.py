def numberOfWays(n, x):
    """
    :type n: int
    :type x: int
    :rtype: int
    """
    MOD = 10 ** 9 + 7

    '''
    从1开始选， 一个choice一个choice往后， dfs(choice, cur_num)
    选的话：dfs(choice + 1, cur_num - choice ** x)
    不选的话：dfs(choice + 1, cur_num)
    '''
    memo = {}
    def dfs(choice, cur_num):
        key = (choice, cur_num)
        if key in memo:
            return memo[key]
        # 两种终止条件
        if choice ** x > cur_num:
            return 0
        if choice ** x == cur_num:
            return 1
        ans =  (dfs(choice + 1, cur_num - choice ** x) + dfs(choice + 1, cur_num)) % MOD
        memo[key] = ans
        return ans

    return dfs(1, n)


def numberOfWaysDP(n, x):
    """
    :type n: int
    :type x: int
    :rtype: int
    """
    # 先把所有n以内的power num全部找出来
