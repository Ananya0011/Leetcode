class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new=[0]*len(nums)
        suffix=[0]*len(nums)
        suffix[-1]=1
        prefix=[0]*len(nums)
        prefix[0]=1
        for i in range(len(nums)-2,-1,-1):
            suffix[i]=suffix[i+1]*nums[i+1]
        for j in range(1,len(nums)):
            prefix[j]=prefix[j-1]*nums[j-1]
        for k in range(len(nums)):
            new[k]=suffix[k]*prefix[k]
        return new
                
                
