class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head):
            return None
        elif(not head.next):
            return head
        else:
            
            p=head
            t=head.next
            p.next=t.next
            t.next=p
            head=t
            t,p=p,t
            k=t
            p=p.next
            if(p):
                p=p.next
            t=t.next
            if(t):
                t=t.next
            while(t):
                p.next=t.next
                t.next=p
                k.next=t
                k=p
                t,p=p,t
                p=p.next
                if(p):
                    p=p.next
                t=t.next
                if(t):
                    t=t.next
            return head
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(3)
head.next.next.next=ListNode(4)
head.next.next.next.next=ListNode(5)
head.next.next.next.next.next=ListNode(6)
head.next.next.next.next.next.next=ListNode(7)

s=Solution()
s.swapPairs(head)
while(head):
    print(head.val)
    head=head.next
