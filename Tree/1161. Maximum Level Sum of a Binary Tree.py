class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        """ BFS + Queue: Caculate sum at every level and take max """
        max_sum = float('-inf')
        res = 1
        q = deque()
        q.append([root, 1])

        while q:
            cur_sum = 0      # sum at current level

            for _ in range(len(q)):
                node, level = q.popleft()
                cur_sum += node.val

                if node.left:
                    q.append([node.left, level + 1])
                if node.right:
                    q.append([node.right, level + 1])
            
            # if found greater sum, update max_sum and its level
            if cur_sum > max_sum:
                max_sum, res = cur_sum, level

        return res