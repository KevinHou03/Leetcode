class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if s == "" or t == "":
            return ""
        count, window = {}, {}
        res = [-1, -1]
        min_len = float("inf")
        left = 0

        for c in t:
            count[c] = count.get(c, 0) + 1

        have, need = 0, len(count)
        for i in range(len(s)):
            window[s[i]] = 1 + window.get(s[i], 0)
            if s[i] in count and window[s[i]] == count[s[i]]:
                have += 1

            while have == need:
                cur_len = (i - left + 1)
                if cur_len < min_len:
                    min_len = cur_len
                    res = [left, i]
                window[s[left]] -= 1

                if s[left] in count and window[s[left]] < count[s[left]]:
                    have -= 1

                left += 1

        l, r = res
        return s[l: r + 1] if min_len != float("inf") else ""

