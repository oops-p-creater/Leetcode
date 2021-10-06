class Solution():
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans=0
        if(len(s)==0):
            return 0
        for i in range(len(s)):
            l=[]
            c=0
            for j in range(i,len(s)):
                if(s[j] in l):
                    ans=max(ans,c)
                    break
                else:
                    l.append(s[j])
                c=c+1
                ans=max(ans,c)
        return ans
            
s=Solution()
print(s.lengthOfLongestSubstring("c"))