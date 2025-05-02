class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # 在1， len（nums）的区间内，放到他应该放到的位置上，如果是x，就应该放在nums[x-1]这个位置上
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1

s = [36,31,34,37,32,33,]
Solution  = Solution()
print(Solution.firstMissingPositive(s))