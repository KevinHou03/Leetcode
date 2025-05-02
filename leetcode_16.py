import heapq
def threeSumClosest(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    nums.sort()
    closest = float('inf')
    res = -1

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1

        while left < right:
            cur_sum = nums[i] + nums[left] + nums[right]
            if abs(cur_sum - target) < closest:
                closest = abs(cur_sum - target)
                res = cur_sum

            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                return target
    return res
