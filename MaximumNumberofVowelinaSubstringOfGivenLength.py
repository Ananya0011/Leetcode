class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        left=0
        right=0
        vowel_count=0
        max_vowel=0
        for right in range(len(s)):
            if (right-left+1)>k:
                if s[left] in "aeiou":
                    vowel_count-=1
                left+=1
            if s[right] in "aeiou":
                vowel_count+=1
            if (right-left+1)==k:   
                max_vowel=max(max_vowel,vowel_count)
        return max_vowel
            
            

        
