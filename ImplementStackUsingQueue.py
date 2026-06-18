class MyStack(object):

    def __init__(self):
        self.firstq=deque()
        self.popq=deque()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.firstq.append(x)

    def pop(self):
        """
        :rtype: int
        """
        for i in range(len(self.firstq)-1):
            self.popq.append(self.firstq.popleft())  
        value=self.firstq.popleft()
        for i in range(len(self.popq)):
            self.firstq.append(self.popq.popleft())
        return value

    def top(self):
        """
        :rtype: int
        """
        return self.firstq[-1]
    def empty(self):
        """
        :rtype: bool
        """
        if self.firstq:
            return False
        else:
            return True 


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
