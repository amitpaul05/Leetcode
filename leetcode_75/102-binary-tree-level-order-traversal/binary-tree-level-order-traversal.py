# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_vals = []
        if root:
            q = deque([root])

            while q:
                l_size = len(q)
                current_level_vals = []
                for i in range(l_size):
                    current = q.popleft()
                    current_level_vals.append(current.val)
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)

                level_vals.append(current_level_vals)
        return level_vals