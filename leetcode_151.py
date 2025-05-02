def reverseWords(s):
    """
    :type s: str
    :rtype: str
    """
    s = s.strip()

    s2 = s.split() # without argument: remove all the space automatically while still splitting

    s2.reverse()
    return " ".join(s2)



s = " hello world "
print(reverseWords(s))