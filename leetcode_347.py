import heapq


def topKFrequent(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    # use dictionary
    memo = {} # num: freq
    min_heap = []
    for i in range(k):
        memo[nums[i]] = memo.get(nums[i], 0) + 1
    for num, freq in memo.items():
        heapq.heappush(min_heap, (num, freq))
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return [num for num, freq in min_heap]