def findMissingRanges(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[List[int]]
    """
    res = []
    _min,_max = float('inf'), float('-inf')
    i = lower
    nums = set(nums)
    while i <= upper:
        while i not in nums and i <= upper:
            _min = min(_min, i)
            _max = max(_max, i)
            i += 1
        if _min != float('inf'):
            res.append([_min, _max])
        _min, _max = float('inf'), -float('inf')
        i += 1
    return res


nums = [0,1,3,50,75]
print(findMissingRanges(nums,0,99))