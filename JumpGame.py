class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        si=nums[0]
        for i in range(len(nums)):
            if si<i:
                return False
                break
            elif si==len(nums)-1 or si>len(nums)-1:
                return True
                break  
            si=max(si,i+nums[i])
       
