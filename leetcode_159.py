def lengthOfLongestSubstringTwoDistinct(s):
    """
    :type s: str
    :rtype: int
    """
    _map = {}
    left = 0
    max_l = 0

    for right in range(len(s)):
        _map[s[right]] = _map.get(s[right], 0) + 1

        while len(_map) > 2:
            _map[s[left]] -= 1
            if _map[s[left]] == 0:
                del _map[s[left]]
            left += 1
        max_l = max(max_l, right - left + 1)

    return max_l
