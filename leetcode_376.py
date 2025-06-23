def wiggleMaxLength(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 只关注趋势，比如正向的 nums[i + 1] > nums[i] 和反向的nums[i + 1] < nums[i]
    pos, neg = 1, 1
    # 第i个数字和第i-1个数字构成的趋势符合哪一个条件
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            pos = neg + 1
        elif nums[i] < nums[i-1]:
            neg = pos + 1

    return max(neg, pos)
