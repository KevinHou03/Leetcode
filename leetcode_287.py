'''
在有环链表里，用快慢指针便利，快慢指针相遇的地方一定在环内，但是具体在环的哪个位置不得而知
所以，当我们确定环内一个位置之后，如何找到环起点？
-> 我们让一个指针从头开始，另一个从相遇点（环内）开始，他们相遇的地方就是环头
'''
def findDuplicate(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    slow, fast = nums[0], nums[0]
    # 先找到环内一点
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    #此时相遇点在环内，执行第二步找到环头
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


nums = [1,3,4,2,2]
print(findDuplicate(nums))