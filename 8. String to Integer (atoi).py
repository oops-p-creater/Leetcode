class Solution():
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        x=s.split(" ")[0]
        ans=""
        
        for i in range(len(x)):
            if(x[i].isnumeric()):
                ans=ans+x[i]
            elif(x[i]=="-" and i==0):
                ans=ans+x[i]
            elif(x[i]=="+" and i!=0):
                break
            elif(x[i]=="+" and i==0):
                continue
            else:
                break
        if(len(ans)==0 or (len(ans)==1 and ans[0]=="-")):
            return 0
        ans=int(ans)
        if(ans<-2**31):
            return -2**31
        if(ans>2**31-1):
            return 2**31-1
        return ans
            
s=Solution()
print(s.myAtoi(""))
            
        