'''
Input: n = 9
Output: 6
Explanation:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9] n = 9
arr = [2, 4, 6, 8] n = 4
arr = [2, 6] n = 2
arr = [6] n = 1

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] n = 9
arr = [2, 4, 6, 8, 10] n = 4
arr = [4, 8] n = 2
arr = [8] n = 1
'''


def lastRemaining(n):
    """
    :type n: int
    :rtype: int
    """

    #用recursion，第一轮从左到右删除后，实际上是只剩一半的数字，然后每个数字x2
    def helper(n, left_to_right):
        if n == 1:
            return 1
        if left_to_right:
            return 2 * helper(n // 2, False)
        else:
            return 2 * helper(n // 2, True) - (1 if n % 2 == 0 else 0)

    return helper(n, True)


