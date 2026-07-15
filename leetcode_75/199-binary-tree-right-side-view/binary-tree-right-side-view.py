# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        right_tree = []
        if root:
            q = deque([root])

            while q:
                l = len(q)
                for i in range(l):
                    c = q.popleft()
                    if i == l-1:
                        right_tree.append(c.val)
                    if c.left:
                        q.append(c.left)
                    if c.right:
                        q.append(c.right)
                
        return right_tree