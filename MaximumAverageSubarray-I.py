class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        left=0
        right=-1
        sum1=0
        max_avg=float('-inf')
        for i in nums:
            sum1+=i
            right+=1
            while (right-left+1)>k:
                sum1-=nums[left]
                left+=1
            if (right-left+1)==k:
                max_avg=max(max_avg,(float(sum1)/k))
        return max_avg
            
