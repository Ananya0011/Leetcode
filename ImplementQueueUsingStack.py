class MyQueue(object):

    def __init__(self):
        self.stack=[]
        self.newstack=[]
        self.value=0

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)        

    def pop(self):
        """
        :rtype: int
        """
        while len(self.stack)>1:
            self.newstack.append(self.stack.pop())
        self.value=self.stack.pop()
        for i in range(len(self.newstack)):
            self.stack.append(self.newstack.pop())
        return self.value
        


    def peek(self):
        """
        :rtype: int
        """
        while len(self.stack)>1:
            self.newstack.append(self.stack.pop())
        self.value=self.stack.pop()
        self.stack.append(self.value)
        for i in range(len(self.newstack)):
            self.stack.append(self.newstack.pop())
        return self.value
        

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack:
            return False
        else:
            return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
