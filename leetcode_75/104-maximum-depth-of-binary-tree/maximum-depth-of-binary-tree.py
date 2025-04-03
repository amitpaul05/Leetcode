# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
# #         self.right = right
# class Solution:
#     def maxDepth(self, root: Optional[TreeNode]) -> int:
#         def max_depth(root, depth):
#             if not root:
#                 return depth
#             return max(max_depth(root.left, depth+1), max_depth(root.right, depth+1))

#         return max_depth(root, 0)

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        depth_l = self.maxDepth(root.left)
        depth_r = self.maxDepth(root.right)
        print(depth_l, depth_r)
        return max(depth_l, depth_r) + 1

        