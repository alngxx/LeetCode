# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        """ Iteration: O(h), O(1)
        1. cur = root, iterate indefinitely
        2. If val > cur.val:
        - If not cur.right: insert val as cur.right, return root
        - Otherwise: move cur = cur.right
        3. Else val <= cur.val: do similar
        """
        if not root:
            return TreeNode(val)
        
        cur = root
        while True:
            if val > cur.val:
                if not cur.right:
                    cur.right = TreeNode(val)
                    return root
                cur = cur.right
            else:
                if not cur.left:
                    cur.left = TreeNode(val)
                    return root
                cur = cur.left