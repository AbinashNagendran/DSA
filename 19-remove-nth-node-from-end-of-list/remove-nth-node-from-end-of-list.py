# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first find the length 
        tr = head
        length = 0
        while(tr):
            tr = tr.next
            length+=1

        indexToDelete = length - n

        tr = head
        index = 0
        if index == indexToDelete:
            return head.next

        tr = tr.next
        index+=1
        pre = head
        while(tr):
            if index == indexToDelete:
                pre.next = tr.next
                break
            else:
                tr = tr.next
                pre = pre.next
                index+=1
        return head



                
            
        
        
        