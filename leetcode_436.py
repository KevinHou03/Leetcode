def findRightInterval(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: List[int]
    """

    aux = sorted((interval[0], i) for i, interval in enumerate(intervals))
    res = []
    for interval in intervals:
        end = interval[1]
        aux_start, aux_end = 0, len(aux)
        while aux_start < aux_end:
            mid = (aux_start + aux_end) // 2
            if aux[mid][0] < end:
                aux_start = mid + 1
            else:
                aux_end = mid
        #判断是否存在，如果不存在的话，所以的start都比这个end小，aux_start会跑到最右边去
        if aux_start >= len(aux):
            res.append(-1)
        else:
            res.append(aux[aux_end][1]) # 二分法查找完后left和right都会在同一个位置，也就是第一个满足条件的位置，如果没有查找到，那么left会一直向右边移动，直到 = len(aux)
    return res

intervals = [[3,4],[2,3],[1,2]]
print(findRightInterval(intervals))
