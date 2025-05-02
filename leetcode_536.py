# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def str2tree(s):
        """
        :type s: str
        :rtype: Optional[TreeNode]
        """

        # use stack
        # stack[-1]永远是当前节点的father
        # 永远先往left append，不行再right
        stack = []
        i = 0

        while i < len(s):
            if s[i] == ')': # pop.return to the last level of the tree
                stack.pop()
                i += 1
            elif s[i].isdigit() or s[i] == '-': # 如果是数字，就记录下来
                start = i
                i += 1
                while i < len(s) and s[i].isdigit():
                    i += 1
                val = int(s[start:i])
                new_node = TreeNode(val)
                if stack:
                    # 注意栈顶 也就是stack【-1】永远是该节点的father节点,可以append left则left，不行再right，所以先检查left
                    father_node = stack[-1]
                    if not father_node.left: #没有左子
                        father_node.left = new_node
                    else:#有左子
                        father_node.right = new_node
                stack.append(new_node)
            else: # 如果是(
                i += 1

            return stack[0]



