# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ans = [0]

        def dfs(root, minValPath):
            if root == None:
                return
            
            if root.val >= minValPath:
                ans[0] = ans[0] + 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)
            else:
                dfs(root.left, minValPath)
                dfs(root.right, minValPath)
            return
        

        dfs(root, root.val)
        return ans[0]
        