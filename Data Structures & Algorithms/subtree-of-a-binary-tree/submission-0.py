# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        need = subRoot.val 
        stack = []
        stack.append(root)
        node = None

        while stack: 
            node = stack.pop()
            if node:  
                if node.val == need: 
                    if (self.sameTree(node, subRoot)): 
                        return True
                stack.append(node.left)
                stack.append(node.right)

        return False

    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot and not root: 
            return True 
        if not root or not subRoot: 
            return False 
        if root.val != subRoot.val: 
            return False 

        return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right) 