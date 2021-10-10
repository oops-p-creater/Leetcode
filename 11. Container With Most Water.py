class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxi=0
        l=0
        h=len(height)-1
        while(l<h):
            maxi=max(min(height[l],height[h])*(h-l),maxi)
            if(height[l]<height[h]):
                l=l+1
            else:
                h=h-1
            
        return maxi