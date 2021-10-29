
class Solution(object):
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if(sum(candidates)<target):
            return []
        if(sum(candidates)==target):
            return [candidates]
        def fun(candidates,target,curr,i,ans):
            if(sum(curr)>target):
                return
            if(sum(curr)==target):
                if(curr not in ans):
                    ans.append(curr[::])
            if(i>=(len(candidates))):
                return
            curr.append(candidates[i])
            i=i+1
            fun(candidates,target,curr,i,ans)
            curr.pop()
            
            fun(candidates,target,curr,i,ans)
            return
        ans=[]
        candidates.sort()
        fun(candidates,target,[],0,ans)
        return ans
s=Solution()
print(s.combinationSum2([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],30))