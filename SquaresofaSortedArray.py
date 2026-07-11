class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left=0
        right=len(nums)-1
        pos=len(nums)-1   
        answer=[0]*len(nums)
        while left<=right:
            if abs(nums[left])>=abs(nums[right]):
                answer[pos]=nums[left]*nums[left]
                left+=1
            else:
                answer[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
        return answer
