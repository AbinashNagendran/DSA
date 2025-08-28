"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        old_to_new = {}
        tr = head

        while(tr):
            new_node = Node(tr.val)
            old_to_new[tr] = new_node
            tr = tr.next

        tr = head
        new_head = old_to_new[head]
        curr = new_head
        while(tr):
            if tr.random:
                curr.random = old_to_new[tr.random]
            if tr.next:
                curr.next = old_to_new[tr.next]
            tr = tr.next
            curr = curr.next
        return new_head