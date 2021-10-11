class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        ans=""
        if(len(strs)<2):
            if(len(strs)==1):
                return strs[0]
            else:
                return ""
        a=strs[0]
        b=strs[1]
        for i in range(min(len(a),len(b))):
            if(a[i]==b[i]):
                ans=ans+a[i]
            else:
                break
        
        
        for i in range(2,len(strs)):
            if(strs[i]==""):
                return ""
            k=strs[i]
            if(ans==k[:len(ans)]):
                continue
            else:
                if(len(k)<len(ans)):
                    if(ans==k):
                        continue
                    else:
                        ans=ans[:len(k)]
                for j in range(min(len(ans),len(k))):
                    if(k[j]==ans[j]):
                        continue
                    else:
                        ans=ans[:j]
                        break
        return ans 
                
s=Solution()
print(s.longestCommonPrefix(["ac","ac","a","a"]))