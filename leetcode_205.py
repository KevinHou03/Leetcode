def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    _map = {}
    for i in range in range(len(e)):
        if s[i] not in _map.keys():
            _map[i] = t[i]
        else:
            if _map[i] != t[i]:
                return False


print(int('a'))