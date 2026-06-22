class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        stack=[]
        if len(s)>len(t):
            return False 
        if not t and s:
            return False
        for i in s:
            stack.append(i)
        for j in range(len(t)-1,-1,-1):
            if not stack:
                return True
            if t[j]==stack[-1]:
                stack.pop()
        if not stack:
            return True
        else:
            return False

##did the code idea and structure on my own yayyyy
        
