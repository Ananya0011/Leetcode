class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ls=set()
        left=0
        right=-1
        maxlen=0
        for x in s:
            while x in ls:
                ls.remove(s[left])
                left+=1
            ls.add(x)
            right+=1
            maxlen=max(maxlen,right-left+1)
        return maxlen

