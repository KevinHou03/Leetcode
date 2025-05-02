class union_find(object):
    def __init__(self, n):
        # 初始化并查集，创建 n 个独立的集合，每个节点的父亲是自己
        # :param n: 节点数量
        self.parent = list(range(n))  # parent[i] 表示 i 的父节点，初始时每个节点指向自己
        self.rank = [0] * n # rank[i] 记录以 i 为根的树的高度，用于优化合并操作


    def find(self, x):
        # 找到节点 x 所属的集合（即 x 的根节点
        # return 的是根节点，即所属集合的代表元
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # 如果x不是自己的根节点，那就递归的往上找
        return self.parent[x]

    def union(self, x, y):
        # 合并x y所属的两个集合
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y: # 这就表明这两个元素已经在同一个集合里了
            return False

        # union by rank 当合并两个集合时，总是将Rank 较小的树挂到Rank 较大的树上。
        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x # y的rank低， 所以y挂到x上， y的parent变成x（y本来没有parent）
        elif self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1
            # 只有这种情况rank会 + 1， 因为其他情况树的最大高度不变
        return True