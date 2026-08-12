class Solution(object):
    def sumSubarrayMins(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        min_sum=0
        ms=[]
        for i in range(len(arr)):
            left_boundary=0
            right_boundary=0
            right_choice=0
            left_choice=0
            while ms and arr[ms[-1]]>arr[i]:
                pvalue=ms.pop()
                right_boundary=i
                if ms:
                    left_boundary=ms[-1]
                else:
                    left_boundary=-1
                left_choice=pvalue - left_boundary
                right_choice=right_boundary-pvalue
                min_sum+=arr[pvalue]*right_choice*left_choice  
            ms.append(i)
        while ms:
            pvalue=ms.pop()
            left_boundary=0
            right_boundary=0
            right_choice=0
            left_choice=0
            right_boundary=len(arr)
            if ms:
                left_boundary=ms[-1]
            else:
                left_boundary=-1
            left_choice=pvalue - left_boundary
            right_choice=right_boundary-pvalue
            min_sum+=arr[pvalue]*right_choice*left_choice
        return min_sum % 1000000007
