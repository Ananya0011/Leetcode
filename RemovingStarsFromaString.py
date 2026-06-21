class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        st=[]
        for i in range(len(s)):
            if s[i]!='*':
                st.append(s[i])
            else:
                st.pop()
        result="".join(st)
        return result

