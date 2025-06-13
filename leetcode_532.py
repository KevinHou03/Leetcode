from collections import Counter


def findPairs(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    # 1 1 3 4 5
    if k == 0:
        freq = Counter(nums)
        return sum(1 for count in freq.values() if count > 1)
    nums_uniq_list = sorted(set(nums))
    res = 0
    # 对每一个数字n，用二分法查找n + k是否在右侧
    def binary_search(target, nums):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return True
        return False
    for i in range(len(nums_uniq_list)):
        if binary_search(nums_uniq_list[i] + k, nums_uniq_list[i + 1:]):
            res += 1
    return res




nums = [1,2,3,4,5]
k = 1
print(findPairs(nums, k))


