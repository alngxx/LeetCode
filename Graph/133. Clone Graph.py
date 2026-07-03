"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        """
        BFS: O(V + E), O(V)
        1. Clone the start node, store mapping old -> new in visited dict
        2. BFS through original graph using queue
        3. For each node popped, go through its neighbors
        4. If neighbor not cloned yet, clone it and add to queue
        5. Connect current clone's neighbors list to the neighbor's clone
        """
        if not node:
            return None

        # map store old node -> cloned node
        clone = {}
        # create new Node object with same value as node, but neighbors defaults to []
        clone[node] = Node(node.val)
        q = deque([node])

        while q:
            cur = q.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in clone:
                    clone[neighbor] = Node(neighbor.val)
                    q.append(neighbor)

                # clone[cur] = clone of current node popped from queue
                # clone[neighbor] = clone of one of cur's original neighbors
                clone[cur].neighbors.append(clone[neighbor])
        
        return clone[node]