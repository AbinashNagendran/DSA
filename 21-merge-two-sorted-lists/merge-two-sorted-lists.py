# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = ListNode()
        tr = merged

        while list1 and list2:
            if list1.val > list2.val: 
                tr.next = list2
                list2 = list2.next
            else:
                tr.next = list1
                list1 = list1.next
            tr = tr.next
        
        if list1:
            tr.next = list1
        else:
            tr.next = list2
        return merged.next
            
            
        
        