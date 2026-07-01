# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if not root: 
            return 
        
        return self.invert(root)

    def invert(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: 
            return root
        if not root.right and not root.left:
            return root

        tmp = root.left
        root.left = self.invert(root.right)
        root.right =self.invert(tmp)
        return root 
