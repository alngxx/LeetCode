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
        """ BFS + Queue: O(n), O(w) 
        1. If no root, return None
        2. For each node in current level, set its next = next node in queue
        3. Last node in each level get its next = None (default)
        """
        if not root:
            return None

        q = deque([root])
        while q:
            level_size = len(q)

            for i in range(len(q)):
                node = q.popleft()
                if i < level_size - 1:          # if not last node in current level
                    node.next = q[0]            # point to next in queue
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return root