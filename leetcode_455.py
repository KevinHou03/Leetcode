def findContentChildren(g, s):
    """
    :type g: List[int]
    :type s: List[int]
    :rtype: int
    """
    g.sort()
    s.sort()
    res = 0

    kid_index, cookie_index = 0, 0
    while kid_index < len(g) and cookie_index < len(s):
        if g[kid_index] <= s[cookie_index]:
            res += 1
            kid_index += 1
        cookie_index += 1
    return res

g = [1,2,3]
s = [1,1]
print(findContentChildren(g, s))



