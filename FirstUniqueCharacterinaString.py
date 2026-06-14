class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dc={}
        for i in s:
            if i in dc:
                dc[i]+=1
            else:
                dc[i]=1
        for j in range(len(s)):
            if dc[s[j]]==1:
                return j
        return -1
