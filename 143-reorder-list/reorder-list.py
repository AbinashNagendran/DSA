# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while(fast != None and fast.next != None):
            fast = fast.next.next
            slow = slow.next
        
        l1 = head
        l2 = slow.next
        slow.next = None

        def reverseList(head):
            if not head: 
                return None 
            pre = head
            tr = head.next
            while tr != None:
                temp = tr.next
                tr.next = pre
                pre = tr
                tr = temp
            head.next = None 
            return pre
        l2 = reverseList(l2)

        while(l2 != None):
            nextNode = l2.next
            temp = l1.next
            l1.next = l2
            l2.next = temp
            l1 = l2.next
            l2 = nextNode



        