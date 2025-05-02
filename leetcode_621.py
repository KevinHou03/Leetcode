def leastInterval(tasks, n):
    """
    :type tasks: List[str]
    :type n: int
    :rtype: int
    """
    # 尽量找到label不一样的task
    # 在任意一次idle之前尽可能的完成最多的task

    freq_map = {}
    for task in tasks:
        freq_map[task] = freq_map.get(task, 0) + 1

    pattern = max(freq_map.values())
    max_count = sum(1 for task in freq_map if freq_map[task] == pattern)  # Count tasks with max frequency
    return max(len(tasks), (pattern - 1) * (n + 1) + max_count)



