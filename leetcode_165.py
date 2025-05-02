def compareVersion(version1, version2):
    """
    :type version1: str
    :type version2: str
    :rtype: int
    """
    version1 = version1.split('.')
    version2 = version2.split('.')
    print(version1)

    for i in range(max(len(version1), len(version2))):
        n1 = int(version1[i])
        n2 = int(version2[i])

        if n1 > n2:
            return 1
        if n1 < n2:
            return -1

    return 0