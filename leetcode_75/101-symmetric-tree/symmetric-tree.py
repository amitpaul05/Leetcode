# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leftTreeEqualRightTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if root1.left and root2.right:
            if root1.left.val != root2.right.val:
                return False
            return self.leftTreeEqualRightTree(root1.left, root2.right)
        elif not root1.left and not root2.right:
            return True
        return False
    
    def rightTreeEqualLeftTree(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        print(root1.right, root2.left)
        if root1.right and root2.left:
            if root1.right.val != root2.left.val:
                return False
            return self.rightTreeEqualLeftTree(root1.right, root2.left)
        elif not root1.right and not root2.left:
            return True
        return False
        


    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def mirror(a, b):
            if a is None or b is None:
                return a is b
            return (
                a.val == b.val
                and mirror(a.left, b.right)
                and mirror(a.right, b.left)
            )

        return True if root is None else mirror(root.left, root.right)
        
