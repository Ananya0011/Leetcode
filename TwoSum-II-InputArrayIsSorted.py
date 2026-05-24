class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        right=len(numbers)-1
        sum1=0
        while left<right:
            sum1=numbers[left]+numbers[right]
            if sum1>target:
                right-=1
            elif sum1<target:
                left+=1
            elif sum1==target:
                break
        return [left+1,right+1]


            
