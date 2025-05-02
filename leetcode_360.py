def sortTransformedArray(nums, a, b, c):
    """
    :type nums: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: List[int]
    """
    res = []
    for num in nums:
        res.append(a * num**2 + b * num + c)
    return sorted(res)

print(sortTransformedArray([-4,-2,2,4], 1,3,5))

def sortTransformedArray2(nums, a, b, c):

    sym_axis = (-1 * b) / (2 * a)
    res = [0] * len(nums)
    # 如果a大于0， 开口向上，约往两端越大
    def f(num):
        return a * num**2 + b * num + c
    if a > 0:
        index = len(nums) - 1
        left, right = 0, len(nums) - 1
        while left <= right:
            if f(nums[left]) > f(nums[right]):
                res[index] = f(nums[left])
                left += 1
            else:
                res[index] = f(nums[right])
                right -= 1
            index -= 1
    # 如果a小于0， 开口向下，约往两端越小
    else:
        left, right = 0, len(nums) - 1
        while left <= right:
            index = 0
            if f(nums[left]) < f(nums[right]):
                res[index] = f(nums[left])
            else:
                res[index] = f(nums[right])
            index += 1
    return res

print(sortTransformedArray2([-4,-2,2,4], 1,3,5))
