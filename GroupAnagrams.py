class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dc={}
        for i in strs:
            a=tuple(sorted(i))
            if a in dc:
                dc[a].append(i)
            else:
                dc[a]=[i]
        return list(dc.values())

            
