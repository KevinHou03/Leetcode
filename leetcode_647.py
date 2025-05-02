def countSubstrings(s):
    """
    :type s: str
    :rtype: int
    """

    dp = [[False] * len(s) for _ in range(len(s))]
    count = 0
    # dp[i][j] 意味着s[i:j + 1]是否为回文

    for j in range(len(s)):
        for i in range(j + 1): # i can be equal to j
            if s[i] == s[j] and (j - i < 2 or dp[i + 1][j - 1]):
                dp[i][j] = True
                count += 1

    return count

