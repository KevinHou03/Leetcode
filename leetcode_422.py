def validWordSquare(words):
    """
    :type words: List[str]
    :rtype: bool
    """
    rows = len(words)
    for i in range(rows):
        for j in range(len(words[i])):
            if words[i][j] != words[j][i] or j >= rows or i >= len(words[j]):
                return False
    return True



words = ["abcd","bnrt","crm","dt"]
print(validWordSquare(words))

["b  a  l. l",
 "a. s. e. e",
 "l. e. t",
 "l. e. p"]