class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        dc={}
        left=0
        right=-1
        max_freq=0
        for i in s:
            if i in dc:
                dc[i]+=1
            else:
                dc[i]=1
            right+=1
            max1=max(dc.values())
            while (right-left+1)-max1>k:
                dc[s[left]]-=1
                left+=1
                max1=max(dc.values())
            max_freq=max(max_freq,right-left+1)
        return max_freq
            
                

    
