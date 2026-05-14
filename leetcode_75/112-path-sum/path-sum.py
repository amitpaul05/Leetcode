# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
    # 1. Base case: if the node is empty, no path exists
        if not root:
            return False
        
        # 2. Check if it is a leaf node
        if not root.left and not root.right:
            return root.val == targetSum
        
        # 3. Recursively check subtrees with the remaining sum
        remaining_sum = targetSum - root.val
        return self.hasPathSum(root.left, remaining_sum) or self.hasPathSum(root.right, remaining_sum)