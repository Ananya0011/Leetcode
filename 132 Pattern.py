class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        small=float('inf')
        stack=[]
        for i in range(len(nums)):
            current=nums[i]
            while stack and stack[-1][0]<current:
                small= min(small,stack[-1][1])
                stack.pop()
            if stack and stack[-1][1]<current<stack[-1][0]:
                return True
            if small != float('inf'):
                stack.append([current,small])
            small=min(small,current)
        return False
