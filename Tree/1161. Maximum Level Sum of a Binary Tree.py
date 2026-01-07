class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        BFS (Level-order traversal): Caculate sum at every level and take max
        """
        from collections import deque  # double-ended queue

        max_sum = -99999
        res = 0
        level = 1  # initial level

        # Queue for BFS (level-order traversal)
        q = deque()
        q.append(root)

        while q:
            cur_sum = 0  # sum at current level
            # Iterate all nodes in current level
            for _ in range(len(q)):
                node = q.popleft()  # q.dequeue()
                cur_sum += node.val

                # Add left and right child if exists
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # Update max_sum and its corresponding level
            if max_sum < cur_sum:
                max_sum, res = cur_sum, level

            level += 1  # move to next level

        return res
