def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """


    '''
    1.从右到左找到第一个i < i + 1的元素，i是pivot
    2.再从右到左找到第一个大于i的元素，k，k是successor
    3.swap i and k
    4. reverse i索引右边的部分
    '''

    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            pivot = i
            break
    for j in range(len(nums) - 1, -1, -1):
        if nums[j] > nums[pivot]:
            successor = j
            break
    nums[pivot], nums[successor] = nums[successor], nums[pivot]

    left = pivot + 1
    right = len(nums) - 1
    while left <= right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

