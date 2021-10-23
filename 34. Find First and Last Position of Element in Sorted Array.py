class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        ans=[]
        h=len(nums)-1
        if(len(nums)==0):
            return [-1,-1]
        if(len(nums)==2):
            if(nums[0]==target and nums[1]==target):
                return [0,1]
            else:
                return [-1,-1]
        
        while(l<h):
            if(l+1==h):
                if(nums[l]==target and nums[h]==target):
                    return [l,h]
                else:
                    return [-1,-1]
            m=(h+l)//2
            if(nums[m]==target):
                if(nums[m+1]==target):
                    return [m,m+1]
                elif(nums[m-1]==target):
                    return [m-1,m]
                else:
                    return [m,m]
            elif(nums[m]<target):
                l=m
            else:
                h=m
        return [-1,-1]
s=Solution()
print(s.searchRange([1],1))