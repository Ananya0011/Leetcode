class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        nstack=[]
        for i in range(len(tokens)):
            if tokens[i] in ['+','-','*','/']:
                a=int(nstack.pop())
                b=int(nstack.pop())
                if tokens[i]=='+':
                    nstack.append(a+b)
                elif tokens[i]=='-':
                    nstack.append(b-a)
                elif tokens[i]=='*':
                    c=a*b
                    nstack.append(c)
                elif tokens[i]=='/':
                    d=int(float(b)/a)
                    nstack.append(d)
            else:
                nstack.append(int(tokens[i]))
        return nstack.pop()
        



