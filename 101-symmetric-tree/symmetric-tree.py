# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        q = deque() 
        q.append(root.left)
        q.append(root.right)
        while(q):
            l, r = q.popleft(), q.popleft()
            if not l and not r:
                continue
            if (not l and r) or (l and not r):
                return False
            if l.val != r.val:
                return False
            q.append(l.left)
            q.append(r.right)
            q.append(l.right)
            q.append(r.left)
        return True
        