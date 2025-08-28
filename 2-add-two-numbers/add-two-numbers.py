# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        cur = res
        tr1 = l1
        tr2 = l2
        carryOn = 0
        while(tr1 or tr2) or carryOn != 0:
            num1 = tr1.val if tr1 else 0
            num2 = tr2.val if tr2 else 0
            val = num1 + num2 + carryOn
            carryOn = val // 10
            digit = val % 10
            cur.next = ListNode(digit)
            cur = cur.next
            tr1 = tr1.next if tr1 else None 
            tr2 = tr2.next if tr2 else None 
        return res.next