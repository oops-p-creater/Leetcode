class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        maxi=nums[-1]
        ind=len(nums)-1
        f=0
        for i in range(len(nums)-1,-1,-1):
            if nums[i-1]<nums[i]:
                ind = i-1
                maxi=nums[i-1]
                break
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]>maxi):
                nums[i],nums[ind]=nums[ind],nums[i]
                f=1
                nums[:]=nums[:ind+1]+sorted(nums[ind+1:])
                break
        if(f==0):
            nums.sort()
        return nums
s=Solution()
print(s.nextPermutation([2,7,5]))