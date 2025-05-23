# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def max_depth(root, depth):
            if not root:
                return depth
            return max(max_depth(root.left, depth+1), max_depth(root.right, depth+1))

        return max_depth(root, 0)


        