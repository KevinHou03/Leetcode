import heapq
from collections import defaultdict


def networkDelayTime(times, n, k):
    """
    :type times: List[List[int]]
    :type n: int
    :type k: int
    :rtype: int
    """

    # build graph
    graph = defaultdict(list)
    for start, end, time in times:
        graph[start].append((end, time))

    dist = {}
    min_heap = [(0, k)]

    while min_heap:
        cur_time, cur_node = heapq.heappop(min_heap)
        if cur_node in dist:
            continue
        dist[cur_node] = cur_time
        for neighbor, n_time in graph[cur_node]:
            if neighbor not in dist:
                heapq.heappush(min_heap, (cur_time + n_time, neighbor))

    return max(dist.values()) if len(dist) == n else -1