def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    # 用stack来解决，一个stack储存所有的nums，另一个储存所有[]之前的字符串
    '''
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"
    0. num = 3
    1. num_stack = [3], str_stack = [""], cur = "", num = 0
    2. cur_str = "a" 
    3. k = 3, _str = "", cur_str = "" + 3 * "a" = "aaa"
    
    4. num = 0 * 10 + 2 = 2
    5. num_stack = [2], str_stack = ["aaa"], cur = "aaa", num = 0
    6. cur_str = b
    7. cur_str = bc
    8. k = 2 _str = "aaa" cur_str = _str + cur_str * k = bcbc
    '''
    num_stack = []
    str_stack = [] # 储存的是遇见"]"之前的str
    num = 0 # 处理multi-digit situation 例如 12, 29
    cur_str = ""
    for c in s:
        if c.isdigit():
            num = num * 10 + int(c)
        elif c == '[':
            num_stack.append(num)
            str_stack.append(cur_str)
            cur_str = ""
            num = 0
        elif c == ']':
            k = num_stack.pop()
            _str = str_stack.pop()
            cur_str = _str + k * cur_str
        else: # in abcde....
            cur_str += c

    return cur_str

'''
    
    Input: s = "3[a2[c]]"
    Output: "accaccacc"
    
    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
'''
def decodeString_recur(s):
    """
    :type s: str
    :rtype: str
    """
    def decode(i):
        # 遇 [ 就递归，遇 ] 就 return i+1
        res = ""
        num = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            elif s[i] == '[': # 这个时候才开始recursion,recursively计算[]里面的部分
                cur_str, i = decode(i)
                res += num * cur_str
                num = 0
            elif s[i] == ']': # 这个时候return，代表一个递归子串的结束
                return res, i + 1
            else:
                res += s[i]
                i += 1
        return res, i

    return decode(0)[0]

'''
s = "3[a2[c]]"
第一次调用：decode(0)
初始：res = "", num = 0

s[0] = '3' → num = 3

s[1] = '[' → 进入递归，调用 decode(2) 来处理 [...] 中的内容

第二次调用：decode(2)
初始：res = "", num = 0

s[2] = 'a' → res = "a"

s[3] = '2' → num = 2

s[4] = '[' → 进入递归，调用 decode(5) 来处理 [...]

第三次调用：decode(5)
初始：res = "", num = 0

s[5] = 'c' → res = "c"

s[6] = ']' → 返回 ("c", 7)

⬆️ 回到第二次调用 decode(2)：

拿到结果 "c", 当前 num = 2

更新：res = "a" + 2 * "c" = "acc"

s[7] = ']' → 返回 ("acc", 8)

⬆️ 回到第一次调用 decode(0)：

拿到结果 "acc", 当前 num = 3

更新：res = "" + 3 * "acc" = "accaccacc"

i = 8，已到末尾 → 返回 ("accaccacc", 8)
'''









