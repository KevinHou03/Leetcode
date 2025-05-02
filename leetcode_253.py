import heapq
def minMeetingRooms(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    #这个方法只能过一部分case
    # intervals.sort()
    # rooms = 1
    # for i in range(1, len(intervals)):
    #     start, end = intervals[i]
    #
    #     if start < intervals[i-1][1]:
    #         rooms +=1
    # return rooms

    intervals.sort()
    min_heap = []

    for interval in intervals:
        if len(min_heap) > 0 and interval[0] >= min_heap[0]:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, interval[1])
    return len(min_heap)


r = [[9,10],[4,9],[4,17]]
r.sort()
print(r)
print(minMeetingRooms(r))