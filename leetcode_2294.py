def partitionArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # 12356 - 2
    # 2245 - 0
    # 02 - 1
    #1225 - 2

    nums.sort()
    res = []
    _min, _max = 0, 0
    i = 0
    #
    # while i < len(nums):
    #     start = nums[i]
    #     res += 1
    #
    #     while i < len(nums) and nums[i] - start < k:
    #         i += 1
    #
    # return resR
    nums.sort()
    res = []
    _min = 0

    while _min < len(nums) and _max < len(nums):
        _max = _min
        while _max < len(nums) and nums[_max] - nums[_min] <= k:
            _max += 1
        res.append([nums[_min:_max]])
        _min = _max

    return len(res)

nums = [3,6,1,2,5] # 12356
k = 2
print(partitionArray(nums, k))


