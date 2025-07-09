def isBipartite(graph):
    """
    :type graph: List[List[int]]
    :rtype: bool
    """
    # bipartisan问题，如果每一条边的两端都能用不同的两个颜色表示，则为bipartite
    # -1 未染色 0/1

    n = len(graph)
    colors = [-1] * n

    def dfs(node, color): # 该node，以及他是什么颜色
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == -1:
                if not dfs(neighbor, 1 - color):  # 对A的邻居递归，一定要assign和A不一样的颜色
                    return False # 如果是同一个颜色，返回false
            elif colors[neighbor] == color: # 如果A的邻居颜色和A一样
                return False#同理

        return True

    for i in range(n):
        if colors[i] == -1:
            if not dfs(i, 0):
                return False
    return True