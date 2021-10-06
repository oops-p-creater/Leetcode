class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        
        """
        if(len(s)==1):
            return s
        
        maxNow=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                
                l=i
                h=j
                y=0
                if(s[l:h+1]==s[l:h+1][::-1]):
                    y=len(s[l:h+1])
                    
                if(y>len(maxNow)):
                    inl=i
                    inh=j
                    maxNow=s[l:h+1][::]
                    
        return(maxNow)
s=Solution()
print(s.longestPalindrome("laksjclknnnnkkkknnnn"))
                    
                
                
                
                
        