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
        ans = [root.val]
        counter = [0]


        def dfs(root):
            if root == None:
                return
            dfs(root.left)
            counter[0]+=1
            if counter[0] == k:
                ans[0] = root.val
                return
            dfs(root.right)
            return 
        dfs(root)
        return ans[0]
        