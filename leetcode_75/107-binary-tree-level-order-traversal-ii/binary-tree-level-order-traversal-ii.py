# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        roots_from_bottom = []
        q = deque([root])
        while q:
            l = len(q)
            current_level = []
            for i in range(l):
                current = q.popleft()
                current_level.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            
            roots_from_bottom.insert(0, current_level)
        return roots_from_bottom