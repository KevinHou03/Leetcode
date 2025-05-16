import heapq
from collections import deque, Counter


def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    # freq_map = {}
    # res = ""
    # for char in s:
    #     if char not in freq_map:
    #         freq_map[char] = 1
    #     else:
    #         freq_map[char] += 1
    # q = []
    # for char, freq in freq_map.items():
    #     heapq.heappush(q, [-freq, char])
    #
    # while q:
    #     freq, char = heapq.heappop(q)
    #     for i in range(-freq):
    #         res += char
    # return res


# this is much much faster
    freq_map = Counter(s)
    sorted_chars = sorted(freq_map.items(), key=lambda x: -x[1])
    return ''.join(char * freq for char, freq in sorted_chars)


print(frequencySort("abba"))


print(frequencySort("accccbba"))

