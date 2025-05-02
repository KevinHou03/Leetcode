def findRepeatedDnaSequences(s):
    """
    :type s: str
    :rtype: List[str]
    """
    left = 0
    right = 9

    seq_count = {}
    res = set()

    for i in range(len(s) - 10 + 1):
        cur_seq = s[i : i + 10]
        seq_count[cur_seq] = seq_count.get(cur_seq, 0) + 1
        if seq_count[cur_seq] > 1:
            res.add(cur_seq)

    return list(res)
