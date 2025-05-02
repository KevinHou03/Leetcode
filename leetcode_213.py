def rob(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0], nums[1])

    def aux(nums):
        dp = [-1] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        robbed = [False] * len(nums)

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return max(dp)

    return max(aux(nums[:len(nums) - 1]), aux(nums[1:]))


# if rob the first, can not rob the last -> [0, len(nums) - 1]
# if not rob the first, can rob the last -> [1, len(nums)]

nums = [1,2,3,1]
print(rob(nums))
