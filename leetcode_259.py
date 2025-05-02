def threeSumSmaller(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    res = 0
    nums.sort()
    n = len(nums)

    for i in range(n - 2):
        j, k = i + 1, n - 1
        while j < k:
            if nums[i] + nums[j] + nums[k] < target:
                res += k - j
                j += 1
            else:
                k -= 1
    return res
