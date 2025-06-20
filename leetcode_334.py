def increasingTriplet(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    l = m = float('inf')
    for num in nums:
        if num > m:
            return True
        elif num <= l:
            l = num
        else:
            m = num
    return False

nums = [1,1,-2,6]
print(increasingTriplet(nums))




