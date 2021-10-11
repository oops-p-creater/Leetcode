class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        for i in range(len(nums)):
            a=nums[i]
            l=i+1
            h=len(nums)-1
            while(l<h):
                if(nums[l]+nums[h]+a==0):
                    k=[nums[i],nums[l],nums[h]]
                    if k not in ans:
                        ans.append([nums[i],nums[l],nums[h]])
                    l=l+1
                    h=h-1
                elif(nums[l]+a+nums[h]<0):
                    l=l+1
                else:
                    h=h-1
        return ans
s=Solution()
print(s.threeSum([3,0,-2,-1,1,2]))