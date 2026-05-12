# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if (not root.left and not root.right):
            return 1
        queue = deque([root])
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
        level = 2
        while queue:
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if not current_node.left and not current_node.right:
                    return level
                else:
                    if current_node.left:
                        queue.append(current_node.left)
                    if current_node.right:
                        queue.append(current_node.right)
            level += 1

        return level
