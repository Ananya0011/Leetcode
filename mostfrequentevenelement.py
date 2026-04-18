class Solution(object):
    def mostFrequentEven(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        freq = {}
        for x in nums:
            if x % 2 == 0:
                if x in freq:
                    freq[x] += 1
                else:
                    freq[x] = 1
        best = -1
        max_freq = 0

        for num in freq:
            if freq[num] > max_freq:
                max_freq = freq[num]
                best = num
            elif freq[num] == max_freq and num < best:
                best = num
        return best


                        
        
