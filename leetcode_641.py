class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.q = [None] * k
        self.size = k
        self.cur_size = 0
        self.head = 0 # 指向队首元素的位置
        self.tail = 0 # 指向队尾下一个可插入的位置

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        _ _ 8 9 6 4 _ k = 7
        """
        if self.isFull():
            return False
        self.head = (self.head - 1 + self.size) % self.size
        self.q[self.head] = value
        self.cur_size += 1
        return True


    def insertLast(self, value):
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

    def deleteFront(self):
        """
        :rtype: bool
        _ _ 8 9 6 4 _ k = 7
        """
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.size
        self.cur_size -= 1
        return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        # self.tail = (self.head + self.cur_size - 2) % self.size
        self.cur_size -= 1
        return True



    def getFront(self):
        """
        :rtype: int
        """
        if self.isEmpty():
            return -1
        return self.q[self.head]

    def getRear(self):
        """
        :rtype: int
         _ _ 8 9 6 4 _ k = 7
        """
        if self.isEmpty():
            return -1
        return self.q[(self.head + self.cur_size - 1) % self.size]

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