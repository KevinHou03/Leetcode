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
    # 先把所有n以内的 power num with ^x 全部找出来
    MOD = 10 ** 9 + 7

    powers = []
    while True:
        i = 1
        power = i ** x
        if power > n:
            break
        powers.append(power)
        i += 1

    # 定义dp， dp[i]表示利用x凑成i这个数的方案总数
    dp = [0] * (n + 1)
    dp[0] = 1

    for power in powers:
        for t in range(n, power - 1, -1):
            dp[t] = (dp[t] + dp[t - power]) % MOD

    return dp[n]
# 这是一个01背包问题




