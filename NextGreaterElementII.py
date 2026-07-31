class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        narray=2*nums
        answer=[-1]*len(narray)
        n=len(nums)
        nstack=[]
        for i in range(len(narray)-1,-1,-1):
            if not nstack:
                nstack.append(narray[i])
            else:
                while nstack and narray[i]>=nstack[-1]:
                    nstack.pop()
                if nstack:
                    answer[i]=nstack[-1]
                else:
                    answer[i]=-1
                nstack.append(narray[i])
        return answer[:n]
