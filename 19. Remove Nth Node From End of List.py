class ListNode(object):

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        
        temp=head
        c=0
        while(temp):
            temp=temp.next
            c=c+1
        
        if(c==1 and n==1):
            return None
        if(c==n):
            return head.next
        c=c-n-1
        temp=head
        while(c!=0):
            temp=temp.next
            c=c-1
            
        a=temp
        a.next=temp.next.next
        return head
        
s=Solution()
head=ListNode(1)
head.next=ListNode(2)
print(s.removeNthFromEnd(head,2))
print(head.val)