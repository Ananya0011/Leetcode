from collections import deque
class RecentCounter(object):

    def __init__(self):
        self.request=deque()
    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.request.append(t)
        while True:
            if self.request[0]<t-3000:
                self.request.popleft()
            else:
                break
        return len(self.request)

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
