class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """ In-order Traversal: O(n), O(h)
        1. We track global res and prev node
        2. Recurse left
        2. At current node: if prev, update res = min(res, node - prev)
        3. Move prev to next node
        4. Recurse right
        """
        res = float('inf')
        prev = None 

        def dfs(node):
            nonlocal res, prev
            if not node:
                return
            
            dfs(node.left)
            if prev:
                res = min(res, node.val - prev.val)
            prev = node
            dfs(node.right)
        
        dfs(root)
        return res