def find132pattern(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # 暴力三重循环，时间太长
    # for i in range(0, len(nums) - 2):
    #     for j in range(i + 1, len(nums) - 1):
    #         if nums[i] > nums[j]:
    #             continue
    #         for k in range(j + 1, len(nums)):
    #             if nums[i] < nums[k] < nums[j]:
    #                  return True
    # return False


    stack = [] # pair, [num, minleft]
    curMin = nums[0]
    for n in nums[1:]:
        while stack and n >= stack[-1][0]:
            stack.pop()
        if stack and n > stack[-1][1]:
            return True

        stack.append([n, curMin])
        curMin = min(curMin, n)

    return False











nums = [-1,3,2,0]
print(find132pattern(nums))