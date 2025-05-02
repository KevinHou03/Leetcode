# topological sort
import heapq
from collections import defaultdict

from sympy.physics.vector.printing import params


# construct undirected using dictionary

def undirected(edges):
    graph = defaultdict(list)
    for edge in edges:
        a, b = edge

        if a not in graph:
            graph[a] = []
        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


# 用dfs访问所有改节点的neighbors

def dfs(graph, vertice, visited):
    if vertice in visited:
        return False
    visited[vertice] = True

    for neighbor in graph[vertice]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


'''
dijkstra 算法
给定一个带权重的图（边权重为正），从起点出发，找出到所有其他节点的最短距离
每次都从当前未访问的节点中，选择**最短路径（当前已知最小距离）**的节点，更新它的邻居
所以我们要用minheap存放未访问的节点，这样每次才能在未访问节点中选出路径最短的那一个
'''
# nodes is [[,,],[,,][,,]...] => [a, b, wight]
def dijkstra(nodes, start_node, num_nodes):
    # first build the graph
    graph = defaultdict(list)
    for start, end, weight in nodes:
        graph[start].append((end, weight)) # use tuple
        # 单向图，不需要反着再来一次

    # 建立min heap
    min_heap = [(0,start_node)] # 分别为到这个节点当前的cost，以及当前节点
    dist = {} # 储存每个节点最短到达时间， 是最短。

    while min_heap:
        cost, cur_node = heapq.heappop(min_heap)
        if cur_node in dist:
            continue
        dist[cur_node] = cost
        for neighbor, weight in graph[cur_node]:
            if neighbor not in dist:
                heapq.heappush(min_heap, (cost + weight, neighbor))


    # return 的时候注意一点，不是说dist有元素就行，而是dist的元素数量必须等于所有元素数量，因为有可能会有元素无法被cover到
    # 还有一点，不能用len(nodes)去求有多少node，len(node)是边数。
    return max(dist.values()) if len(dist) == num_nodes else -1

# Dijkstra 算法允许“并行信号扩散”，但它是按“当前最短路径优先”来安排顺序的，不是真的并行，而是优先级驱动。






