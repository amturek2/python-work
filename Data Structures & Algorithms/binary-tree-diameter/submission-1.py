# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maximum = 0
        if not root: 
            return 0 

        self.dfsmax(root)
        return self.maximum 
        
    def dfsmax(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0 

        maxright = self.dfsmax(root.right)
        maxleft = self.dfsmax(root.left)
        self.maximum = max(self.maximum, maxright+ maxleft)
    
        return 1 + max(maxright,  maxleft )
