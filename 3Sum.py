class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        new_list=[]
        nums.sort()
        target=0
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]>target:
                    right-=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif nums[i]+nums[left]+nums[right]<target:
                    left+=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                else:
                    sublist=[nums[i],nums[left],nums[right]]
                    new_list.append(sublist)
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
        return new_list
