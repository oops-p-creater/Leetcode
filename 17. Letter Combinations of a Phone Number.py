class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        temp=[]
        d={
            '2':"abc",
            '3':"def",
            '4':"ghi",
            '5':"jkl",
            '6':"mno",
            '7':"pqrs",
            '8':"tuv",
            '9':"wxyz",
        }
        if(len(digits)>0):
            temp=list(d[digits[0]])
        else:
            return []
        for i in range(1,len(digits)):
            ans=temp[::]
            temp=[]
            for j in ans:
                for k in d[digits[i]]:
                    temp.append(j+k)
        return temp
s=Solution()
print(s.letterCombinations("234"))