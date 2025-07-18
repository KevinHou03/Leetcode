class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def allPossibleFBT(self, n):
        """
        :type n: int
        :rtype: List[Optional[TreeNode]]
        """
        # 注意，完全二叉树的节点数必须是奇数！！！
        # 递归方法会返回一棵树，最终返回所有树
        # 当用i个node构建左子树，就只能用n - 1 - i个node构建右子树
        # 当我们得到左右子树之后，用嵌套loop尝试所有的挂法
        if n % 2 == 0:
            return []
        memo = {}  # (i : [TreeNodes()]
        def construct(num):
            if num in memo:
                return memo[num]
            # 尝试所有的i，因为i个nodes被用来build左树，但是记住i必须是odd num
            res = []
            for i in range(1, num, 2):
                left = construct(i)
                right = construct(num - 1 - i)
                # nested loop trying to catch all the possible FBT
                for l in left:
                    for r in right:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        res.append(root)
            memo[num] = res
            return res





        return construct(n)




