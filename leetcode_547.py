import collections


def findCircleNum(isConnected):
    """
    :type isConnected: List[List[int]]
    :rtype: int
    """

    def dfs(city, visited):
        # 把所有和city direct和indirectly相连的city全部加到visited里面去
        for neighbor in range(len(isConnected[city])):
            if isConnected[city][neighbor] == 1 and neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, visited)

    n = len(isConnected)
    visited = set()
    province_count = 0

    for i in range(n):
        if i not in visited:
            # get一个new prov
            visited.add(i)
            dfs(i, visited)
            province_count += 1

    return province_count


    # return dict

s1 =                        [[1,1,0],
                             [1,1,1],
                             [0,1,1]]


print(findCircleNum(s1))



