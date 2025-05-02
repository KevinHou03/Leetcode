'''
输入一个列表，生成该列表中所有可能的排列（不允许重复使用元素，排列顺序不同算不同结果）。
'''
print("全排列")
def permutaion(nums):

    res = []
    used = [False] * len(nums)
    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)

            #撤销选择
            path.pop()
            used[i] = False

    backtrack([])
    print(len(res))
    return res


s = [1,2,3,4,5]
res = permutaion(s)
res.sort()
print(res)

print("partial排列")
def partial_permutaion(nums, k):

    res = []
    used = [False] * len(nums)
    def backtrack(path):
        if len(path) == k:
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            path.append(nums[i])
            backtrack(path)

            #撤销选择
            path.pop()
            used[i] = False

    backtrack([])
    print(len(res))
    return res



s2 = [1,2,3,4,5]
res2 = partial_permutaion(s2,3)
res2.sort()
print(res2)






