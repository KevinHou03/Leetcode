def kthGrammar(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    0
    01
    0110
    01101001
    ...
    """
    table = [0]
    def helper(cur_n, cur_table):
        if cur_n == n:
            return cur_table[k - 1]
        new_table = []
        for i in range(len(cur_table)):
            if cur_table[i] == 0:
                new_table.append(0)
                new_table.append(1)
            else:
                new_table.append(1)
                new_table.append(0)
        return helper(cur_n + 1, new_table)

    return helper(1, table)

print(kthGrammar(2, 2))

# 可以跑，但是内存会爆炸，因为你每次构建新的table
# 所以可以用二叉树思维，
'''
n=1:          0
n=2:        0   1
n=3:      0  1 1  0
n=4:    0 1 1 0 1 0 0 1
n=5  01 10 10 01 10 01 01 10

'''
def kthGrammar2(n, k):
    if n == 1:
        return 0
    father = kthGrammar(n - 1, (k + 1) // 2)
    # 判断son是左子还是右子，1， 3， 5， 7都是左，剩下都是右
    _even = (k % 2 == 0) # if k % 2 = 0, even = False 为左子
    if _even:
        return 1 if father == 0 else 0
    else:
        return 0 if father == 0 else 1









