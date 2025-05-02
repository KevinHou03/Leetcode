def isOneEditDistance(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if abs(len(s) - len(t)) > 1:
        return False

    if len(s) - len(t) == 0: # 只能有一个不同。 acb ab
        count = 0
        for i in range(len(s)):
            if s[i] != t[i]:
                count += 1
        return count == 1

    elif len(s) - len(t) == 1:# 必须删掉一个
        count = 0
        for j in range(len(s)):
            if s[j] not in t:
                count += 1
        return count == 1

    else:# 加一个 ab acb
        count = 0
        for k in range(len(s)):
            if s[k] not in t:
                count += 1
        return count == 1




