# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        self.ans = None
        self.counter = 0
        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            self.counter+=1
            if self.counter == k:
                self.ans = root.val
                return
            dfs(root.right)
            return 
        dfs(root)
        return self.ans
        