class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        a=[]
        b=[]
        for i in range(len(s)):
            if (s[i]=='#'):
                if not a:
                    continue
                else:
                    a.pop(-1)
            else:
                a.append(s[i])
        for j in range(len(t)):
            
            if (t[j]=='#'):
                if not b:
                    continue
                else:
                    b.pop(-1)
            else:
                b.append(t[j])
        if a==b:
            return True
        else:
            return False
