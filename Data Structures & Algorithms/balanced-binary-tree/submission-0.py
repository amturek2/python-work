# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # height balanced means within 1 

        # for each - you have to subtract right from left 
        # if the absolute value is more than 1 - you return false
        # otherwise you keep going 
        self.balanced = True 
        self.getHeight(root)
        return self.balanced 
        #each node stores it's height 

    def getHeight(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0

        heightLeft = self.getHeight(root.left)
        heightRight = self.getHeight(root.right)

        if abs(heightLeft - heightRight) > 1: 
            self.balanced = False 
        return 1 + max(heightLeft, heightRight)
        