class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        """ BFS - Node Indexing: O(n), O(n)
        1. Record [node, index] into queue
        2. Left child = 2 * index, right child = 2 * index + 1
        3. Width = last_index - first_index + 1
        4. Track max at every level
        """
        res = 0
        q = deque()
        q.append([root, 0])     # [node, index]

        while q:
            cur_level = []      # index of node in current level
            for _ in range(len(q)):
                node, index = q.popleft()
                cur_level.append(index)
                
                if node.left:
                    q.append([node.left, 2 * index])
                if node.right:
                    q.append([node.right, 2 * index + 1])
            
            # width of this level = last_index - first_index + 1
            width = cur_level[-1] - cur_level[0] + 1
            res = max(res, width)
        
        return res