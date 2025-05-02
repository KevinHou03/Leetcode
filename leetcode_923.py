def threeSumMulti(arr, target):
    """
    :type arr: List[int]
    :type target: int
    :rtype: int
    """
    count = 0
    arr.sort()
    for i in range(len(arr) - 2):
        left, right = i + 1, len(arr) - 1
        while left < right:
            cur_sum = arr[i] + arr[left] + arr[right]
            if cur_sum < target:
                left += 1
            elif cur_sum > target:
                right -= 1
            else:
                if arr[left] == arr[right]:
                    count += (right - left + 1) * (right - left) // 2
                    count %= (10**9 + 7)
                    break
                else:
                    l_count, r_count = 1, 1
                    while left + 1 < right and arr[left] == arr[left + 1]:
                        left += 1
                        l_count += 1
                    while right - 1 > left and arr[right] == arr[right - 1]:
                        right -= 1
                        r_count += 1
                    count +=  (l_count * r_count)
                    count %= (10**9 + 7)
                    left += 1
                    right -= 1

    return count
