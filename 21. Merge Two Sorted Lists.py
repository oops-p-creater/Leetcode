# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if(not l1 and not l2):
            return None
        if(not l1):
            return l2
        if(not l2):
            return l1
        final=None
        temp=None
        while(l1 and l2):
            if(l1.val<l2.val):
                newTemp=ListNode(l1.val)
                if(not final):
                    
                    final=newTemp
                    temp=newTemp
                    l1=l1.next
                else:
                    temp.next=newTemp
                    temp=newTemp
                    l1=l1.next
            elif(l2.val<l1.val):
                newTemp=ListNode(l2.val)
                if(not final):
                    final=newTemp
                    temp=newTemp
                    l2=l2.next
                else:
                    temp.next=newTemp
                    temp=newTemp
                    
                    l2=l2.next
            else:
                newTemp=ListNode(l2.val)
                if(not final):
                    final=newTemp
                    temp=newTemp
                    l2=l2.next
                else:
                    temp.next=newTemp
                    temp=newTemp
                    
                    l2=l2.next
        if(l1):
            temp.next=l1
            return final
        if(l2):
            temp.next=l2
            return final
        return final
                
l1=ListNode(1)
l1.next=ListNode(2)
l1.next.next=ListNode(4)        
l2=ListNode(1)
l2.next=ListNode(3)
l2.next.next=ListNode(4)            
                
s=Solution()
x=(s.mergeTwoLists(l1,l2))
while(x):
    print(x.val)
    x=x.next

        