# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root1, root2):
            if not root2 or not root1:
                if root2 or root1:
                    return False
                return True 
            if root1.val != root2.val:
                return False
            left = dfs(root1.left, root2.left)
            right = dfs(root1.right, root2.right)

            if left and right:
                return True 
            return False

        return dfs(p, q)
        