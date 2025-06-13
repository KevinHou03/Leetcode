def maxAdjacentDistance(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    max_adj_dis = 0
    start, end = nums[0], nums[-1]
    for i in range(len(nums) - 1):
        diff = abs(nums[i] - nums[i + 1])
        max_adj_dis = max(max_adj_dis, diff)
    max_adj_dis = max(max_adj_dis, abs(end - start))
    return max_adj_dis

nums = [-5,-10,-5]
print(maxAdjacentDistance(nums))


