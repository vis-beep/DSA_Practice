# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumRootToLeaf(self, root):
        return self.dfs(root, 0)
    
    def dfs(self, node, current):
        if not node:
            return 0
        
        # shift left and add current node value
        current = current * 2 + node.val
        
        # if leaf node, return the binary number formed
        if not node.left and not node.right:
            return current
        
        # return sum of left and right subtree
        return self.dfs(node.left, current) + self.dfs(node.right, current)
        
