class MyCircularQueue(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.size = k
        self.q = [None] * k
        self.cur_size = 0
        self.head = 0



    def enQueue(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        tail = (self.head + self.cur_size) % self.size
        self.q[tail] = value
        self.cur_size += 1
        return True


    '''
    在 循环队列（circular queue中，不能实打实地remove掉head指向的元素，因为这样会破坏它的固定长度 + 环形结构设计初衷。
    你只能remove head的指向，这样在enqueue中他就会自动顶替掉之前remove掉的元素
    '''
    def deQueue(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        # should remove the head
        self.head = (self.head + 1) % self.size
        self.cur_size -= 1
        return True



    def Front(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def Rear(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        tail = (self.head + self.cur_size - 1) % self.size
        return self.q[tail]

    def isEmpty(self):
        """
        :rtype: bool
        """
        return self.cur_size == 0

    def isFull(self):
        """
        :rtype: bool
        """
        return self.cur_size == self.size

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()