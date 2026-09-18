class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        res = root.val

        # dfs(node) = max sum can get if going down from me
        def dfs(node):
            if not node:
                return 0
            
            # ignore negative path
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            # update max path sum through this node
            nonlocal res
            res = max(res, left + node.val + right)

            # tell max sum branch to parent node
            # dfs(20) = 20 + max(15, 7) = 35
            return node.val + max(left, right)
        
        dfs(root)
        return res