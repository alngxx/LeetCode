class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        """ In-order Traversal: O(n), O(h)
        -  BST has: left < root < right
        -  Thus, in-order(left -> root -> right) gives nodes in ascending order
        - Return k-th node while traverse
        """
        count = res = 0 
        def dfs(node):
            nonlocal count
            nonlocal res

            # stop when res is found
            if not node or res:
                return
            
            # in-order traversal
            dfs(node.left)
            count += 1
            if count == k:
                res = node.val
            dfs(node.right)
        
        dfs(root)
        return res