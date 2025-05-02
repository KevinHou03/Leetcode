def countGoodTriplets(arr, a, b, c):
    """
    :type arr: List[int]
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    arr_len = len(arr)
    ans = 0
    for i in range(arr_len):
        for j in range(i + 1, arr_len):
            for k in range(j + 1, arr_len):
                if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                    ans += 1
    return ans

