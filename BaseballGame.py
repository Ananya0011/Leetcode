class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        record=[]
        sum=0
        for op in operations:
            if op=='C':
                if not record:
                    return 0
                else:
                    record.pop()
            elif op == 'D':
                if not record:
                    return 0
                else:
                    record.append(int(2*record[-1]))
            elif op=='+':
                record.append(int(record[-2]+record[-1]))
            else:
                record.append(int(op))
        for i in range(len(record)):
            sum+=record[i]
        return sum
            
