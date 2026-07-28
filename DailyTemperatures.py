class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[0]*len(temperatures)
        nstack=[]
        for i in range(len(temperatures)-1,-1,-1):
            if  not nstack:
                nstack.append(i)
            else:
                while nstack and temperatures[i]>=temperatures[nstack[-1]]:
                    nstack.pop()
                if not nstack:
                    answer[i]=0
                    nstack.append(i)
                else:
                    answer[i]=nstack[-1]-i
                    nstack.append(i)
        return answer


