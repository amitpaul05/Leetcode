# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q = deque([root])
        level = 1
        zigzag_nodes = []
        while q:
            l = len(q)
            level_nodes = []
            for i in range(l):
                current = q.popleft()
                if level % 2 == 0:
                    level_nodes.insert(0, current.val)
                else:
                    level_nodes.append(current.val)
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
            level += 1
            zigzag_nodes.append(level_nodes)
        return zigzag_nodes

