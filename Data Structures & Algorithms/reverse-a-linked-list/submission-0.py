class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head: 
            return 

        curr = head
        prev = None
        while(curr != None):
            tmp = curr.next 
            curr.next = prev 
            prev = curr
            curr = tmp 
        return prev