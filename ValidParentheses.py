class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=[]
        pairs={')':'(','}':'{',']':'['}
        for i in s:
            if i in '([{':
                stack.append(i)
            elif i in ')]}':
                if not stack:
                    return False
                elif stack[-1]==pairs[i]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False

