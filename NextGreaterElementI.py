class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nstack=[]
        answer=[0]*len(nums2)
        c_ans=[0]*len(nums1)
        for i in range(len(nums2)-1,-1,-1):
            if not nstack:
                nstack.append(i)
                answer[i]=-1
            else:
                while nstack and nums2[i]>nums2[nstack[-1]]:
                    nstack.pop()
                if nstack:
                    answer[i]= nums2[nstack[-1]]
                else:
                    answer[i]=-1
                nstack.append(i)
        val_to_answer = dict(zip(nums2, answer))
        for j , nums in enumerate(nums1):
            c_ans[j]=val_to_answer[nums]
        return c_ans
