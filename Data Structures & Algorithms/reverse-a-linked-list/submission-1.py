class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: 
            return 

        newHead = head 
        if head.next: 
            newHead = self.reverseList(head.next)
            head.next.next = head 
        head.next = None 

        return newHead