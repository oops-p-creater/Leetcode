class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums)==0):
            return None
        elif(len(nums)==1):
            return 0
        
        i=0
        while(i<len(nums)-1):
            if(nums[i]==nums[i+1]):
                del nums[i+1]
            else:
                i=i+1
            
        return len(nums)
                
s=Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))