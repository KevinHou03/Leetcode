# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def splitBST(root, target):
        """
        :type root: Optional[TreeNode]
        :type target: int
        :rtype: List[Optional[TreeNode]]
        """
        # 用recursion
        '''
        1. 利用BST性质，如果该node.val < target， 那么node及node左边都应该同时放到第一颗树
        2. 在上面的情况下，右子树需要递归的讨论，因为可能存在 node.right > target的情况
        
        3. 如果node.val > target, 那么右子树全部被放到第二颗树，左子树同样需要递归的讨论
        
        '''

        def helper(node):  # 返回[left_sub, right_sub]
            if not node:
                return [None, None]
            if node.val <= target:
                left_sub, right_sub = helper(node.right) # left_sub:你某个右边邻居的左边邻居， right_sub:你某个左边邻居的右边邻居
                node.right = left_sub # 把拆出来仍属于左子树的部分挂回当前节点右边，保持结构尽可能不变，在同一个子树里的父子关系要尽量保留
                #在node.val <=target 的时候right_sub是node的右子树拆出的左子树部分，还是会比node要大，所以要挂在node右边
                # left_sub 是 node.right 中 ≤ target 的部分（属于左子树)所以它要挂在 node.right 上（和 node 一起形成左子树）
                return [node, right_sub]
            elif node.val > target:
                left_sub, right_sub = helper(node.left)
                node.left = right_sub
                return [left_sub, node]

        return helper(root)

