from collections import defaultdict


def possibleBipartition(n, dislikes):
    """
    :type n: int
    :type dislikes: List[List[int]]
    :rtype: bool
    """
    # 首先构建图，把dislikes 里面的所有人 connect 所有人
    # 如果a不喜欢b，他们就是相同的颜色的node，因为他们两不能在一边
    # 只要根据dislikes构建就可以了，因为bipar本质是一条边两个node不在同一group，已经满足题意

    # construct the graph
    graph = defaultdict(list)
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)

    colors = [-1] * n
    def dfs(node, color):
        colors[node] = color
        for neighbor in graph[node]:
            if colors[neighbor] == -1: # 如果这个neighbor还没有染色，则可以dfs他去找，如果已经染色，就直接判断
                if not dfs(neighbor, 1 - color):
                    return False
            elif colors[neighbor] == color:
                return False

        return True

    for i in range(1, n + 1):
        if colors[i] == -1:
            if not dfs(i, 1):
                return False
    return True










