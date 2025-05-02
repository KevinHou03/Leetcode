def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # memo = {}
    # for i in range(len(nums)):
    #     memo[nums[i]] = memo.get(nums[i], 0) + 1
    # return max(memo.keys(), key = memo.get)

    nums.sort()
    return nums[len(nums)//2]

nums = [3,3,4]
print(majorityElement(nums))