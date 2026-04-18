class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq={}
        for x in nums:
            if x in freq:
                freq[x]+=1
            else:
                freq[x]=1
        maj=0
        for num in freq:
            if freq[num]>len(nums)/2:
                maj=num
        return maj 
