class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dc={}
        count=0
        for i in nums:
            if i in dc:
                dc[i]+=1
                return True
            else:
                dc[i]=1
        return False
        

