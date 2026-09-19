# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        """ DFS in-order: O(n), O(h)
        1. Init global prev = None, and res = True
        2. Recurse left
        3. If prev and prev.val >= node.val: update res = False
        4. Advance prev to current node
        5. Recurse right
        """
        res = True
        prev = None

        def dfs(node):
            nonlocal res, prev
            if not node or res == False:
                return
            
            dfs(node.left)
            if prev and prev.val >= node.val:
                res = False

            prev = node         # advance prev to current node
            dfs(node.right)
        
        dfs(root)
        return res