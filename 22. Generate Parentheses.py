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
            else:
                if(o>c):
                    
                    recur(n,temp+")",o,c+1)
                if(o<n):
                    
                    recur(n,temp+"(",o+1,c)
                
                
        recur(n,"",0,0)
        return (ans)
s=Solution()
print(s.generateParenthesis(3))