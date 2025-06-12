def findNthDigit(n):
    """
    :type n: int
    :rtype: int
    """
    # -9/ -90/ -900...
    #一位数 两位数 三位数 四位数。。。。
    initial = 9
    digit_count = 1
    start = 1

    while n > initial * digit_count:
        n = n - initial * digit_count
        initial *= 10
        digit_count += 1
        start *= 10

    num = str(start + (n - 1) // digit_count)
    return int(num[(n - 1) % digit_count])

print(findNthDigit(11))