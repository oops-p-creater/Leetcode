class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ans=[]
        d={}
    
        for i in range(len(nums)):
            a=nums[i]
            for j in range(i+1,len(nums)):
                b=nums[j]
                l=j+1
                h=len(nums)-1
                while(l<h):
                    if(nums[l]+nums[h]+a+b==target):
                        k=str(i)+str(j)+str(l)+str(h)
                        if(([nums[i],nums[j],nums[l],nums[h]]) not in ans) :
                            ans.append([nums[i],nums[j],nums[l],nums[h]])
                            d[k]=1
                        l=l+1
                        h=h-1
                    elif(nums[l]+a+nums[h]+b<target):
                        l=l+1
                    else:
                        h=h-1
        return ans
s=Solution()
print(s.fourSum([1,0,-1,0,-2,2],0))