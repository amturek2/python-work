# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        rootStr = self.serialize(root)
        subRootStr = self.serialize(subRoot)

        print(subRootStr)
        print(rootStr)
        return subRootStr in  rootStr


    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root: 
            return ",null"
        leftVal = self.serialize(root.left)
        rightVal = self.serialize(root.right)
        return "," +leftVal +",L" + str(root.val) + ",R" + rightVal

