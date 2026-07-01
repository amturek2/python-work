# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maximum = 0
        stack = []
        stack.append(root)
        while (stack):
            node = stack.pop()

            if node:
                maximum = max(maximum, self.maxDepth(node.left) + self.maxDepth(node.right))
                stack.append(node.right)
                stack.append(node.left)

        return maximum 


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))

# at root you get depth of right and depth of left, add them and maintain that max 
# at 2 you get depth of right and depth of left, add them and see if that is bigger than max 
# go until no root
# return max 

