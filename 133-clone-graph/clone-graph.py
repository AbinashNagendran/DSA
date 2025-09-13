"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        ref = {} # map nodes to cloned nodes

        def dfs(node):

            if node in ref: 
                return ref[node]

            copy = Node(node.val)
            ref[node] = copy
            for neighbour in node.neighbors: 
                copy.neighbors.append(dfs(neighbour))
            return copy
        
        return dfs(node) if node else None
        