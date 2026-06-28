"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root:
            q = deque([root])
            while q:
                l_size = len(q)
                for i in range(l_size):
                    current = q.popleft()
                    if i < l_size-1:
                        current.next = q[0]
                    if current.left:
                        q.append(current.left)
                    if current.right:
                        q.append(current.right)
                current.next = None
        return root