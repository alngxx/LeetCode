# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        """
        Perform BFS that process every levels
        """
        res = []
        q = collections.deque()
        q.append(root)

        # Calculate average of each level by BFS
        while q:
            cur_sum = 0  # sum of each level
            cur_node = len(q)  # number of nodes in each level
            for _ in range(len(q)):
                node = q.popleft()
                cur_sum += node.val

                # Enqueue left/right child if exists
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(float(cur_sum / cur_node))
        return res
