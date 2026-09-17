class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        """ DFS: O(n), O(h)
        1. dfs(node, cur_num): return sum of all root-to-leaf numbers from this node
        2. If node is None, return 0
        3. Build number: cur_num = cur_num * 10 + node.val
        4. If leaf, return cur_num (path complete)
        5. Otherwise return dfs(left) + dfs(right) to sum all paths
        """
        def dfs(node, cur_num):
            if not node:
                return 0 
            
            # add node as last digit
            cur_num = cur_num * 10 + node.val
            # if node is leaf, end this path
            if not node.left and not node.right:
                return cur_num
            
            return dfs(node.left, cur_num) + dfs(node.right, cur_num)
        return dfs(root, 0)