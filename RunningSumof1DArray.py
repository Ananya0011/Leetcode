class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        val=0
        for i in nums:
            val+=i
            result.append(val)
        return result
