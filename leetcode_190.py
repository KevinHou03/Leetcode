
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(n):
        result = 0
        #取最后一位
        for i in range(32):
            last_bit = n & 1
            #拼接 -> 先左移，把结果腾出空间，再拼接
            result = (result << 1) | last_bit
            n >>= 1
        return result


n = "00000010100101000001111010011100"
print(int(n, 2))

