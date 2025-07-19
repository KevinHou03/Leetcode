def myPow(x, n):
    is_neg = False
    if n < 0:
        is_neg = True
    a = x
    n = abs(n)
    for i in range(0, n - 1):
        x = x*a
    return x if is_neg is False else 1/x

print(myPow(2,-2))

def Pow(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / Pow(x, -n)
    return x * Pow(x, n - 1)

print(Pow(3, 4))

def myPow2(x, n):
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    half = myPow(x, n // 2)
    return half * half if n % 2 == 0 else half * half * x