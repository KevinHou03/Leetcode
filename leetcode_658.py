import heapq


def findClosestElements(arr, k, x):
    """
    :type arr: List[int]
    :type k: int
    :type x: int
    :rtype: List[int]
    """
    # use priority queue / min heap
    # but the min heap method will be slow

    # q = []
    # for i in range(len(arr)):
    #     distance = abs(arr[i] - x)
    #     heapq.heappush(q, (-distance, -arr[i]))
    #     if len(q) > k:
    #
    #         heapq.heappop(q)
    #     print(q)
    # return sorted([-val for _, val in q])
    #

    # left, right = 0, len(arr) - k
    # while left < right:
    #     mid = (left + right) // 2
    #     if x - arr[mid] >  arr[mid + k] - x:
    #         left = mid + 1
    #     else:
    #         right = mid
    # return arr[left: left + k]

    left, right = 0, len(arr) - 1
    while right - left + 1 > k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1
    return arr[left:right + 1]




print(findClosestElements([1,2,3,4,5],4,3))