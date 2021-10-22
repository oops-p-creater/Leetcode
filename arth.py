def check(l):
    c=1
    final=0
    l.sort()
    for i in range(len(l)-1):
        if(abs(l[i+1]-l[i])==1):
            c=c+1
        else:
            c=1
            final=max(c,final)
    return max(c,final)
def buildingHouses(queries):
    ans=[]
    ans.append(queries[0])
    c=1
    k=[]
    k.append(c)
    final2=1
    for i in range(1,len(queries)):
        ans.append(queries[i])
        final2=max(check(ans),final2)
        k.append(final2)
    return(k)
print(buildingHouses([-8,-4,-7,-3,-2,0,-9,1,-5,-1]))