class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        area=0
        stack=[]
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][0]>heights[i]:
                height, start = stack.pop()
                area=max(area,(height*(i-start)))
            stack.append((heights[i],start))
        while stack:
            height, start = stack.pop()
            area=max(area,(height*(len(heights)-start)))
        return area

                


                
