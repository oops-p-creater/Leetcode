# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        L1=""
        L2=""
        temp=l1
        while(temp!=None):
            L1=L1+str(temp.val)
            temp=temp.next
        temp=l2
        while(temp!=None):
            L2=L2+str(temp.val)
            temp=temp.next
        c=0
        ans=""
        for i in range(min(len(L1),len(L2))):
            x=int(L1[i])+int(L2[i])+c
            c=0
            if(x>9):
                c=x//10
            ans=ans+str(x%10)
        for j in range(i+1,max(len(L1),len(L2))):
            try:
                x=int(L2[j])+c
                c=0
                if(x>9):
                    c=x//10
                ans=ans+str(x%10)
            except:
                x=int(L1[j])+c
                c=0
                if(x>9):
                    c=x//10
                ans=ans+str(x%10)
        if(c!=0):
            ans=ans+str(c)
        print(ans)
        x=ans                                 
        res=None
        last=None
        for i in x:
            temp=ListNode(i)
            if(not res):
                res=temp
                last=res
            else:
                last.next=temp
                last=last.next
        return res
                
            
        