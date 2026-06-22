# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        # Step 1: Swap the left and right child pointers
        root.left, root.right = root.right, root.left
        
        # Step 2: Recursively invert both the left and right subtrees till the base case
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root