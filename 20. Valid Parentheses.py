class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if(len(s)%2!=0):
            return False
        l=[]
        f=0
        for i in s:
            if(i=="(" or i=="{" or i=="["):
                l.append(i)
            else:
                if(len(l)==0):
                    return False
                else:
                    if(len(l)>0 and i=="]"):
                        if(l[-1]=="["):
                            l.pop()
                            f=1
                            continue
                        else:
                            return False
                    if(len(l)>0 and i=="}"):
                        if( l[-1]=="{"):
                            l.pop()
                            f=1
                            continue
                        else:
                            return False
                    if(len(l)>0 and i==")"):
                        if(l[-1]=="("):
                            l.pop()
                            f=1
                            continue
                        else:
                            return False
        if(len(l)==0):
            return True
        else:
            return False
                
s=Solution()
print(s.isValid("("))
                    
        