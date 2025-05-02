from collections import defaultdict


def findRedundantConnection(edges):
    """
    :type edges: List[List[int]]
    :rtype: List[int]
    """
    # 如果加上这条边便会形成一个环，那么答案就是这条边 题目想找到形成环的最后一条边
    # 利用dfs检测是否生成环
    graph = defaultdict(list)
    def dfs(u, v, visited):
        if u in visited: # 如果又回到起点，说明死胡同死循环，返回false
            return False
        if u == v: # 如果可以到target，即u可以通过一些其他路线到v，则说明加入此条边会形成环，返回true
            return True

        visited.add(u)

        for neighbor in graph[u]:
            if dfs(neighbor, v, visited):
                return True
        return False

    '''
    如何找到那一条促使环形成的边？
    在我们加入一条边，注意是一条边u-v之前
    检查u可不可以通过一些其他路径到v
    如果可以，那么u-v一加入，就形成环了
    
    '''
    for edge in edges:
        u, v = edge # 两个节点
        if u in graph and v in graph:
            if dfs(u, v, set()):
                return [u, v] # 如果形成环了，则返回
        graph[u].append(v)
        graph[v].append(u)
    return []


def findRedundantConnection2(edges): # use union find
    parent = [ i for i in range(len(edges) + 1)]
    ranks = [1] * (len(edges) + 1)

    def find(n): # given n, find its parent
        # if parent[n] != n:
        #     parent[n] = find(parent[n])
        # return parent[n]
        p = parent[n]
        while p != parent[p]:
            parent[p] = parent[parent[p]]
            p = parent[p]
        return p

    def union(n1, n2):
        root1 = find(n1)
        root2 = find(n2)

        if root1 == root2:
            return False # now we know we find a redundant edge

        if ranks[root1] > ranks[root2]:
            parent[root2] = root1
        elif ranks[root1] < ranks[root2]:
            parent[root1] = root2
        else:
            parent[root1] = root2
            ranks[root2] += 1
        return True

    for n1, n2 in edges:
        if not union(n1, n2):
            return [n1, n2]

