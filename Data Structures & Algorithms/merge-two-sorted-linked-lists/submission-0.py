# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: 
            return 
        elif not list2: 
            return list1
        elif not list1:
            return list2

        if list1.val <= list2.val: 
            curr1, curr2 = list1, list2
            headToReturn = list1
        else: 
            curr1, curr2 = list2, list1
            headToReturn = list2

        while (curr1 and curr2):
            # merging second list value into first 
            if curr1.next and curr2.val < curr1.next.val: 
                # print("curr1", curr1.val,"curr2", curr2.val)
                tmp = curr1.next 
                curr1.next = curr2
                curr2 = curr2.next
                curr1 = curr1.next
                while (curr2 and curr2.val < tmp.val): 
                    curr1.next = curr2
                    curr1 = curr1.next
                    curr2 = curr2.next

                curr1.next = tmp 
                curr1 = curr1.next
            elif not curr1.next:
                curr1.next = curr2
                curr2 = None
            else: 
                curr1 = curr1.next

        return headToReturn

