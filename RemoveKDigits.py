class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        stack=[]
        for i in range(len(num)):
            while stack and stack[-1]>num[i] and k>0:
                stack.pop()
                k-=1
            stack.append(num[i])
        while stack and k>0:
            stack.pop()
            k-=1
        else:
            s = ''.join(stack)
            s=s.lstrip('0')
            if not s:
                return "0"
            else:
                return s
