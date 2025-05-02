def trailingZeroes(n):
    """
    :type n: int
    :rtype: int
    """

    #每当分离出一个5和2，就会多一个0
    #对于每个factorial来说，2比5多，所以只要数有多少个5，就知道有多少个0

    count = 0
    while n >= 5:
        count += n // 5
        n //= 5
    return count