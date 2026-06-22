class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        prefix=[]
        total_sum=0
        pivot_index=0
        right_sum=0
        for i in range(len(nums)):
            total_sum+=nums[i]
            prefix.append(total_sum)
        for j in range(len(nums)):
            if j!= 0:
                left_sum=prefix[j-1]
            else:
                left_sum=0
            right_sum=total_sum-nums[j]-left_sum
            if right_sum==left_sum:
                return j   
        return -1
                
        
