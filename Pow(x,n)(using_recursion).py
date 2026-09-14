class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1

        if n < 0:
            result = self.myPow(x, (-1 * n) // 2)
        else:
            result = self.myPow(x, n // 2)

        if n % 2 == 0:
            ans = result * result
        else:
            ans = result * result * x

        if n > 0:
            return ans
        else:
            return 1 / ans
