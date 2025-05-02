def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """

    left, right = 0, len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] < target:
            left += 1
        elif numbers[left] + numbers[right] > target:
            right -= 1
        else:
            return [left,right]

    return []

numbers = [2,7,11,15]
target = 9

print(twoSum(numbers, target))