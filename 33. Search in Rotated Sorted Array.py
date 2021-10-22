


class Solution(object):
    def binary(self,l,low,high,target):
        while(low<high):
            mid=(low+high+1)//2
            if(l[low]==target):
                return low
            elif(l[high]==target):
                return high
            elif(l[mid]==target):
                return mid
            elif(high==low+1):
                return None
            else:
                if(l[mid]<target):
                    low=mid
                else:
                    high=mid
        return None
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l=0
        k=0
        h=len(nums)-1
        if(l==h):
            if(target==nums[l]):
                return l
            else:
                return -1
        if(len(nums)==2):
            if(target==nums[0]):
                return 0
            elif(target==nums[1]):
                return 1
            else:
                return -1
            
            
            

        while(l<h):
            m=(h+l+1)//2
            if(nums[l]==target):
                return l
            elif(nums[h]==target):
                return h
            
            elif(nums[m]==target):
                return m
            elif(nums[m+1]<nums[m] and nums[m-1]<nums[m]):
                k=m+1
                break
            elif(nums[m+1]>nums[m] and nums[m-1]>nums[m]):
                k=m
                break
            else:
                if(nums[l]<nums[m] and nums[h]>nums[m]):
                    return self.binary(nums,0,len(nums)-1,target) or -1
                elif(nums[l]<nums[m]):
                    l=m
                else:
                    h=m
            
        
        return (self.binary(nums,k,len(nums)-1,target) or self.binary(nums,0,k,target)) or -1
s=Solution()
print(s.search([1,3,5],0))
                    
                    