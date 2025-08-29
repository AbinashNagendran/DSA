# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        def sameTree(root1, root2):
            if not root2 or not root1:
                if root2 or root1:
                    return False
                return True 
            if root1.val != root2.val:
                return False
            left = sameTree(root1.left, root2.left)
            right = sameTree(root1.right, root2.right)
            if left and right:
                return True 
            return False
            
        def dfs(root, subRoot):
            if root == None:
                return False
            if sameTree(root, subRoot):
                return True
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)

        return dfs(root, subRoot)
        