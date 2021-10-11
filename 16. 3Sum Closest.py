class Solution(object):
    def threeSumClosest(self, nums,target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        mini=9**10
        sum=9999999999999
        for i in range(len(nums)):
            a=nums[i]
            l=i+1
            h=len(nums)-1
            while(l<h):
                if(nums[l]+nums[h]+a==0):
                    l=l+1
                    h=h-1
                elif(nums[l]+a+nums[h]<target):
                    if(abs(target-(nums[l]+nums[h]+a))<mini):
                        mini=abs(target-(nums[l]+nums[h]+a))
                        sum=(nums[l]+nums[h]+a)
                    l=l+1
                else:
                    if(abs(target-(nums[l]+nums[h]+a))<mini):
                        mini=abs(target-(nums[l]+nums[h]+a))
                        sum=(nums[l]+nums[h]+a)
                    h=h-1
        return sum
s=Solution()
print(s.threeSumClosest([0,5,-1,-2,4,-1,0,-3,4,-5],1))