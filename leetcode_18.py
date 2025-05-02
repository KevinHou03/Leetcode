def fourSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    #固定两个指针，用双指诊查询剩下的值，complexity oN^3
    nums.sort()
    res = []
    for i in range(len(nums) - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums) - 2):
            if j > 0 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, len(nums) - 1

            while left < right:
                cur_sum = nums[i] + nums[j] + nums[left] + nums[right]
                if cur_sum < target:
                    left += 1
                elif cur_sum > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
    return res
