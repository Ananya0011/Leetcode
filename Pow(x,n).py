class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        half=pow(x,n//2)
        if n%2==0:
            return half*half
        return half*half*x
