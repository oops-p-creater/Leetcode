class Solution(object):
    def reverse(self, x):
        if(x<-2**31 or x>2**31-1):
            return 0
        elif(x==0):
            return 0
        else:
            x=str(x)
            x.strip("0")
            if(x[0]=="-"):
                x=x[1:][::-1]
                x=int(x)
                x=x*-1
                if(x<-2**31 or x>2**31-1):
                    return 0
                return x
            else:
                x=x[::-1]
                x=int(x)
                if(x<-2**31 or x>2**31-1):
                    return 0
                return x
            
        