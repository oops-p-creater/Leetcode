ans=[]
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        def recur(n,temp,o,c):
            global ans
            if(c==n and o==n):
                ans.append(temp[::])
                return
            if(o<n):
                temp=temp+"("
                recur(n,temp,o+1,c)
                temp=temp[:-1]
            if(o>c):
                temp=temp+")"
                recur(n,temp,o,c+1)
                temp=temp[:-1]
            return
        recur(n,"",0,0)
        return (ans)
s=Solution()
print(s.generateParenthesis(3))