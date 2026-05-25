class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        left=len(s)-1
        right=len(t)-1
        dcs={}
        dct={}
        if len(s) != len(t):
            return False
        while left >=0 or right>=0:
            if s[left] in dcs:
                dcs[s[left]]+=1
            else:
                dcs[s[left]]=1
            if t[right] in dct:
                dct[t[right]]+=1
            else:
                dct[t[right]]=1
            left -= 1
            right -= 1
        if dcs != dct:
            return False
        else:
            return True
        
        
