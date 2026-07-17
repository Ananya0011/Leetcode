class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        water=0
        count=0
        max_left=[0]*len(height)
        max_left[0]=height[0]
        max_right=[0]*len(height)
        max_right[len(height)-1]=height[len(height)-1]
        if (len(height)-1)<0:
            return 0
        if (len(height)-1)==1:
            return height[len(height)-1]
        for i in range(1,len(height)-1):
            max_left[i]=max(max_left[i-1],height[i])
        for j in range(len(height)-2,0,-1):
            max_right[j]=max(max_right[j+1],height[j])
        for k in range(len(height)):
            water=min(max_right[k],max_left[k])-height[k]
            if water<0:
                continue
            else:
                count+=water
        return count
