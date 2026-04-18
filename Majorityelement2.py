class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        elist=[]
        for y in freq:
            if freq[y]>len(nums)/3:
                elist.append(y)
        return elist
