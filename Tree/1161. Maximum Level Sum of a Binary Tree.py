class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """
        BFS (Level-order traversal): Caculate sum at every level and take max
        """
        max_sum = -99999
        res = 0
        level = 1

        q = deque()
        q.append(root)

        while q:
            cur_sum = 0  # sum at current level

            for _ in range(len(q)):
                node = q.popleft()  
                cur_sum += node.val

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            # update max_sum and its corresponding level
            if max_sum < cur_sum:
                max_sum, res = cur_sum, level

            level += 1  

        return res
