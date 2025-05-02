def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    memo = {}
    for num in nums:
        memo[num] = memo.get(num, 0) + 1
    return [key for key in memo.keys() if memo[key] > len(nums) // 3]


nums = [3,2,3]
print(majorityElement(nums))